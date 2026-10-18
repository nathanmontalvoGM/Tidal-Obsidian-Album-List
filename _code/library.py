"""
Maintenance for the album notes. Everything here except `check` is a dry run unless you add --apply.

    python _code/library.py check                 # health report: duplicates, missing covers/tracklists, unknown tags
    python _code/library.py tags [--apply]        # apply _scripts/tags.json to every album + playlist, sync genre pages
    python _code/library.py retag [--all] [--apply]
                                                  # fill tags from MusicBrainz for untagged albums
                                                  # (--all: also top up albums with fewer than 4 tags)
                                                  # skips albums whose tags you edited on the album page

Tidal import lives in sync_tidal.py. Shared code is in common.py.
"""
import argparse
import json
import os
import re
from collections import Counter, defaultdict

from common import (VAULT, COVERS_FOLDER, GENRES_FOLDER, GENRE_STUB, PLAYLISTS_FOLDER, album_notes,
                    create_genre_page, get_field, get_tags, is_known, musicbrainz_lookup, normalize_list,
                    read_note, resolve_tags, set_tags, tag_key, unquote, write_note)

TAG_LIMIT = 4


def genre_tags(text):
    """An album's tags minus Favorite (that's a tag too, but not a genre)."""
    return [t for t in get_tags(text) if tag_key(t) != "favorite"]


def rel(path):
    return os.path.relpath(path, VAULT)


# ── tags ──────────────────────────────────────────────────
def is_generated_genre_page(text):
    """The one-line stub, or the old generated page that carried its own copy of the code."""
    return text.strip() == GENRE_STUB.strip() or (
        "```dataviewjs" in text and re.search(r'^const TAG = "[^"]*";', text, re.M) is not None)


def cmd_tags(apply):
    removed, renamed, unknown, in_use = Counter(), Counter(), Counter(), Counter()
    notes_changed = 0
    for path, text, crlf in album_notes():
        old = get_tags(text)
        new = normalize_list(old)
        in_use.update(new)
        unknown.update(t for t in old if not is_known(t))
        if old == new:
            continue
        for t in old:
            clean = t.strip("\"'").lstrip("#")
            n = normalize_list([t])
            if not n:
                removed[clean] += 1
            elif n[0] != clean:
                renamed[f"{clean} -> {n[0]}"] += 1
        notes_changed += 1
        write_note(path, set_tags(text, new), crlf, dry_run=not apply)

    playlists_changed = 0
    if os.path.isdir(PLAYLISTS_FOLDER):
        for name in sorted(os.listdir(PLAYLISTS_FOLDER)):
            if not name.endswith(".md"):
                continue
            path = os.path.join(PLAYLISTS_FOLDER, name)
            text, crlf = read_note(path)
            m = re.search(r"const TAGS\s*=\s*(\[[\s\S]*?\]);", text)
            if not m:
                continue
            old = json.loads(m.group(1))
            new = sorted(normalize_list(old), key=str.lower)
            if new == old:
                continue
            playlists_changed += 1
            print(f"  playlist {name}: {len(old)} tags -> {len(new)}")
            text = text[:m.start()] + f"const TAGS = {json.dumps(new)};" + text[m.end():]
            text = re.sub(r"(\*\*Tags:\*\*)[^|\n]*", lambda x: f"{x.group(1)} {', '.join(new)} ", text, count=1)
            write_note(path, text, crlf, dry_run=not apply)

    # Genre pages: one per tag in use. Generated pages for unused tags go; hand-written pages are never touched.
    created, converted, deleted = [], [], []
    os.makedirs(GENRES_FOLDER, exist_ok=True)
    wanted = {t.lower(): t for t in in_use}
    have = {}
    for name in sorted(os.listdir(GENRES_FOLDER)):
        if not name.endswith(".md"):
            continue
        path = os.path.join(GENRES_FOLDER, name)
        text, _ = read_note(path)
        stem = name[:-3]
        if not is_generated_genre_page(text):
            have[stem.lower()] = stem
            continue
        if stem.lower() in wanted and stem.lower() not in have:
            have[stem.lower()] = stem
            if text != GENRE_STUB:
                converted.append(stem)
                write_note(path, GENRE_STUB, dry_run=not apply)
        else:
            deleted.append(stem)
            if apply:
                os.remove(path)
    for low, tag in sorted(wanted.items()):
        if low not in have:
            created.append(tag)
            write_note(os.path.join(GENRES_FOLDER, f"{tag}.md"), GENRE_STUB, dry_run=not apply)

    verb = "changed" if apply else "to change"
    print(f"\nAlbum notes {verb}: {notes_changed}")
    print(f"Playlists {verb}: {playlists_changed}")
    print(f"Genre pages: {len(converted)} converted to the shared page, {len(created)} created, {len(deleted)} removed")
    if created:
        print("  created: " + ", ".join(created))
    if deleted:
        print("  removed (no album uses these tags): " + ", ".join(deleted))
    if renamed:
        print(f"\nMerged/renamed ({sum(renamed.values())}):")
        for k, v in renamed.most_common(25):
            print(f"  {k}  x{v}")
        if len(renamed) > 25:
            print(f"  ... and {len(renamed) - 25} more")
    if removed:
        print(f"\nRemoved as non-genre ({sum(removed.values())}):")
        print("  " + ", ".join(f"{k} x{v}" for k, v in removed.most_common()))
    if unknown:
        print("\nTags not in tags.json (kept as-is; add them to aliases or blocklist):")
        print("  " + ", ".join(f"{k} x{v}" for k, v in unknown.most_common()))
    if not apply:
        print("\nDry run only. Re-run with --apply to make these changes.")


# ── retag ─────────────────────────────────────────────────
def cmd_retag(apply, top_up):
    # Albums whose tags you edited on the album page (tags_edited: true) are never touched.
    todo = [(p, t, c) for p, t, c in album_notes()
            if len(genre_tags(t)) < (TAG_LIMIT if top_up else 1) and get_field(t, "tags_edited") != "true"]
    print(f"{len(todo)} albums to look up on MusicBrainz (about {len(todo) * 2.5 / 60:.0f} min).\n")
    changed = not_found = 0
    for path, text, crlf in todo:
        artist, title = unquote(get_field(text, "artist")), unquote(get_field(text, "title"))
        keep = normalize_list(get_tags(text))
        raw, _, _ = musicbrainz_lookup(artist, title)
        limit = TAG_LIMIT + (len(keep) - len(normalize_list(genre_tags(text))))  # Favorite doesn't use up a slot
        added = resolve_tags(raw, limit, keep=keep) if raw else []
        if not added:
            not_found += 1
            print(f"No tags found: {rel(path)}")
            continue
        changed += 1
        print(f"{rel(path)}: + {', '.join(added)}")
        write_note(path, set_tags(text, keep + added), crlf, dry_run=not apply)
        for tag in added:
            create_genre_page(tag, dry_run=not apply)
    print(f"\nTagged: {changed}   Nothing found: {not_found}")
    if not apply:
        print("Dry run only. Re-run with --apply to write the tags.")


# ── check ─────────────────────────────────────────────────
def cmd_check():
    by_id = defaultdict(list)
    no_cover, broken_cover, no_table, untagged, removed = [], [], [], [], []
    unknown = Counter()
    used_covers = set()
    total = 0
    for path, text, _ in album_notes():
        total += 1
        by_id[str(get_field(text, "tidal_id"))].append(path)
        cover = unquote(get_field(text, "cover"))
        m = re.match(r"\[\[(.+?)(\|.*)?\]\]$", cover or "")
        if not m:
            no_cover.append(path)
        elif not os.path.exists(os.path.join(VAULT, m.group(1))):
            broken_cover.append(f"{rel(path)}  ->  {m.group(1)}")
        else:
            used_covers.add(os.path.basename(m.group(1)))
        if not any(l.startswith("| # |") for l in text.split("\n")):
            no_table.append(path)
        tags = get_tags(text)
        if not genre_tags(text):
            untagged.append(path)
        unknown.update(t for t in tags if not is_known(t))
        if get_field(text, "removed_from_tidal"):
            removed.append(path)

    unused = sorted(f for f in os.listdir(COVERS_FOLDER) if f not in used_covers) if os.path.isdir(COVERS_FOLDER) else []
    dupes = {k: v for k, v in by_id.items() if len(v) > 1}

    def section(title, items, fix=None, show=15):
        mark = "OK " if not items else "!! "
        print(f"{mark}{title}: {len(items)}" + (f"   (fix: {fix})" if items and fix else ""))
        for i in list(items)[:show]:
            print(f"      {i if isinstance(i, str) and not os.path.isabs(i) else rel(i)}")
        if len(items) > show:
            print(f"      ... and {len(items) - show} more")

    print(f"{total} album notes\n")
    section("Same tidal_id in more than one note", [f"{k}: " + " | ".join(rel(p) for p in v) for k, v in dupes.items()],
            "delete the extra note; keep the one with your ratings")
    section("No cover property", no_cover, "python _code/sync_tidal.py")
    section("Cover property points at a missing file", broken_cover)
    section("No tracklist", no_table, "python _code/sync_tidal.py (fills missing ones from Tidal)")
    section("No tags", untagged, "python _code/library.py retag --apply", show=5)
    section("Tags not in tags.json", [f"{k} x{v}" for k, v in unknown.most_common()],
            "add to aliases or blocklist, then library.py tags --apply")
    section("Not in your Tidal favorites anymore (flagged, kept)", removed, show=40)
    section("Cover images no note uses", unused, "safe to delete if you don't want them")


def main():
    ap = argparse.ArgumentParser(description="Music library maintenance.")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("check", help="health report (read-only)")
    p = sub.add_parser("tags", help="apply _scripts/tags.json everywhere and sync genre pages")
    p.add_argument("--apply", action="store_true")
    p = sub.add_parser("retag", help="fill tags from MusicBrainz")
    p.add_argument("--all", action="store_true", help="also top up albums with fewer than 4 tags")
    p.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    if a.cmd == "check":
        cmd_check()
    elif a.cmd == "tags":
        cmd_tags(a.apply)
    else:
        cmd_retag(a.apply, a.all)


if __name__ == "__main__":
    main()
