import os
import re
import time
import json
from difflib import SequenceMatcher
import aoty

VAULT_PATH = os.path.dirname(os.path.abspath(__file__))  # vault root
ALBUMS_FOLDER = VAULT_PATH
GENRES_FOLDER = os.path.join(VAULT_PATH, "00 Dashboard", "Genres")
IGNORE_FOLDERS = {"_covers", "_templates", ".obsidian", "00 Dashboard"}
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

def is_valid_genre_tag(tag):
    tag_clean = tag.lower().strip()
    if re.match(r'^\d+$', tag_clean):
        return False
    if tag_clean in IGNORE_TAGS:
        return False
    if len(tag_clean) < 3:
        return False
    return True

def get_existing_genre_notes():
    tags = []
    if not os.path.exists(GENRES_FOLDER):
        return tags
    for filename in os.listdir(GENRES_FOLDER):
        if filename.endswith(".md"):
            tags.append(slugify_tag(filename.replace(".md", "")))
    return tags

def get_note_tags(content):
    yaml_tags = re.findall(r'^\s+-\s+(.+)$', content, re.MULTILINE)
    if yaml_tags:
        return [slugify_tag(t.strip()) for t in yaml_tags]
    inline_match = re.search(r'^tags:\s*(\[.*?\])', content, re.MULTILINE)
    if inline_match:
        try:
            tags = json.loads(inline_match.group(1))
            return [slugify_tag(str(t)) for t in tags if str(t).strip()]
        except Exception:
            pass
    return []

def write_note_tags(content, new_tags):
    new_tags_block = "\n" + "\n".join(f"  - {tag}" for tag in new_tags)
    result = re.sub(
        r'^tags:(\s*\n(?:\s+-\s+.+\n?)*)',
        f'tags:{new_tags_block}\n',
        content,
        flags=re.MULTILINE
    )
    if result != content:
        return result
    result = re.sub(
        r'^tags:\s*\[.*?\]',
        f'tags:{new_tags_block}',
        content,
        flags=re.MULTILINE
    )
    result = re.sub(
        r'^tags:\s*$',
        f'tags:{new_tags_block}',
        result,
        flags=re.MULTILINE
    )
    return result

def create_genre_note(tag):
    """Genre page = one line; _scripts/playlist.js draws it using the note's name as the tag."""
    os.makedirs(GENRES_FOLDER, exist_ok=True)
    filepath = os.path.join(GENRES_FOLDER, f"{tag}.md")
    if os.path.exists(filepath):
        return
    with open(filepath, "w", encoding="utf-8") as f:
        f.write('```dataviewjs\nawait dv.view("_scripts/playlist", { tags: [dv.current().file.name], genre: true });\n```\n')
    print(f"   Created genre note: {tag}.md")
from albumoftheyearapi import AOTY

def get_aoty_tags(client, artist, title):
    try:
        # Search for the album
        results = client.search_albums(f"{artist} {title}")
        if not results:
            return []

        print(f"   Search results: {results}")

        # Take first result — it returns album IDs/slugs
        first = results[0] if isinstance(results, list) else None
        if not first:
            return []

        # Get genres for that album
        genres = client.album_genres(first)
        if not genres:
            return []

        print(f"   AOTY genres: {genres}")
        return genres if isinstance(genres, list) else []

    except Exception as e:
        print(f"   AOTY error: {e}")
        return []

# ── Main ──────────────────────────────────────────────────
print("=" * 50)
print("AOTY TAG FETCH")
print("=" * 50)
print(f"Scanning for untagged albums in: {ALBUMS_FOLDER}\n")

# Init AOTY client
client = aoty.Client()

known_tags = get_existing_genre_notes()

updated = 0
skipped_has_tags = 0
skipped_no_result = 0
total_untagged = 0

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

        existing_tags = get_note_tags(content)
        if existing_tags:
            skipped_has_tags += 1
            continue

        total_untagged += 1

        artist_match = re.search(r'^artist:\s*"?(.+?)"?\s*$', content, re.MULTILINE)
        title_match = re.search(r'^title:\s*"?(.+?)"?\s*$', content, re.MULTILINE)
        if not artist_match or not title_match:
            continue

        artist = artist_match.group(1).strip()
        title = title_match.group(1).strip()

        print(f"\n{artist} - {title}")

        raw_tags = get_aoty_tags(client, artist, title)
        if not raw_tags:
            print(f"   No tags found on AOTY")
            skipped_no_result += 1
            continue

        resolved = []
        for raw_tag in raw_tags:
            if len(resolved) >= TAG_LIMIT:
                break
            if not is_valid_genre_tag(raw_tag):
                print(f"   Skipping: {raw_tag}")
                continue
            match = fuzzy_match(raw_tag, known_tags)
            if match:
                clean = slugify_tag(match)
            else:
                clean = slugify_tag(raw_tag)
                if clean:
                    known_tags.append(clean)
            if clean and clean not in resolved:
                resolved.append(clean)

        if not resolved:
            print(f"   No usable tags after filtering")
            skipped_no_result += 1
            continue

        new_content = write_note_tags(content, resolved)
        if new_content != content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"   Tagged: {resolved}")
            for tag in resolved:
                create_genre_note(tag)
            updated += 1

        time.sleep(1)

# ── Summary ───────────────────────────────────────────────
print("\n" + "=" * 50)
print("AOTY TAG COMPLETE")
print("=" * 50)
print(f"  Untagged albums found:   {total_untagged}")
print(f"  Albums tagged:           {updated}")
print(f"  No AOTY result:          {skipped_no_result}")
print(f"  Skipped (had tags):      {skipped_has_tags}")