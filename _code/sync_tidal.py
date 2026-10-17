"""
Sync your Tidal favorite albums into the vault.

Run from anywhere:
    python _code/sync_tidal.py --dry-run     # see what would change; writes nothing
    python _code/sync_tidal.py               # do it

Options: [--dry-run] [--refresh-tracklists] [--fix-years]
   (default)             add new albums; fill in missing tracklists, "added" dates and cover links;
                         flag albums you've removed from your Tidal favorites
   --dry-run             print what would change, write nothing
   --refresh-tracklists  replace every tracklist with Tidal's, keeping your ratings
   --fix-years           set each album's year to its original release year (slow: one MusicBrainz lookup per album)
"""
import json
import os
import re
import sys
import time

import requests
import tidalapi

from common import (VAULT, COVERS_FOLDER, SESSION_FILE, album_notes, create_genre_page, get_field,
                    musicbrainz_lookup, musicbrainz_tracklist, read_note, resolve_tags, sanitize,
                    set_field, unquote, write_note)

DRY_RUN = "--dry-run" in sys.argv
REFRESH_TRACKLISTS = "--refresh-tracklists" in sys.argv
FIX_YEARS = "--fix-years" in sys.argv
if "--overwrite" in sys.argv:
    print("--overwrite was removed (it could lose ratings). Use --refresh-tracklists and/or --fix-years instead.")
    sys.exit(1)
if DRY_RUN:
    print("DRY RUN: nothing will be written.\n")


# ── Load session ──────────────────────────────────────────
session = tidalapi.Session()

if not os.path.exists(SESSION_FILE):
    print("No session file found. Attempting to authenticate with Tidal...")
    print("A browser window or login URL will appear. Complete the login to continue.")
    try:
        session.login_oauth_simple()
        with open(SESSION_FILE, "w") as f:
            json.dump({
                "token_type": session.token_type,
                "access_token": session.access_token,
                "refresh_token": session.refresh_token,
                "expiry_time": str(session.expiry_time)
            }, f)
        print("Authentication successful! Session saved.\n")
    except Exception as e:
        print(f"Authentication failed: {e}")
        sys.exit(1)
else:
    try:
        with open(SESSION_FILE, "r") as f:
            data = json.load(f)
        loaded = session.load_oauth_session(
            data["token_type"],
            data["access_token"],
            data["refresh_token"],
            data["expiry_time"]
        )
        if not loaded:
            raise Exception("Session expired")
        print("Session loaded successfully.\n")
    except Exception as e:
        print(f"Session load failed ({e}). Re-authenticating...")
        try:
            session.login_oauth_simple()
            with open(SESSION_FILE, "w") as f:
                json.dump({
                    "token_type": session.token_type,
                    "access_token": session.access_token,
                    "refresh_token": session.refresh_token,
                    "expiry_time": str(session.expiry_time)
                }, f)
            print("Re-authentication successful!\n")
        except Exception as e2:
            print(f"Re-authentication failed: {e2}")
            sys.exit(1)

# ── Fetch all Tidal albums ────────────────────────────────
print("Fetching your Tidal library...")
favorites = tidalapi.Favorites(session, session.user.id)

all_albums = []
offset = 0
limit = 50

while True:
    batch = favorites.albums(limit=limit, offset=offset)
    if not batch:
        break
    all_albums.extend(batch)
    print(f"Fetched {len(all_albums)} albums so far...")
    offset += limit  # keep going until Tidal returns an empty page (short pages happen)

all_albums = list({str(a.id): a for a in all_albums}.values())  # pages can overlap if favorites change mid-fetch
print(f"Found {len(all_albums)} albums on Tidal.\n")

os.makedirs(COVERS_FOLDER, exist_ok=True)

TABLE_HEADER = ["| # | Title | Duration | Rating /10 |", "|---|-------|----------|------------|"]
ROW_RE = re.compile(r"^\|\s*([\d]+(?:-\d+)?)\s*\|\s*(.*?)\s*\|\s*([\d:]*)\s*\|\s*([0-9.]*)\s*\|\s*$")


def read_ratings(text):
    """Existing ratings by track title, by track number, and by row position."""
    by_title, by_num, by_pos = {}, {}, []
    for line in text.split("\n"):
        r = ROW_RE.match(line)
        if r:
            by_pos.append(r.group(4))
            if r.group(4):
                by_title[r.group(2).strip().lower()] = r.group(4)
                by_num[r.group(1)] = r.group(4)
    return by_title, by_num, by_pos


def build_table(tracks, ratings=({}, {}, [])):
    """Returns (table, ratings_kept). A rating carries over by title, then track number,
    then row position (only when both lists have the same number of tracks)."""
    by_title, by_num, by_pos = ratings
    same_length = len(by_pos) == len(tracks)
    lines, kept = list(TABLE_HEADER), 0
    for i, tr in enumerate(tracks):
        title = str(tr["title"]).replace("|", "-")
        rating = (by_title.get(title.lower()) or by_num.get(str(tr["num"]))
                  or (by_pos[i] if same_length else "") or "")
        kept += bool(rating)
        lines.append(f"| {tr['num']} | {title} | {tr['duration']} | {rating} |")
    return "\n".join(lines), kept


def replace_table(text, table):
    """Swap the tracklist table for a new one, or add one under the album view if there is none."""
    lines = text.split("\n")
    start = next((i for i, l in enumerate(lines) if l.startswith("| # |")), None)
    if start is None:
        stub = text.find('await dv.view("_scripts/album");')
        if stub == -1:
            return text.rstrip("\n") + "\n\n" + table + "\n"
        end = text.find("```", stub) + 3
        return text[:end] + "\n\n" + table + "\n" + text[end:].lstrip("\n")
    end = start
    while end < len(lines) and lines[end].startswith("|"):
        end += 1
    return "\n".join(lines[:start] + table.split("\n") + lines[end:])


def has_table(text):
    return any(l.startswith("| # |") for l in text.split("\n"))


def tidal_tracklist(album):
    """Tracklist straight from Tidal, so it matches the edition you actually stream."""
    try:
        items, offset = [], 0
        while True:
            batch = album.tracks(limit=100, offset=offset)
            items.extend(batch)
            if len(batch) < 100:
                break
            offset += 100
    except Exception as e:
        print(f"   Tidal tracklist error: {e}")
        return []
    discs = {getattr(t, "volume_num", 1) or 1 for t in items}
    tracks = []
    for t in items:
        name = t.name or ""
        version = getattr(t, "version", None)
        if version and version.lower() not in name.lower():
            name = f"{name} ({version})"
        secs = int(getattr(t, "duration", 0) or 0)
        m, s = divmod(secs, 60)
        num = f"{t.volume_num}-{t.track_num}" if len(discs) > 1 else str(t.track_num)
        tracks.append({"num": num, "title": name, "duration": f"{m}:{s:02d}" if secs else ""})
    return tracks


def original_year(tidal_year, mb_year):
    """Tidal often reports the reissue/remaster year; MusicBrainz knows the first release.
    Only trust MusicBrainz when it's 2+ years earlier: 1-year gaps are usually a
    pre-release single or promo, not a reissue."""
    if mb_year and tidal_year and mb_year <= tidal_year - 2:
        return mb_year
    return tidal_year or mb_year or "Unknown"


def date_added(album):
    d = getattr(album, "user_date_added", None)
    return d.strftime("%Y-%m-%d") if d else None


def name_keys(artist, title):
    return {(sanitize(artist).lower(), sanitize(title).lower())}


notes_by_id, notes_by_name = {}, {}
for _path, _text, _ in album_notes():
    notes_by_id.setdefault(str(get_field(_text, "tidal_id")), _path)
    folder_name = os.path.basename(os.path.dirname(_path))
    file_title = re.sub(r"\s\(\d{4}\)$", "", os.path.splitext(os.path.basename(_path))[0])
    keys = name_keys(folder_name, file_title) | name_keys(unquote(get_field(_text, "artist")), unquote(get_field(_text, "title")))
    for k in keys:
        notes_by_name.setdefault(k, []).append(_path)
print(f"Indexed {len(notes_by_id)} existing album notes.\n")


def download_cover(album, cover_filepath):
    if os.path.exists(cover_filepath) or DRY_RUN:
        return
    try:
        response = requests.get(album.image(640), timeout=10)
        if response.status_code == 200:
            with open(cover_filepath, "wb") as img_file:
                img_file.write(response.content)
    except Exception as e:
        print(f"   Could not download cover for {album.name}: {e}")

stats = {k: 0 for k in ["created", "id_changed", "untouched", "tracklist_filled", "tracklist_refreshed",
                        "year_fixed", "added_date", "cover_linked", "removed", "restored"]}
favorite_ids = {str(a.id) for a in all_albums}

print("=" * 50)
print("SYNCING: Tidal -> Obsidian" + ("  (dry run)" if DRY_RUN else ""))
print("=" * 50)

for album in all_albums:
    artist = sanitize(album.artist.name)
    title = sanitize(album.name)
    tidal_id = str(album.id)
    cover_filename = f"{artist} - {title}.jpg"
    cover_filepath = os.path.join(COVERS_FOLDER, cover_filename)

    existing_path = notes_by_id.get(tidal_id)
    old_id = None
    if not existing_path:
        # Same album under a new Tidal ID (labels re-deliver albums): the note whose
        # artist + title match and whose own ID is no longer in your favorites.
        for path in notes_by_name.get((artist.lower(), title.lower()), []):
            pid = str(get_field(read_note(path)[0], "tidal_id"))
            if pid not in favorite_ids:
                existing_path, old_id = path, pid
                notes_by_id.pop(pid, None)
                notes_by_id[tidal_id] = path
                break

    if not existing_path or not get_field(read_note(existing_path)[0], "cover"):
        download_cover(album, cover_filepath)
    cover_value = f'"[[_covers/{cover_filename}]]"' if os.path.exists(cover_filepath) else None

    # ── Existing note: only fill in what's missing (plus the opt-in refreshes) ──
    if existing_path:
        text, crlf = read_note(existing_path)
        new = text
        label = os.path.relpath(existing_path, VAULT)

        if old_id:
            new = set_field(new, "tidal_id", tidal_id)
            stats["id_changed"] += 1
            print(f"Tidal ID changed {old_id} -> {tidal_id}, note kept: {label}")
        if get_field(new, "removed_from_tidal"):
            new = set_field(new, "removed_from_tidal", None)
            stats["restored"] += 1
            print(f"Back in favorites: {label}")
        added = date_added(album)
        if added and not get_field(new, "added"):
            new = set_field(new, "added", added)
            stats["added_date"] += 1
        if cover_value and not get_field(new, "cover"):
            new = set_field(new, "cover", cover_value)
            stats["cover_linked"] += 1

        if REFRESH_TRACKLISTS or not has_table(new):
            tracks = tidal_tracklist(album)
            if tracks:
                was = has_table(new)
                old_ratings = read_ratings(new)
                table, kept = build_table(tracks, old_ratings)
                if kept < len(old_ratings[0]):
                    print(f"SKIPPED tracklist refresh, {len(old_ratings[0]) - kept} rating(s) wouldn't carry over: {label}")
                else:
                    new = replace_table(new, table)
                    stats["tracklist_refreshed" if was else "tracklist_filled"] += 1
                    print(f"{'Refreshed' if was else 'Added'} tracklist ({len(tracks)} tracks): {label}")

        if FIX_YEARS:
            _, _, mb_year = musicbrainz_lookup(album.artist.name, album.name)
            current = get_field(new, "year")
            year = original_year(album.year, mb_year)
            if str(year) != str(current) and year != "Unknown":
                new = set_field(new, "year", year)
                stats["year_fixed"] += 1
                print(f"Year {current} -> {year}: {label}")

        if new != text:
            write_note(existing_path, new, crlf, DRY_RUN)
        else:
            stats["untouched"] += 1
        continue

    # ── New album ──
    print(f"\nNew: {album.artist.name} - {album.name}")
    mb_tags_raw, mbid, mb_year = musicbrainz_lookup(album.artist.name, album.name)
    year = original_year(album.year, mb_year)

    note_tags = resolve_tags(mb_tags_raw) if mb_tags_raw else []
    print(f"   Tags: {note_tags or 'none found'}")
    for tag in note_tags:
        create_genre_page(tag, DRY_RUN)

    tracks = tidal_tracklist(album) or musicbrainz_tracklist(mbid)
    print(f"   Tracklist: {len(tracks)} tracks" if tracks else "   No tracklist found")

    fields = [
        f"title: {json.dumps(album.name, ensure_ascii=False)}",
        f"artist: {json.dumps(album.artist.name, ensure_ascii=False)}",
        f"year: {year}",
        f"tidal_id: {tidal_id}",
    ]
    if cover_value:
        fields.append(f"cover: {cover_value}")
    if date_added(album):
        fields.append(f"added: {date_added(album)}")
    fields.append("tags:" + ("".join(f"\n  - {t}" for t in note_tags) if note_tags else " []"))
    fields.append("rating:")
    content = "---\n" + "\n".join(fields) + "\n---\n\n```dataviewjs\nawait dv.view(\"_scripts/album\");\n```\n"
    if tracks:
        content += "\n" + build_table(tracks)[0] + "\n"

    folder = os.path.join(VAULT, artist)
    filepath = os.path.join(folder, f"{title} ({year}).md")
    if os.path.exists(filepath):  # a different album with the same name: never overwrite it
        filepath = os.path.join(folder, f"{title} ({year}) {tidal_id}.md")
    if not DRY_RUN:
        os.makedirs(folder, exist_ok=True)
    write_note(filepath, content, dry_run=DRY_RUN)
    notes_by_id[tidal_id] = filepath
    stats["created"] += 1
    print(f"   Created: {os.path.relpath(filepath, VAULT)}")

# ── Albums no longer in your Tidal favorites ──────────────
# They're kept (with your ratings) and flagged; adding them back to favorites clears the flag.
today = time.strftime("%Y-%m-%d")
missing = [tid for tid in notes_by_id if tid not in favorite_ids]
if len(missing) > max(25, len(notes_by_id) // 5):
    print(f"\nWARNING: {len(missing)} albums aren't in the favorites list Tidal returned. That looks like an")
    print("incomplete download, not real removals, so nothing was flagged. Run the sync again later.")
    missing = []
for tid, path in sorted(((t, notes_by_id[t]) for t in missing), key=lambda x: x[1]):
    if not os.path.exists(path):
        continue
    text, crlf = read_note(path)
    if get_field(text, "removed_from_tidal") or str(get_field(text, "tidal_id")) in favorite_ids:
        continue
    write_note(path, set_field(text, "removed_from_tidal", today), crlf, DRY_RUN)
    stats["removed"] += 1
    print(f"Not in Tidal favorites anymore: {os.path.relpath(path, VAULT)}")

# ── Summary ───────────────────────────────────────────────
print("\n" + "=" * 50)
print("SYNC COMPLETE" + ("  (dry run: nothing was written)" if DRY_RUN else ""))
print("=" * 50)
print(f"  New albums:                         {stats['created']}")
print(f"  Tidal ID changed (note kept):       {stats['id_changed']}")
print(f"  Tracklists added (were missing):    {stats['tracklist_filled']}")
print(f"  Tracklists refreshed from Tidal:    {stats['tracklist_refreshed']}")
print(f"  Years corrected:                    {stats['year_fixed']}")
print(f"  'added' dates filled in:            {stats['added_date']}")
print(f"  Cover links filled in:              {stats['cover_linked']}")
print(f"  Flagged as removed from favorites:  {stats['removed']}")
print(f"  Back in favorites (flag cleared):   {stats['restored']}")
print(f"  Unchanged:                          {stats['untouched']}")
print("\nNext: if new tags were added, run  python _code/library.py tags --apply")
