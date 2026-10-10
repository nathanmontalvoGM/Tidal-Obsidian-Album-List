import os
import re

VAULT_PATH = r"I:\My Drive\DriveSyncFiles\Tidal Album Folders\Tidal Albums"
PLAYLISTS_FOLDER = os.path.join(VAULT_PATH, "00 Dashboard", "Playlists")
GENRES_FOLDER = os.path.join(VAULT_PATH, "00 Dashboard", "Genres")

OLD = 't.toLowerCase() === TAG.toLowerCase() || t.toLowerCase() === "#" + TAG.toLowerCase()'
NEW = 'String(t).toLowerCase() === TAG.toLowerCase() || String(t).toLowerCase() === "#" + TAG.toLowerCase()'

fixed = 0

for folder in [PLAYLISTS_FOLDER, GENRES_FOLDER]:
    for filename in os.listdir(folder):
        if not filename.endswith(".md"):
            continue
        filepath = os.path.join(folder, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        if OLD in content:
            new_content = content.replace(OLD, NEW)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Fixed: {filename}")
            fixed += 1

print(f"\nDone. Fixed {fixed} files.")
