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