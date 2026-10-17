import os

GENRES_FOLDER = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "00 Dashboard", "Playlists")

genres = []
for filename in os.listdir(GENRES_FOLDER):
    if filename.endswith(".md"):
        name = filename.replace(".md", "")
        genres.append(name)

genres.sort()

print(f"Found {len(genres)} genre notes:\n")
for genre in genres:
    print(f"  - {genre}")