"""
Remove duplicate album notes (same tidal_id) and the covers/folders only they used.

Run from the vault root:
    python dedupe_albums.py            # dry run: prints what would change, touches nothing
    python dedupe_albums.py --apply    # actually deletes

Safety: a note in DELETE is only removed if another note with the same tidal_id
exists and is being kept. Covers are only removed if no remaining note uses them.
"""
import os
import re
import sys
from collections import defaultdict

VAULT = os.path.dirname(os.path.abspath(__file__))
APPLY = "--apply" in sys.argv
SKIP_DIRS = {".git", ".obsidian", "_covers", "_templates", "_scripts", "_code", "_tools", "_todo", "00 Dashboard"}

# Reviewed list. Left side is deleted; the comment names the copy that is kept.
DELETE = [
    # Old importer bug turned "." into "..." in names. Keep the clean-name copy.
    "Andrew W...K/I Get Wet (2001).md",                       # keep Andrew W.K/
    "Andrew W...K/You're Not Alone (2018).md",                # keep Andrew W.K/
    "J... Cole/The Fall-Off (2026).md",                       # keep J. Cole/
    "No I...D/From The Private Collection of Saba and No ID (2025).md",  # keep No I.D/
    "Fontaines D...C/Romance (2024).md",                      # keep Fontaines D.C/
    "Megadeth/Peace Sells......... But Who's Buying- (1986).md",
    "Sea Power/The Compleat British Sea Power, Vol... 1- The Decline of British Sea Power (2015).md",
    "Sakanaction/834...194 (2019).md",
    "Common/The Auditorium Vol... 1 (2024).md",
    "Psychedelic Porn Crumpets/High Visceral, Pt... 1 (2016).md",
    "Machine Girl/…Because I’m Young Arrogant and Hate Everything You Stand For (2017).md",

    # Tidal renamed the artist, so the importer made a second folder.
    "TEED/When the Lights Go (2022).md",                      # keep Totally Enormous Extinct Dinosaurs/ (has tracklist)
    "The London Suede/Autofiction (2022).md",                 # keep Suede/ (has cover + extra tag)

    # Tidal changed the year it reports, so the importer made a second file.
    "Maruja/Knocknarea (2026).md",                            # keep 2023 (original release)
    "Fellowship/The Saberlight Chronicles (2026).md",         # keep 2022 (original release)
    "Bring Me The Horizon/Count Your Blessings - Repented (2006).md",  # keep 2026 (the 2026 re-recording)

    # Renamed copies without the year; the importer's own filename is kept.
    "Rammstein/Sehnsucht.md",                                 # keep Sehnsucht (Remastered 2023) (1998).md
    "Rammstein/Herzeleid.md",                                 # keep Herzeleid (Remastered 2020) (1996).md
]


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def album_info(path):
    text = read(path)
    fm = re.match(r"^---\n(.*?)\n---", text.replace("\r\n", "\n"), re.S)
    if not fm:
        return None
    tid = re.search(r"^tidal_id:\s*(\S+)", fm.group(1), re.M)
    if not tid:
        return None
    artist = re.search(r"^artist:\s*\"?(.*?)\"?\s*$", fm.group(1), re.M)
    return {"tid": tid.group(1), "artist": artist.group(1) if artist else "", "text": text}


def covers_used(rel_path, info):
    used = set(re.findall(r"!\[\[(_covers/[^\]|]+)", info["text"]))
    base = re.sub(r"\s\(\d{4}\)$", "", os.path.splitext(os.path.basename(rel_path))[0])
    used.add(f"_covers/{info['artist']} - {base}.jpg")
    return used


# Index every album note in the vault.
notes = {}
for d, dirs, files in os.walk(VAULT):
    dirs[:] = [x for x in dirs if x not in SKIP_DIRS]
    for f in files:
        if f.endswith(".md"):
            full = os.path.join(d, f)
            info = album_info(full)
            if info:
                notes[os.path.relpath(full, VAULT).replace("\\", "/")] = info

by_tid = defaultdict(list)
for rel, info in notes.items():
    by_tid[info["tid"]].append(rel)

to_delete = []
for rel in DELETE:
    if rel not in notes:
        print(f"  already gone: {rel}")
        continue
    keepers = [r for r in by_tid[notes[rel]["tid"]] if r != rel and r not in DELETE]
    if not keepers:
        print(f"  SKIPPED (no other copy would remain): {rel}")
        continue
    to_delete.append(rel)
    print(f"  delete: {rel}\n          keep: {keepers[0]}")

kept = {r: i for r, i in notes.items() if r not in to_delete}
still_used = set().union(*(covers_used(r, i) for r, i in kept.items())) if kept else set()
dead_covers = sorted(
    c for rel in to_delete for c in covers_used(rel, notes[rel])
    if c not in still_used and os.path.exists(os.path.join(VAULT, c))
)
for c in dead_covers:
    print(f"  delete cover: {c}")

if APPLY:
    for rel in to_delete:
        os.remove(os.path.join(VAULT, rel))
    for c in dead_covers:
        os.remove(os.path.join(VAULT, c))
    for rel in to_delete:
        folder = os.path.dirname(os.path.join(VAULT, rel))
        if os.path.isdir(folder) and not os.listdir(folder):
            os.rmdir(folder)
            print(f"  removed empty folder: {os.path.relpath(folder, VAULT)}")

remaining = {t: rs for t, rs in by_tid.items() if len([r for r in rs if r not in to_delete]) > 1}
print(f"\n{'Deleted' if APPLY else 'Would delete'} {len(to_delete)} notes and {len(dead_covers)} covers.")
if remaining:
    print("Duplicates NOT handled by this script (review by hand):")
    for t, rs in remaining.items():
        print(f"  tidal_id {t}: " + " | ".join(r for r in rs if r not in to_delete))
else:
    print("No other duplicate tidal_ids in the vault.")
if not APPLY:
    print("\nDry run only. Re-run with --apply to make these changes.")
