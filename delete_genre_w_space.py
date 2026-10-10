import os
import re

VAULT_PATH = r"I:\My Drive\DriveSyncFiles\Tidal Album Folders\Tidal Albums"
GENRES_FOLDER = os.path.join(VAULT_PATH, "00 Dashboard", "Genres")

print("=" * 50)
print("GENRE NOTE CLEANUP")
print("=" * 50)
print(f"Scanning: {GENRES_FOLDER}\n")

deleted = 0
kept = 0

for filename in os.listdir(GENRES_FOLDER):
    if not filename.endswith(".md"):
        continue

    tag_name = filename.replace(".md", "")

    if ' ' in tag_name:
        filepath = os.path.join(GENRES_FOLDER, filename)
        os.remove(filepath)
        print(f"Deleted: {filename}")
        deleted += 1
    else:
        kept += 1

print("\n" + "=" * 50)
print("COMPLETE")
print("=" * 50)
print(f"  Deleted: {deleted}")
print(f"  Kept:    {kept}")
