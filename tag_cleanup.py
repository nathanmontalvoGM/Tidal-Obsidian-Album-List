import os
import re
import json

VAULT_PATH = os.path.dirname(os.path.abspath(__file__))  # vault root
ALBUMS_FOLDER = VAULT_PATH
GENRES_FOLDER = os.path.join(VAULT_PATH, "00 Dashboard", "Genres")
IGNORE_FOLDERS = {"_covers", "_templates", ".obsidian", "00 Dashboard"}

def slugify_tag(tag):
    return ''.join(word.capitalize() for word in re.sub(r'[^a-zA-Z0-9 ]', '', tag).split())

def create_genre_note(tag):
    """Genre page = one line; _scripts/playlist.js draws it using the note's name as the tag."""
    os.makedirs(GENRES_FOLDER, exist_ok=True)
    filepath = os.path.join(GENRES_FOLDER, f"{tag}.md")
    if os.path.exists(filepath):
        return
    with open(filepath, "w", encoding="utf-8") as f:
        f.write('```dataviewjs\nawait dv.view("_scripts/playlist", { tags: [dv.current().file.name], genre: true });\n```\n')
    print(f"   Created genre note: {tag}.md")

# ── Scan and fix ──────────────────────────────────────────
print("=" * 50)
print("TAG CLEANUP")
print("=" * 50)
print(f"Scanning: {ALBUMS_FOLDER}\n")

fixed_files = 0
fixed_tags = 0
skipped_files = 0
all_tags_seen = set()

for root, dirs, files in os.walk(ALBUMS_FOLDER):
    dirs[:] = [d for d in dirs if d not in IGNORE_FOLDERS]
    for filename in files:
        if not filename.endswith(".md"):
            continue

        filepath = os.path.join(root, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        if "tidal_id:" not in content:
            skipped_files += 1
            continue

        # Try YAML list format first
        yaml_tags = re.findall(r'^\s+-\s+(.+)$', content, re.MULTILINE)

        # Try inline JSON array format
        inline_match = re.search(r'^tags:\s*(\[.*?\])', content, re.MULTILINE)
        inline_tags = []
        if inline_match:
            try:
                inline_tags = json.loads(inline_match.group(1))
            except Exception:
                inline_tags = []

        tags = yaml_tags if yaml_tags else inline_tags
        if not tags:
            skipped_files += 1
            continue

        # Check if any tag has a space
        has_spaced = any(' ' in str(t).strip() for t in tags)
        if not has_spaced:
            skipped_files += 1
            continue

        # Slugify all tags
        new_tags = []
        changed = []
        for t in tags:
            t = str(t).strip()
            slugged = slugify_tag(t)
            if not slugged:
                continue
            if slugged not in new_tags:
                new_tags.append(slugged)
                all_tags_seen.add(slugged)
            if ' ' in t:
                changed.append(f"'{t}' -> '{slugged}'")
                fixed_tags += 1

        if not changed:
            skipped_files += 1
            continue

        # Replace tags block in frontmatter — handle both formats
        new_tags_block = "\n" + "\n".join(f"  - {tag}" for tag in new_tags)

        if yaml_tags:
            new_content = re.sub(
                r'^tags:(\s*\n(?:\s+-\s+.+\n?)*)',
                f'tags:{new_tags_block}\n',
                content,
                flags=re.MULTILINE
            )
        else:
            new_content = re.sub(
                r'^tags:\s*\[.*?\]',
                f'tags:{new_tags_block}',
                content,
                flags=re.MULTILINE
            )

        if new_content != content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Fixed: {filename}")
            for c in changed:
                print(f"   {c}")
            fixed_files += 1

# ── Create any missing genre notes ───────────────────────
print(f"\nChecking genre notes for {len(all_tags_seen)} unique tags...")
for tag in sorted(all_tags_seen):
    create_genre_note(tag)

# ── Summary ───────────────────────────────────────────────
print("\n" + "=" * 50)
print("CLEANUP COMPLETE")
print("=" * 50)
print(f"  Files fixed:        {fixed_files}")
print(f"  Tags slugified:     {fixed_tags}")
print(f"  Files skipped:      {skipped_files}")
print(f"  Genre notes synced: {len(all_tags_seen)}")
