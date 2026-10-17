import tidalapi
import json
import os
import re
import requests
import sys
import time
import random
import string
from difflib import SequenceMatcher

from tag_rules import normalize_tag, normalize_list, is_known, CANONICAL

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SESSION_FILE = os.path.join(SCRIPT_DIR, "tidal_session.json")
MUSICBRAINZ_APP = "ObsidianTidalSync/1.0 (nathanmontalvo1222@gmail.com)"

# Usage: python sync_tidal.py [--dry-run] [--refresh-tracklists] [--fix-years]
#   (default)             add new albums; fill in missing tracklists, "added" dates and cover links;
#                         flag albums you've removed from your Tidal favorites
#   --dry-run             print what would change, write nothing
#   --refresh-tracklists  replace every tracklist with Tidal's, keeping your ratings
#   --fix-years           set each album's year to its original release year (slow: one MusicBrainz lookup per album)
DRY_RUN = "--dry-run" in sys.argv
REFRESH_TRACKLISTS = "--refresh-tracklists" in sys.argv
FIX_YEARS = "--fix-years" in sys.argv
if "--overwrite" in sys.argv:
    print("--overwrite was removed (it could lose ratings). Use --refresh-tracklists and/or --fix-years instead.")
    sys.exit(1)
if DRY_RUN:
    print("DRY RUN: nothing will be written.\n")

VAULT_PATH = SCRIPT_DIR  # this script lives at the vault root
ALBUMS_FOLDER = VAULT_PATH
COVERS_FOLDER = os.path.join(VAULT_PATH, "_covers")
GENRES_FOLDER = os.path.join(VAULT_PATH, "00 Dashboard", "Genres")
IGNORE_FOLDERS = {"_covers", "_templates", ".obsidian", "00 Dashboard"}

IGNORE_TAGS = {
    "seen live", "favorites", "favourite", "love", "awesome", "great",
    "beautiful", "amazing", "excellent", "good", "best", "under 2000",
    "party", "inspiring", "charity", "new release", "newrelease",
    "compilations", "compilation", "soundtrack", "reissue", "deluxe",
    "albums i own", "check out", "fun", "epic",
}

if not os.path.exists(SESSION_FILE):
    print("ERROR: No session file found.")
    print("Please run this script in a terminal first to authenticate with Tidal.")
    print(f"Expected session file at: {os.path.abspath(SESSION_FILE)}")
    sys.exit(1)

def sanitize(name):
    name = str(name)
    name = re.sub(r'[\\/*?:"<>|]', "-", name)
    name = re.sub(r'[…]', '...', name)
    name = name.strip('. ')
    return name

def slugify_tag(tag):
    return ''.join(word.capitalize() for word in re.sub(r'[^a-zA-Z0-9 ]', '', tag).split())

def rand_id(length=4):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def fuzzy_match(tag, existing_tags, threshold=0.82):
    tag_lower = tag.lower().replace(" ", "").replace("-", "")
    best_match = None
    best_ratio = 0
    for existing in existing_tags:
        existing_lower = existing.lower().replace(" ", "").replace("-", "")
        ratio = SequenceMatcher(None, tag_lower, existing_lower).ratio()
        if ratio > best_ratio:
            best_ratio = ratio
            best_match = existing
    if best_ratio >= threshold:
        return best_match
    return None

def get_existing_tags():
    tags = []
    if not os.path.exists(GENRES_FOLDER):
        return tags
    for filename in os.listdir(GENRES_FOLDER):
        if filename.endswith(".md"):
            tag = filename.replace(".md", "")
            tags.append(slugify_tag(tag))
    return tags

_last_mb_request = 0.0

def mb_get(url, params):
    """GET from MusicBrainz at no more than ~1 request/second, retrying when it
    answers 503 (its "slow down" response) instead of losing the lookup."""
    global _last_mb_request
    for attempt in range(5):
        wait = 1.1 - (time.time() - _last_mb_request)
        if wait > 0:
            time.sleep(wait)
        _last_mb_request = time.time()
        response = requests.get(url, params=params, headers={"User-Agent": MUSICBRAINZ_APP}, timeout=15)
        if response.status_code == 503 and attempt < 4:
            time.sleep(2 ** attempt * 2)  # 2, 4, 8, 16 seconds
            continue
        response.raise_for_status()
        return response

def musicbrainz_get_tags(artist, album):
    try:
        url = "https://musicbrainz.org/ws/2/release/"
        params = {
            "query": f'release:"{album}" AND artist:"{artist}"',
            "fmt": "json",
            "limit": 5,
            "inc": "release-groups"
        }
        headers = {"User-Agent": MUSICBRAINZ_APP}
        response = mb_get(url, params)
        data = response.json()
        releases = data.get("releases", [])
        if not releases:
            return [], None, None

        release = releases[0]
        mbid = release.get("id")
        rg_id = release.get("release-group", {}).get("id")

        if not rg_id:
            return [], mbid, None

        rg_url = f"https://musicbrainz.org/ws/2/release-group/{rg_id}"
        rg_params = {"fmt": "json", "inc": "tags+genres"}
        rg_response = mb_get(rg_url, rg_params)
        rg_data = rg_response.json()

        tags = []
        genres = rg_data.get("genres", [])
        if genres:
            genres_sorted = sorted(genres, key=lambda x: x.get("count", 0), reverse=True)
            tags = [g["name"] for g in genres_sorted]
        else:
            raw_tags = rg_data.get("tags", [])
            tags_sorted = sorted(raw_tags, key=lambda x: x.get("count", 0), reverse=True)
            tags = [t["name"] for t in tags_sorted]

        first = (rg_data.get("first-release-date") or "")[:4]
        return tags, mbid, int(first) if first.isdigit() else None

    except Exception as e:
        print(f"   MusicBrainz tags error: {e}")
        return [], None, None

def musicbrainz_get_tracklist(mbid):
    if not mbid:
        return []
    try:
        url = f"https://musicbrainz.org/ws/2/release/{mbid}"
        params = {"fmt": "json", "inc": "recordings"}
        headers = {"User-Agent": MUSICBRAINZ_APP}
        response = mb_get(url, params)
        data = response.json()

        tracks = []
        media = data.get("media", [])
        for medium in media:
            disc_num = medium.get("position", 1)
            show_disc = len(media) > 1
            for track in medium.get("tracks", []):
                num = track.get("position", "")
                title = track.get("title", "") or track.get("recording", {}).get("title", "")
                length_ms = track.get("length") or track.get("recording", {}).get("length")
                if length_ms:
                    total_secs = int(length_ms) // 1000
                    m, s = divmod(total_secs, 60)
                    duration = f"{m}:{s:02d}"
                else:
                    duration = ""
                tracks.append({
                    "num": f"{disc_num}-{num}" if show_disc else num,
                    "title": title,
                    "duration": duration,
                    "rating": ""
                })
        return tracks

    except Exception as e:
        print(f"   MusicBrainz tracklist error: {e}")
        return []

def is_valid_genre_tag(tag):
    tag_clean = tag.lower().strip()
    if re.match(r'^\d+$', tag_clean):
        return False
    if tag_clean in IGNORE_TAGS:
        return False
    if len(tag_clean) < 3:
        return False
    return True

def resolve_tags(mb_tags, existing_tags):
    """MusicBrainz tags -> up to 4 canonical tags, using _scripts/tags.json."""
    resolved = []
    for raw_tag in mb_tags:
        if len(resolved) >= 4:
            break
        if not is_valid_genre_tag(raw_tag):
            print(f"   Skipping tag: {raw_tag}")
            continue
        if is_known(raw_tag):
            tag = normalize_tag(raw_tag)  # canonical, or None if blocklisted
        else:
            match = fuzzy_match(raw_tag, CANONICAL)
            tag = match or normalize_tag(slugify_tag(raw_tag))
            if not match:
                print(f"   New tag (add to _scripts/tags.json if it's a keeper): {tag}")
        if tag and tag not in resolved:
            resolved.append(tag)
            if tag not in existing_tags:
                existing_tags.append(tag)
    return resolved[:4]

def create_genre_note(tag):
    """Genre page = one line; _scripts/playlist.js draws it using the note's name as the tag."""
    os.makedirs(GENRES_FOLDER, exist_ok=True)
    filepath = os.path.join(GENRES_FOLDER, f"{tag}.md")
    if os.path.exists(filepath):
        return
    with open(filepath, "w", encoding="utf-8") as f:
        f.write('```dataviewjs\nawait dv.view("_scripts/playlist", { tags: [dv.current().file.name], genre: true });\n```\n')
    print(f"   Created genre note: {tag}.md")

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
    offset += limit
    if len(batch) < limit:
        break

print(f"Found {len(all_albums)} albums on Tidal.\n")

os.makedirs(ALBUMS_FOLDER, exist_ok=True)
os.makedirs(COVERS_FOLDER, exist_ok=True)
os.makedirs(GENRES_FOLDER, exist_ok=True)

existing_tags = get_existing_tags()
print(f"Loaded {len(existing_tags)} existing genre tags.\n")
# ── Note helpers ──────────────────────────────────────────
TABLE_HEADER = ["| # | Title | Duration | Rating /10 |", "|---|-------|----------|------------|"]
ROW_RE = re.compile(r"^\|\s*([\d]+(?:-\d+)?)\s*\|\s*(.*?)\s*\|\s*([\d:]*)\s*\|\s*([0-9.]*)\s*\|\s*$")


def read_note(path):
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()
    return raw.replace("\r\n", "\n"), "\r\n" in raw


def write_note(path, text, crlf=False):
    if DRY_RUN:
        return
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text.replace("\n", "\r\n") if crlf else text)


def get_field(text, key):
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return None
    f = re.search(rf"^{re.escape(key)}:[ \t]*(.*)$", m.group(1), re.M)
    return f.group(1).strip() if f else None


def set_field(text, key, value):
    """Set (or with value=None remove) one frontmatter property, leaving everything else as is."""
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return text
    fm = m.group(1)
    line = re.compile(rf"^{re.escape(key)}:[^\n]*\n?", re.M)
    if value is None:
        fm = line.sub("", fm).rstrip("\n")
    elif line.search(fm + "\n"):
        fm = line.sub(f"{key}: {value}\n", fm + "\n", count=1).rstrip("\n")
    elif re.search(r"^tags:", fm, re.M):
        fm = re.sub(r"^tags:", f"{key}: {value}\ntags:", fm, count=1, flags=re.M)
    else:
        fm = fm + f"\n{key}: {value}"
    return "---\n" + fm + "\n---" + text[m.end():]


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


def index_notes_by_tidal_id():
    """tidal_id -> note path, so a renamed artist or changed year never makes a second note."""
    index = {}
    for root, dirs, files in os.walk(ALBUMS_FOLDER):
        dirs[:] = [d for d in dirs if d not in IGNORE_FOLDERS and not d.startswith((".", "_"))]
        for filename in files:
            if not filename.endswith(".md"):
                continue
            path = os.path.join(root, filename)
            with open(path, "r", encoding="utf-8") as f:
                head = f.read(2000)
            m = re.search(r"^tidal_id:\s*(\S+)", head, re.MULTILINE)
            if m:
                index.setdefault(m.group(1), path)
    return index


notes_by_id = index_notes_by_tidal_id()
print(f"Indexed {len(notes_by_id)} existing album notes.\n")

stats = {k: 0 for k in ["created", "untouched", "tracklist_filled", "tracklist_refreshed",
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

    if not os.path.exists(cover_filepath) and not DRY_RUN:
        try:
            response = requests.get(album.image(640), timeout=10)
            if response.status_code == 200:
                with open(cover_filepath, "wb") as img_file:
                    img_file.write(response.content)
        except Exception as e:
            print(f"   Could not download cover for {title}: {e}")
    cover_value = f'"[[_covers/{cover_filename}]]"' if os.path.exists(cover_filepath) else None

    existing_path = notes_by_id.get(tidal_id)

    # ── Existing note: only fill in what's missing (plus the opt-in refreshes) ──
    if existing_path:
        text, crlf = read_note(existing_path)
        new = text
        label = os.path.relpath(existing_path, ALBUMS_FOLDER)

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
            _, _, mb_year = musicbrainz_get_tags(album.artist.name, album.name)
            current = get_field(new, "year")
            year = original_year(album.year, mb_year)
            if str(year) != str(current) and year != "Unknown":
                new = set_field(new, "year", year)
                stats["year_fixed"] += 1
                print(f"Year {current} -> {year}: {label}")

        if new != text:
            write_note(existing_path, new, crlf)
        else:
            stats["untouched"] += 1
        continue

    # ── New album ──
    print(f"\nNew: {album.artist.name} - {album.name}")
    mb_tags_raw, mbid, mb_year = musicbrainz_get_tags(album.artist.name, album.name)
    year = original_year(album.year, mb_year)

    note_tags = resolve_tags(mb_tags_raw, existing_tags) if mb_tags_raw else []
    print(f"   Tags: {note_tags or 'none found'}")
    if not DRY_RUN:
        for tag in note_tags:
            create_genre_note(tag)

    tracks = tidal_tracklist(album) or musicbrainz_get_tracklist(mbid)
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

    folder = os.path.join(ALBUMS_FOLDER, artist)
    filepath = os.path.join(folder, f"{title} ({year}).md")
    if not DRY_RUN:
        os.makedirs(folder, exist_ok=True)
    write_note(filepath, content)
    notes_by_id[tidal_id] = filepath
    stats["created"] += 1
    print(f"   Created: {artist}/{title} ({year}).md")

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
    if get_field(text, "removed_from_tidal"):
        continue
    write_note(path, set_field(text, "removed_from_tidal", today), crlf)
    stats["removed"] += 1
    print(f"Not in Tidal favorites anymore: {os.path.relpath(path, ALBUMS_FOLDER)}")

# ── Summary ───────────────────────────────────────────────
print("\n" + "=" * 50)
print("SYNC COMPLETE" + ("  (dry run: nothing was written)" if DRY_RUN else ""))
print("=" * 50)
print(f"  New albums:                         {stats['created']}")
print(f"  Tracklists added (were missing):    {stats['tracklist_filled']}")
print(f"  Tracklists refreshed from Tidal:    {stats['tracklist_refreshed']}")
print(f"  Years corrected:                    {stats['year_fixed']}")
print(f"  'added' dates filled in:            {stats['added_date']}")
print(f"  Cover links filled in:              {stats['cover_linked']}")
print(f"  Flagged as removed from favorites:  {stats['removed']}")
print(f"  Back in favorites (flag cleared):   {stats['restored']}")
print(f"  Unchanged:                          {stats['untouched']}")
print("\nNext: run  python normalize_tags.py --apply  if any new tags were added.")
