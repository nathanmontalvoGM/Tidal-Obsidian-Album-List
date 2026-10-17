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

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SESSION_FILE = os.path.join(SCRIPT_DIR, "tidal_session.json")
MUSICBRAINZ_APP = "ObsidianTidalSync/1.0 (nathanmontalvo1222@gmail.com)"

OVERWRITE = "--overwrite" in sys.argv
if OVERWRITE:
    print("Overwrite mode enabled - existing notes will be replaced!")

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
        response = requests.get(url, params=params, headers=headers, timeout=15)
        response.raise_for_status()
        data = response.json()
        releases = data.get("releases", [])
        if not releases:
            return [], None

        release = releases[0]
        mbid = release.get("id")
        rg_id = release.get("release-group", {}).get("id")

        if not rg_id:
            return [], mbid

        time.sleep(1)
        rg_url = f"https://musicbrainz.org/ws/2/release-group/{rg_id}"
        rg_params = {"fmt": "json", "inc": "tags+genres"}
        rg_response = requests.get(rg_url, params=rg_params, headers=headers, timeout=15)
        rg_response.raise_for_status()
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

        return tags, mbid

    except Exception as e:
        print(f"   MusicBrainz tags error: {e}")
        return [], None

def musicbrainz_get_tracklist(mbid):
    if not mbid:
        return []
    try:
        time.sleep(1)
        url = f"https://musicbrainz.org/ws/2/release/{mbid}"
        params = {"fmt": "json", "inc": "recordings"}
        headers = {"User-Agent": MUSICBRAINZ_APP}
        response = requests.get(url, params=params, headers=headers, timeout=15)
        response.raise_for_status()
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
    resolved = []
    for raw_tag in mb_tags:
        if len(resolved) >= 4:
            break
        if not is_valid_genre_tag(raw_tag):
            print(f"   Skipping tag: {raw_tag}")
            continue
        match = fuzzy_match(raw_tag, existing_tags)
        if match:
            clean = slugify_tag(match)
            if clean and clean not in resolved:
                resolved.append(clean)
        else:
            new_tag = slugify_tag(raw_tag)
            if new_tag and new_tag not in resolved:
                resolved.append(new_tag)
                existing_tags.append(new_tag)
    return resolved[:4]

def create_genre_note(tag):
    os.makedirs(GENRES_FOLDER, exist_ok=True)
    filepath = os.path.join(GENRES_FOLDER, f"{tag}.md")
    if os.path.exists(filepath):
        return

    tag_content_lines = [
        f"# {tag}",
        "",
        "```dataviewjs",
        f'const TAG = "{tag}";',
        "",
        "const allCovers = app.vault.getFiles().filter(f => f.path.includes('_covers'));",
        "",
        "function getCover(page) {",
        "    const albumTitle = page.file.name.replace(/\\s\\(\\d{4}\\)$/, \"\");",
        f"    const expectedPath = `_covers/${{page.artist}} - ${{albumTitle}}.jpg`;",
        "    return allCovers.find(f => f.path === expectedPath);",
        "}",
        "",
        "const pages = dv.pages().where(p =>",
        "    p.tidal_id &&",
        "    p.tags &&",
        "    p.tags.some(t => String(t).toLowerCase() === TAG.toLowerCase() || String(t).toLowerCase() === \"#\" + TAG.toLowerCase())",
        ").sort(p => p.artist);",
        "",
        "dv.container.style.cssText = \"display:flex; flex-wrap:wrap; gap:16px; padding:10px 0;\";",
        "",
        "if (pages.length === 0) {",
        "    const empty = dv.container.createEl(\"div\");",
        "    empty.style.cssText = \"color:#666; font-style:italic; padding:10px;\";",
        "    empty.textContent = \"No albums tagged with \" + TAG + \" yet.\";",
        "} else {",
        "    for (let page of pages) {",
        "        const card = dv.container.createEl(\"div\");",
        "        card.style.cssText = `",
        "            width: 160px;",
        "            background: #1a1a1a;",
        "            border-radius: 10px;",
        "            overflow: hidden;",
        "            cursor: pointer;",
        "            transition: transform 0.2s;",
        "            box-shadow: 0 4px 10px rgba(0,0,0,0.4);",
        "        `;",
        "        card.onmouseenter = () => card.style.transform = \"scale(1.05)\";",
        "        card.onmouseleave = () => card.style.transform = \"scale(1.0)\";",
        "",
        "        const img = card.createEl(\"img\");",
        "        img.style.cssText = \"width:160px; height:160px; object-fit:cover; display:block;\";",
        "        const coverFile = getCover(page);",
        "        if (coverFile) {",
        "            img.src = app.vault.getResourcePath(coverFile);",
        "        } else {",
        "            img.style.cssText += \"background:#333;\";",
        "        }",
        "",
        "        const info = card.createEl(\"div\");",
        "        info.style.cssText = \"padding: 8px 10px;\";",
        "",
        "        const title = info.createEl(\"div\");",
        "        title.style.cssText = \"color:#fff; font-weight:bold; font-size:12px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;\";",
        "        title.textContent = page.title || page.file.name;",
        "",
        "        const artist = info.createEl(\"div\");",
        "        artist.style.cssText = \"color:#aaa; font-size:11px; margin-top:2px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;\";",
        "        artist.textContent = page.artist || \"\";",
        "",
        "        const year = info.createEl(\"div\");",
        "        year.style.cssText = \"color:#666; font-size:10px; margin-top:2px;\";",
        "        year.textContent = page.year || \"\";",
        "",
        "        card.onclick = () => app.workspace.openLinkText(page.file.path, \"\", false);",
        "        dv.container.appendChild(card);",
        "    }",
        "}",
        "```",
    ]
    content = "\n".join(tag_content_lines)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
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
def fix_spaced_tags_in_vault(existing_tags):
    print("\nScanning vault for tags with spaces...")
    fixed_count = 0

    for root, dirs, files in os.walk(ALBUMS_FOLDER):
        dirs[:] = [d for d in dirs if d not in IGNORE_FOLDERS]
        for filename in files:
            if not filename.endswith(".md"):
                continue
            filepath = os.path.join(root, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            # Only process files with tidal_id (album notes)
            if "tidal_id:" not in content:
                continue

            # Find YAML list tags
            yaml_tags = re.findall(r'^\s+-\s+(.+)$', content, re.MULTILINE)
            if not yaml_tags:
                continue

            has_spaced = any(' ' in t.strip() for t in yaml_tags)
            if not has_spaced:
                continue

            # Slugify all tags
            new_tags = []
            for t in yaml_tags:
                t = t.strip()
                slugged = slugify_tag(t)
                if slugged and slugged not in new_tags:
                    new_tags.append(slugged)
                    if slugged not in existing_tags:
                        existing_tags.append(slugged)
                        create_genre_note(slugged)

            # Replace tags block in frontmatter
            new_tags_yaml = "\n" + "\n".join(f"  - {tag}" for tag in new_tags)
            new_content = re.sub(
                r'^tags:(\s*\n(?:\s+-\s+.+\n?)*)',
                f'tags:{new_tags_yaml}\n',
                content,
                flags=re.MULTILINE
            )

            if new_content != content:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"   Fixed tags in: {filename} {yaml_tags} -> {new_tags}")
                fixed_count += 1

    print(f"Fixed spaced tags in {fixed_count} notes.\n")

fix_spaced_tags_in_vault(existing_tags)

def index_notes_by_tidal_id():
    """Map tidal_id -> existing note path, so a renamed artist or a changed
    year on Tidal never produces a second note for the same album."""
    index = {}
    for root, dirs, files in os.walk(ALBUMS_FOLDER):
        dirs[:] = [d for d in dirs if d not in IGNORE_FOLDERS and not d.startswith(".")]
        for filename in files:
            if not filename.endswith(".md"):
                continue
            path = os.path.join(root, filename)
            with open(path, "r", encoding="utf-8") as f:
                head = f.read(2000)
            m = re.search(r'^tidal_id:\s*(\S+)', head, re.MULTILINE)
            if m:
                index.setdefault(m.group(1), path)
    return index

notes_by_id = index_notes_by_tidal_id()
print(f"Indexed {len(notes_by_id)} existing album notes by tidal_id.\n")

notes_created = 0
skipped = 0
overwritten = 0

# ── Sync Tidal -> Obsidian ────────────────────────────────
print("=" * 50)
print("SYNCING: Tidal -> Obsidian")
print("=" * 50)

for album in all_albums:
    artist = sanitize(album.artist.name)
    title = sanitize(album.name)
    year = album.year or "Unknown"
    tidal_id = album.id

    cover_filename = f"{artist} - {title}.jpg"
    cover_filepath = os.path.join(COVERS_FOLDER, cover_filename)
    cover_obsidian_path = f"_covers/{cover_filename}"

    if not os.path.exists(cover_filepath):
        try:
            cover_url = album.image(640)
            response = requests.get(cover_url, timeout=10)
            if response.status_code == 200:
                with open(cover_filepath, "wb") as img_file:
                    img_file.write(response.content)
        except Exception as e:
            print(f"   Could not download cover for {title}: {e}")
            cover_obsidian_path = None

    existing_path = notes_by_id.get(str(tidal_id))
    if existing_path:
        if not OVERWRITE:
            skipped += 1
            continue
        filepath = existing_path  # overwrite the note that already exists, wherever it lives
    else:
        artist_folder = os.path.join(ALBUMS_FOLDER, artist)
        os.makedirs(artist_folder, exist_ok=True)
        filepath = os.path.join(artist_folder, f"{title} ({year}).md")
        notes_by_id[str(tidal_id)] = filepath

    # Preserve existing tags and track ratings if overwriting
    existing_note_tags = []
    existing_track_ratings = {}
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            note_content = f.read()

        tag_match = re.search(r'^tags:\s*(\[.*?\])', note_content, re.MULTILINE)
        if tag_match:
            try:
                existing_note_tags = json.loads(tag_match.group(1))
            except Exception:
                existing_note_tags = []

        if not existing_note_tags:
            yaml_tags = re.findall(r'^\s+-\s+(.+)$', note_content, re.MULTILINE)
            if yaml_tags:
                existing_note_tags = [slugify_tag(t.strip()) for t in yaml_tags]

        for row_match in re.finditer(r'^\|\s*[\d-]+\s*\|\s*(.+?)\s*\|\s*[\d:]*\s*\|\s*([0-9.]+)\s*\|', note_content, re.MULTILINE):
            track_title = row_match.group(1).strip()
            rating = row_match.group(2).strip()
            if rating:
                existing_track_ratings[track_title] = rating

    # ── Fetch from MusicBrainz ────────────────────────────
    print(f"\nProcessing: {album.artist.name} - {album.name}")
    mb_tags_raw, mbid = musicbrainz_get_tags(album.artist.name, album.name)

    if not existing_note_tags:
        if mb_tags_raw:
            resolved = resolve_tags(mb_tags_raw, existing_tags)
            if resolved:
                existing_note_tags = resolved
                print(f"   Tags: {existing_note_tags}")
            else:
                print(f"   No usable tags found on MusicBrainz")
        else:
            print(f"   No tags found on MusicBrainz")

        for tag in existing_note_tags:
            create_genre_note(tag)

    tracks = musicbrainz_get_tracklist(mbid)
    if tracks:
        print(f"   Tracklist: {len(tracks)} tracks")
        for track in tracks:
            if track["title"] in existing_track_ratings:
                track["rating"] = existing_track_ratings[track["title"]]
    else:
        print(f"   No tracklist found on MusicBrainz")

    cover_line = f"![[{cover_obsidian_path}]]" if cover_obsidian_path else ""
    aoty_query = requests.utils.quote(f"{album.artist.name} {album.name}")
    aoty_url = f"https://www.albumoftheyear.org/search/?q={aoty_query}"

    if existing_note_tags:
        tags_yaml = "\n" + "\n".join(f"  - {tag}" for tag in existing_note_tags)
    else:
        tags_yaml = " []"

    tidal_btn_id = rand_id()
    aoty_btn_id = rand_id()

    tracklist_md = ""
    if tracks:
        lines = []
        lines.append("## Tracklist")
        lines.append("")

        # Dataviewjs block to calculate and display overall rating
        lines.append("```dataviewjs")
        lines.append("const page = dv.current();")
        lines.append("const content = await app.vault.read(app.vault.getAbstractFileByPath(page.file.path));")
        lines.append("const rows = content.match(/^\\|\\s*[\\d-]+\\s*\\|.+\\|\\s*([0-9.]+)\\s*\\|$/gm) || [];")
        lines.append("const ratings = rows.map(r => {")
        lines.append("    const cols = r.split('|').map(c => c.trim());")
        lines.append("    return parseFloat(cols[cols.length - 2]);")
        lines.append("}).filter(v => !isNaN(v) && v > 0);")
        lines.append("const el = dv.container.createEl('div');")
        lines.append("el.style.cssText = 'font-size:18px; font-weight:bold; color:#fff; padding:6px 0 12px 0;';")
        lines.append("if (ratings.length > 0) {")
        lines.append("    const avg = (ratings.reduce((a, b) => a + b, 0) / ratings.length).toFixed(1);")
        lines.append("    el.textContent = 'Overall Rating: ' + avg + ' / 10 (' + ratings.length + ' tracks rated)';")
        lines.append("} else {")
        lines.append("    el.style.color = '#666';")
        lines.append("    el.textContent = 'Overall Rating: No tracks rated yet';")
        lines.append("}")
        lines.append("```")
        lines.append("")

        lines.append("| # | Title | Duration | Rating /10 |")
        lines.append("|---|-------|----------|------------|")
        for track in tracks:
            t_title = str(track["title"]).replace("|", "-")
            rating = track.get("rating", "")
            lines.append(f"| {track['num']} | {t_title} | {track['duration']} | {rating} |")
        tracklist_md = "\n".join(lines)

    content = f"""---
title: "{album.name}"
artist: "{album.artist.name}"
year: {year}
tidal_id: {tidal_id}
tags:{tags_yaml}
rating:
---

# {album.name}
**Artist:** {album.artist.name}
**Year:** {year}

{cover_line}
```button
name ▶ Play on Tidal
type link
action tidal://album/{tidal_id}
```
^button-{tidal_btn_id}
```button
name Search on Album of the Year
type link
action {aoty_url}
```
^button-{aoty_btn_id}

{tracklist_md}
"""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    if OVERWRITE:
        overwritten += 1
        print(f"   Overwritten: {artist} - {title}")
    else:
        notes_created += 1
        print(f"   Created: {artist} - {title}")

# ── Summary ───────────────────────────────────────────────
print("\n" + "=" * 50)
print("SYNC COMPLETE")
print("=" * 50)
print(f"  New notes created:          {notes_created}")
print(f"  Existing notes overwritten: {overwritten}")
print(f"  Notes skipped (untouched):  {skipped}")