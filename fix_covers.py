"""
Fix missing album covers for artists whose names contain . / : ? etc.

The importer saves covers with a cleaned-up artist name ("Andrew W.K." -> "Andrew W.K"),
but the dashboards looked them up with the raw name from the note. This rewrites every
cover lookup in the vault (genre notes, playlists, Library, Home, _scripts/*.js) to use
findCover(), which tries the cleaned name, the raw name, and the artist folder name.

Run from the vault root:
    python fix_covers.py            # dry run: lists what would change
    python fix_covers.py --apply    # writes the changes
Safe to run more than once; already-fixed files are skipped.
"""
import os
import re
import sys

VAULT = os.path.dirname(os.path.abspath(__file__))
APPLY = "--apply" in sys.argv
SKIP_DIRS = {".git", ".obsidian", "_covers", ".trash"}

HELPER = r'''function findCover(page) {
    const clean = s => String(s || "").replace(/[\\/*?:"<>|]/g, "-").replace(/…/g, "...").replace(/^[. ]+|[. ]+$/g, "");
    const title = page.file.name.replace(/\s\(\d{4}\)$/, "");
    const folder = page.file.folder.split("/").pop();
    for (const artist of [clean(page.artist), page.artist, folder]) {
        const f = app.vault.getAbstractFileByPath(`_covers/${artist} - ${title}.jpg`);
        if (f) return f;
    }
    return null;
}
'''

# (pattern, replacement). Each pattern only fires when the matched code builds a _covers/ path.
RULES = [
    # genre notes, Untagged Albums, templates, playlist.js
    (re.compile(r"^function getCover\(page\) \{$[\s\S]*?^\}$", re.M),
     HELPER + "function getCover(page) { return findCover(page); }"),
    # _tools/Home.md shared helper
    (re.compile(r"^window\._toolsGetCover = function\(page\) \{$[\s\S]*?^\}$", re.M),
     HELPER + "window._toolsGetCover = findCover;"),
    # 00 Dashboard/Library.md
    (re.compile(r"^function coverFor\(page\) \{$[\s\S]*?^\}$", re.M),
     HELPER + "function coverFor(page) {\n    const f = findCover(page);\n    return f ? app.vault.getResourcePath(f) : null;\n}"),
    # _scripts/album.js
    (re.compile(r"^const cover = app\.vault\.getAbstractFileByPath\(`_covers/[^`]*`\);$", re.M),
     HELPER + "const cover = findCover(page);"),
]

# Lines that become dead code once the lookup no longer scans the covers list.
DEAD = [
    re.compile(r'^const coverMap = new Map\(\);\nfor \(let f of app\.vault\.getFiles\(\)\) if \(f\.path\.startsWith\("_covers/"\)\) coverMap\.set\(f\.path, f\);\n', re.M),
    re.compile(r"^const allCovers = app\.vault\.getFiles\(\)\.filter\(f => f\.path\.includes\([\"']_covers[\"']\)\);\n", re.M),
]


def patch(text):
    if "function findCover(" in text:
        return text, 0
    count = 0
    for pattern, replacement in RULES:
        def sub(m):
            nonlocal count
            if "_covers/" not in m.group(0):
                return m.group(0)
            count += 1
            return replacement
        text = pattern.sub(sub, text)
    if count:
        for dead in DEAD:
            name = "coverMap" if "coverMap" in dead.pattern else "allCovers"
            stripped = dead.sub("", text)
            if name not in stripped:
                text = stripped
    return text, count


changed = 0
leftovers = []
for d, dirs, files in os.walk(VAULT):
    dirs[:] = [x for x in dirs if x not in SKIP_DIRS]
    for f in files:
        if not (f.endswith(".md") or f.endswith(".js")):
            continue
        path = os.path.join(d, f)
        rel = os.path.relpath(path, VAULT)
        with open(path, encoding="utf-8") as fh:
            original = fh.read()
        crlf = "\r\n" in original
        text = original.replace("\r\n", "\n")
        new, n = patch(text)
        if n:
            changed += 1
            if changed <= 15:
                print(f"  {'fixed' if APPLY else 'would fix'} ({n}): {rel}")
            if APPLY:
                with open(path, "w", encoding="utf-8", newline="") as fh:
                    fh.write(new.replace("\n", "\r\n") if crlf else new)
        elif "function findCover(" not in text and re.search(r"_covers/\$\{(page\.)?artist\}", text):
            leftovers.append(rel)

if changed > 15:
    print(f"  ... and {changed - 15} more")
print(f"\n{'Fixed' if APPLY else 'Would fix'} {changed} files.")
if leftovers:
    print("Cover lookups this script didn't recognise (fix by hand or ask):")
    for rel in leftovers:
        print(f"  {rel}")
if not APPLY:
    print("\nDry run only. Re-run with --apply to make these changes.")
