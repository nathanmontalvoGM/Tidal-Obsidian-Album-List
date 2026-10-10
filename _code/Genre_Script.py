import os

GENRES_FOLDER = r"I:\My Drive\DriveSyncFiles\Tidal Album Folders\Tidal Albums\00 Dashboard\Playlists"

genres = []
for filename in os.listdir(GENRES_FOLDER):
    if filename.endswith(".md"):
        name = filename.replace(".md", "")
        genres.append(name)

genres.sort()

print(f"Found {len(genres)} genre notes:\n")
for genre in genres:
    print(f"  - {genre}")