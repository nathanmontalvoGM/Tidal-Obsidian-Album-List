import os
import re
import requests
import time
from difflib import SequenceMatcher

VAULT_PATH = os.path.dirname(os.path.abspath(__file__))  # vault root
ALBUMS_FOLDER = VAULT_PATH
GENRES_FOLDER = os.path.join(VAULT_PATH, "00 Dashboard", "Genres")
IGNORE_FOLDERS = {"_covers", "_templates", ".obsidian", "00 Dashboard"}
MUSICBRAINZ_APP = "ObsidianTidalSync/1.0 (your@email.com)"
TAG_LIMIT = 4

IGNORE_TAGS = {
    "seen live", "favorites", "favourite", "love", "awesome", "great",
    "beautiful", "amazing", "excellent", "good", "best", "under 2000",
    "party", "inspiring", "charity", "new release", "newrelease",
    "compilations", "compilation", "soundtrack", "reissue", "deluxe",
    "albums i own", "check out", "fun", "epic",
}

def slugify_tag(tag):
    return ''.join(word.capitalize() for word in re.sub(r'[^a-zA-Z0-9 ]', '', tag).split())

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

def get_existing_genre_notes():
    tags = []
    if not os.path.exists(GENRES_FOLDER):
        return tags
    for filename in os.listdir(GENRES_FOLDER):
        if filename.endswith(".md"):
            tags.append(slugify_tag(filename.replace(".md", "")))
    return tags

def is_valid_genre_tag(tag):
    tag_clean = tag.lower().strip()
    if re.match(r'^\d+$', tag_clean):
        return False
    if tag_clean in IGNORE_TAGS:
        return False
    if len(tag_clean) < 3:
        return False
    return True

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
            return []

        release = releases[0]
        rg_id = release.get("release-group", {}).get("id")
        if not rg_id:
            return []

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

        return tags

    except Exception as e:
        print(f"   MusicBrainz error: {e}")
        return []

def create_genre_note(tag):
    """Genre page = one line; _scripts/playlist.js draws it using the note's name as the tag."""
    os.makedirs(GENRES_FOLDER, exist_ok=True)
    filepath = os.path.join(GENRES_FOLDER, f"{tag}.md")
    if os.path.exists(filepath):
        return
    with open(filepath, "w", encoding="utf-8") as f:
        f.write('```dataviewjs\nawait dv.view("_scripts/playlist", { tags: [dv.current().file.name], genre: true });\n```\n')
    print(f"   Created genre note: {tag}.md")

def get_note_tags(content):
    # Try YAML list format
    yaml_tags = re.findall(r'^\s+-\s+(.+)$', content, re.MULTILINE)
    if yaml_tags:
        return [slugify_tag(t.strip()) for t in yaml_tags]
    # Try inline JSON array
    inline_match = re.search(r'^tags:\s*(\[.*?\])', content, re.MULTILINE)
    if inline_match:
        try:
            import json
            tags = json.loads(inline_match.group(1))
            return [slugify_tag(str(t)) for t in tags]
        except Exception:
            pass
    return []

def write_note_tags(content, new_tags):
    new_tags_block = "\n" + "\n".join(f"  - {tag}" for tag in new_tags)
    # Replace YAML list format
    result = re.sub(
        r'^tags:(\s*\n(?:\s+-\s+.+\n?)*)',
        f'tags:{new_tags_block}\n',
        content,
        flags=re.MULTILINE
    )
    if result != content:
        return result
    # Replace inline JSON format
    result = re.sub(
        r'^tags:\s*\[.*?\]',
        f'tags:{new_tags_block}',
        content,
        flags=re.MULTILINE
    )
    return result

# ── Main ──────────────────────────────────────────────────
print("=" * 50)
print("RETAG ALBUMS")
print("=" * 50)
print(f"Scanning vault: {ALBUMS_FOLDER}\n")

known_tags = get_existing_genre_notes()

updated = 0
unchanged = 0
no_mb_tags = 0
total = 0

for root, dirs, files in os.walk(ALBUMS_FOLDER):
    dirs[:] = [d for d in dirs if d not in IGNORE_FOLDERS]
    for filename in files:
        if not filename.endswith(".md"):
            continue

        filepath = os.path.join(root, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        if "tidal_id:" not in content:
            continue

        total += 1

        # Extract artist and title from frontmatter
        artist_match = re.search(r'^artist:\s*"?(.+?)"?\s*$', content, re.MULTILINE)
        title_match = re.search(r'^title:\s*"?(.+?)"?\s*$', content, re.MULTILINE)
        if not artist_match or not title_match:
            continue

        artist = artist_match.group(1).strip()
        title = title_match.group(1).strip()

        existing_tags = get_note_tags(content)
        existing_lower = [t.lower() for t in existing_tags]

        print(f"\n{artist} - {title}")
        if existing_tags:
            print(f"   Existing tags: {existing_tags}")

        # Fetch from MusicBrainz
        mb_tags_raw = musicbrainz_get_tags(artist, title)

        if not mb_tags_raw:
            print(f"   No MusicBrainz tags found")
            no_mb_tags += 1
            unchanged += 1
            continue

        # Resolve new tags to add
        new_tags_to_add = []
        for raw_tag in mb_tags_raw:
            # Stop if we've hit the limit
            if len(existing_tags) + len(new_tags_to_add) >= TAG_LIMIT:
                break
            if not is_valid_genre_tag(raw_tag):
                continue
            # Fuzzy match against known tags first
            match = fuzzy_match(raw_tag, known_tags)
            if match:
                clean = slugify_tag(match)
            else:
                clean = slugify_tag(raw_tag)
                if clean:
                    known_tags.append(clean)

            if not clean:
                continue
            # Skip if already on the note (case-insensitive)
            if clean.lower() in existing_lower:
                print(f"   Skipping duplicate: {clean}")
                continue
            # Skip if already queued to add
            if clean in new_tags_to_add:
                continue
            new_tags_to_add.append(clean)

        if not new_tags_to_add:
            print(f"   No new tags to add")
            unchanged += 1
            continue

        # Merge and write
        merged_tags = existing_tags + new_tags_to_add
        new_content = write_note_tags(content, merged_tags)

        if new_content != content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"   Added tags: {new_tags_to_add}")
            print(f"   Final tags: {merged_tags}")
            for tag in new_tags_to_add:
                create_genre_note(tag)
            updated += 1
        else:
            unchanged += 1

# ── Summary ───────────────────────────────────────────────
print("\n" + "=" * 50)
print("RETAG COMPLETE")
print("=" * 50)
print(f"  Albums processed:      {total}")
print(f"  Albums updated:        {updated}")
print(f"  Albums unchanged:      {unchanged}")
print(f"  No MusicBrainz tags:   {no_mb_tags}")
