import os

VAULT_PATH = os.path.dirname(os.path.abspath(__file__))  # vault root
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
    """Genre page = one line; _scripts/playlist.js draws it using the note's name as the tag."""
    os.makedirs(GENRES_FOLDER, exist_ok=True)
    filepath = os.path.join(GENRES_FOLDER, f"{tag}.md")
    if os.path.exists(filepath):
        return
    with open(filepath, "w", encoding="utf-8") as f:
        f.write('```dataviewjs\nawait dv.view("_scripts/playlist", { tags: [dv.current().file.name], genre: true });\n```\n')
    print(f"   Created genre note: {tag}.md")

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