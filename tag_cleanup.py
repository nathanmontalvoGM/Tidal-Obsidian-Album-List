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
        "    const clean = s => String(s || \"\").replace(/[\\\\/*?:\"<>|]/g, \"-\").replace(/…/g, \"...\").replace(/^[. ]+|[. ]+$/g, \"\");",
        "    const title = page.file.name.replace(/\\s\\(\\d{4}\\)$/, \"\");",
        "    const folder = page.file.folder.split(\"/\").pop();",
        "    for (const artist of [clean(page.artist), page.artist, folder]) {",
        "        const f = app.vault.getAbstractFileByPath(`_covers/${artist} - ${title}.jpg`);",
        "        if (f) return f;",
        "    }",
        "    return null;",
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
