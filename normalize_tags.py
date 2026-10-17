"""
Apply the tag rules in _scripts/tags.json to every album note and tag playlist.

- Merges spelling variants and synonyms into one tag ("Numetal" -> "NuMetal", "Rap" -> "HipHop")
- Removes blocklisted non-genre tags ("Clonehero", "Bestof2019", ...)
- Fixes the TAGS list in playlist notes the same way

Run from the vault root:
    python normalize_tags.py            # dry run: prints what would change
    python normalize_tags.py --apply    # writes the changes
Safe to re-run any time, e.g. after editing tags.json.
"""
import os
import re
import sys
import json
from collections import Counter

from tag_rules import normalize_list, is_known, tag_key

VAULT = os.path.dirname(os.path.abspath(__file__))
APPLY = "--apply" in sys.argv
SKIP_DIRS = {".git", ".obsidian", "_covers", "_templates", "_scripts", "_code", "_tools", "_todo", "00 Dashboard", ".trash"}
PLAYLISTS = os.path.join(VAULT, "00 Dashboard", "Playlists")

FM_RE = re.compile(r"^---\n(.*?)\n---", re.S)
TAG_BLOCK_RE = re.compile(r"^tags:[ \t]*(\[[^\]\n]*\])?[ \t]*\n((?:[ \t]+-[^\n]*\n)*)", re.M)


def read(path):
    with open(path, encoding="utf-8") as f:
        raw = f.read()
    return raw, "\r\n" in raw


def write(path, text, crlf):
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text.replace("\n", "\r\n") if crlf else text)


def parse_tags(block_match):
    inline, listed = block_match.group(1), block_match.group(2)
    if inline:
        return [t.strip() for t in inline.strip("[]").split(",") if t.strip()]
    return [re.sub(r"^[ \t]+-[ \t]*", "", line).strip() for line in listed.splitlines() if line.strip()]


def render_tags(tags):
    return "tags: []\n" if not tags else "tags:\n" + "".join(f"  - {t}\n" for t in tags)


removed, renamed, unknown = Counter(), Counter(), Counter()
notes_changed = 0

for d, dirs, files in os.walk(VAULT):
    dirs[:] = [x for x in dirs if x not in SKIP_DIRS]
    for name in files:
        if not name.endswith(".md"):
            continue
        path = os.path.join(d, name)
        raw, crlf = read(path)
        text = raw.replace("\r\n", "\n")
        fm = FM_RE.match(text)
        if not fm or not re.search(r"^tidal_id:", fm.group(1), re.M):
            continue
        fm_body = fm.group(1) + "\n"
        block = TAG_BLOCK_RE.search(fm_body)
        if not block:
            continue
        old = parse_tags(block)
        new = normalize_list(old)
        for t in old:
            if not is_known(t):
                unknown[t] += 1
        if old == new:
            continue
        for t in old:
            clean = t.strip('"\'').lstrip("#")
            if not normalize_list([t]):
                removed[clean] += 1
            elif normalize_list([t])[0] != clean:
                renamed[f"{clean} -> {normalize_list([t])[0]}"] += 1
        notes_changed += 1
        new_fm = fm_body[:block.start()] + render_tags(new) + fm_body[block.end():]
        new_text = "---\n" + new_fm.rstrip("\n") + "\n---" + text[fm.end():]
        if APPLY:
            write(path, new_text, crlf)

playlists_changed = 0
if os.path.isdir(PLAYLISTS):
    for name in sorted(os.listdir(PLAYLISTS)):
        if not name.endswith(".md"):
            continue
        path = os.path.join(PLAYLISTS, name)
        raw, crlf = read(path)
        text = raw.replace("\r\n", "\n")
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
        if APPLY:
            write(path, text, crlf)

print(f"\nAlbum notes {'changed' if APPLY else 'to change'}: {notes_changed}")
print(f"Playlists {'changed' if APPLY else 'to change'}: {playlists_changed}")
print(f"\nMerged/renamed ({sum(renamed.values())}):")
for k, v in renamed.most_common(25):
    print(f"  {k}  x{v}")
if len(renamed) > 25:
    print(f"  ... and {len(renamed) - 25} more")
print(f"\nRemoved as non-genre ({sum(removed.values())}):")
print("  " + ", ".join(f"{k} x{v}" for k, v in removed.most_common()))
if unknown:
    print("\nTags not in tags.json (kept as-is; add them to aliases or blocklist):")
    print("  " + ", ".join(f"{k} x{v}" for k, v in unknown.most_common()))
if not APPLY:
    print("\nDry run only. Re-run with --apply to make these changes.")
