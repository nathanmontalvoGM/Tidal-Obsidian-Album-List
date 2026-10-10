import os

VAULT_PATH = r"I:\My Drive\DriveSyncFiles\Tidal Album Folders\Tidal Albums"
GENRES_FOLDER = os.path.join(VAULT_PATH, "00 Dashboard", "Genres")

DELETED_TAGS = [
    "GlitchPop", "Wsum917FmMadison", "PostBritPop", "JazzRap", "DoomMEtal",
    "VideoGameMusic", "ContemporaryCountry", "EDM", "PowerPop", "BestOf2019",
    "CountryFolk", "BrutalDeathcore", "AlternativeRock", "PowerMetal", "SpaceRock",
    "MathRock", "BlackenedDeathcore", "ProgressiveMetal", "IndustrialRock", "PostPunk",
    "ThrashMetal", "DancePop", "AlternativeCountry", "PostPunkRevival", "NeoclassicalDjent",
    "DeathDoomMetal", "SymphonicMetal", "BestOf2022", "NuMetal", "MelodicDeathMetal",
    "ConceptAlbum", "ExperimentalRock", "SymphonicDeathcore", "SkaPunk", "HardcoreHipHop",
    "MidwestEmo", "BlackMetal", "ExperimentalMetal", "HipHop", "PopRock",
    "ProgDeathMetal", "AtmosphericMetal", "IndustrialMetal", "CountryRock", "PostHardcore",
    "TechnicalDeathMetal", "BrutalDeathMetal", "AltPop", "IndieRock", "MathMetal",
    "AlternativeRandB", "PsychedelicRock", "MathCore", "BestAlbums2025", "SoftRock",
    "NewWave", "IndieFolk", "IndiePop", "FolkPop", "FolkRock", "GrooveMetal",
    "NoiseRock", "ProgressivePop", "ConsciousHipHop", "PostRock", "HardRock",
    "ChamberPop", "TechnicalDeathcore", "GlamRock", "HeavyMetal", "AvantGardeMetal",
    "EastCoastHipHop", "AlternativeMetal", "AlternativeDance", "PopRap", "DeathCore",
    "PsychedelicPop"
]

def create_genre_note(tag):
    os.makedirs(GENRES_FOLDER, exist_ok=True)
    filepath = os.path.join(GENRES_FOLDER, f"{tag}.md")
    if os.path.exists(filepath):
        return False

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
    return True

print("=" * 50)
print("RESTORING DELETED GENRE NOTES")
print("=" * 50)

created = 0
skipped = 0
for tag in DELETED_TAGS:
    if create_genre_note(tag):
        print(f"  Restored: {tag}.md")
        created += 1
    else:
        print(f"  Already exists: {tag}.md")
        skipped += 1

print("\n" + "=" * 50)
print("COMPLETE")
print("=" * 50)
print(f"  Restored: {created}")
print(f"  Skipped:  {skipped}")