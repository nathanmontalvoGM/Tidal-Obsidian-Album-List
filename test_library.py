import tidalapi
import json

SESSION_FILE = "tidal_session.json"

session = tidalapi.Session()

# Load saved session
try:
    with open(SESSION_FILE, "r") as f:
        data = json.load(f)
    loaded = session.load_oauth_session(
        data["token_type"],
        data["access_token"],
        data["refresh_token"],
        data["expiry_time"]
    )
    if loaded:
        print(f"Resumed session: {session.user.name}")
    else:
        raise Exception("Session expired")
except Exception:
    session.login_oauth_simple()

# Fetch your albums
favorites = tidalapi.Favorites(session, session.user.id)
albums = favorites.albums()

print(f"\nFound {len(albums)} albums\n")

for album in albums[:10]:  # First 10 only
    print(f"Title:  {album.name}")
    print(f"Artist: {album.artist.name}")
    print(f"Year:   {album.year}")
    print(f"ID:     {album.id}")
    print("---")