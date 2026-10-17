"""
Shared code for the music library scripts (sync_tidal.py, library.py).

Everything that more than one script needs lives here once: vault paths, tag rules
(from _scripts/tags.json), reading/editing album notes, and MusicBrainz lookups.
"""
import json
import os
import re
import time
from difflib import SequenceMatcher

# ── Paths ─────────────────────────────────────────────────
CODE_DIR = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.dirname(CODE_DIR)  # _code/ sits in the vault root
COVERS_FOLDER = os.path.join(VAULT, "_covers")
GENRES_FOLDER = os.path.join(VAULT, "00 Dashboard", "Genres")
PLAYLISTS_FOLDER = os.path.join(VAULT, "00 Dashboard", "Playlists")
TAGS_JSON = os.path.join(VAULT, "_scripts", "tags.json")
SESSION_FILE = os.path.join(VAULT, "tidal_session.json")  # Tidal login; never committed (.gitignore)
SKIP_DIRS = {"_covers", "_templates", "_scripts", "_code", "_tools", "_todo", "00 Dashboard"}

GENRE_STUB = '```dataviewjs\nawait dv.view("_scripts/playlist", { tags: [dv.current().file.name], genre: true });\n```\n'
ALBUM_STUB = '```dataviewjs\nawait dv.view("_scripts/album");\n```\n'
MUSICBRAINZ_APP = "ObsidianTidalSync/1.0 (nathanmontalvo1222@gmail.com)"


# ── Names ─────────────────────────────────────────────────
def sanitize(name):
    """Make a name safe for a Windows filename (same rule the covers were saved with)."""
    name = re.sub(r'[\\/*?:"<>|]', "-", str(name))
    name = name.replace("…", "...")
    return name.strip(". ")


def slugify_tag(tag):
    return "".join(word.capitalize() for word in re.sub(r"[^a-zA-Z0-9 ]", "", tag).split())


def fuzzy_match(tag, candidates, threshold=0.82):
    key = tag.lower().replace(" ", "").replace("-", "")
    best, best_ratio = None, 0
    for c in candidates:
        ratio = SequenceMatcher(None, key, c.lower().replace(" ", "").replace("-", "")).ratio()
        if ratio > best_ratio:
            best, best_ratio = c, ratio
    return best if best_ratio >= threshold else None


# ── Tag rules (_scripts/tags.json) ────────────────────────
with open(TAGS_JSON, encoding="utf-8") as _f:
    _rules = json.load(_f)
ALIASES = _rules["aliases"]
BLOCKLIST = set(_rules["blocklist"])
CANONICAL = sorted(set(ALIASES.values()))

# Crowd tags from MusicBrainz / AOTY that are opinions, not genres
NOT_GENRES = {
    "seen live", "favorites", "favourite", "love", "awesome", "great", "beautiful", "amazing",
    "excellent", "good", "best", "under 2000", "party", "inspiring", "charity", "new release",
    "newrelease", "compilations", "compilation", "soundtrack", "reissue", "deluxe",
    "albums i own", "check out", "fun", "epic",
}


def tag_key(tag):
    """'Nu-Metal', 'nu metal', '#Numetal' -> 'numetal'."""
    return re.sub(r"[^a-z0-9]", "", str(tag).strip().strip("\"'").lstrip("#").lower())


def normalize_tag(tag):
    """Canonical tag; None if blocklisted, empty, or a bare year/decade;
    otherwise the cleaned original (a tag tags.json doesn't know yet)."""
    k = tag_key(tag)
    if not k or k in BLOCKLIST or re.fullmatch(r"\d+s?", k):
        return None
    if k in ALIASES:
        return ALIASES[k]
    cleaned = str(tag).strip().strip("\"'").lstrip("#")
    return cleaned[:1].upper() + cleaned[1:]


def is_known(tag):
    k = tag_key(tag)
    return k in ALIASES or k in BLOCKLIST or bool(re.fullmatch(r"\d+s?", k))


def normalize_list(tags):
    out = []
    for t in tags:
        n = normalize_tag(t)
        if n and n not in out:
            out.append(n)
    return out


def resolve_tags(raw_tags, limit=4, keep=()):
    """Tags from MusicBrainz/AOTY -> up to `limit` canonical tags (counting `keep`, the
    tags the album already has)."""
    resolved = list(keep)
    for raw in raw_tags:
        if len(resolved) >= limit:
            break
        if raw.lower().strip() in NOT_GENRES or len(raw.strip()) < 3:
            continue
        if is_known(raw):
            tag = normalize_tag(raw)
        else:
            tag = fuzzy_match(raw, CANONICAL) or normalize_tag(slugify_tag(raw))
            if tag and tag not in CANONICAL:
                print(f"   New tag (add it to _scripts/tags.json if it's a keeper): {tag}")
        if tag and tag not in resolved:
            resolved.append(tag)
    return resolved[len(keep):]


# ── Reading and editing notes ─────────────────────────────
def read_note(path):
    with open(path, encoding="utf-8") as f:
        raw = f.read()
    return raw.replace("\r\n", "\n"), "\r\n" in raw


def write_note(path, text, crlf=False, dry_run=False):
    if dry_run:
        return
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text.replace("\n", "\r\n") if crlf else text)


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    return m.group(1) if m else None


def get_field(text, key):
    fm = frontmatter(text)
    if fm is None:
        return None
    f = re.search(rf"^{re.escape(key)}:[ \t]*(.*)$", fm, re.M)
    return f.group(1).strip() if f else None


def set_field(text, key, value):
    """Set (or with value=None remove) one property, leaving everything else as is."""
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return text
    fm = m.group(1)
    line = re.compile(rf"^{re.escape(key)}:[^\n]*\n?", re.M)
    if value is None:
        fm = line.sub("", fm).rstrip("\n")
    elif line.search(fm + "\n"):
        fm = line.sub(f"{key}: {value}\n", fm + "\n", count=1).rstrip("\n")
    elif re.search(r"^tags:", fm, re.M):
        fm = re.sub(r"^tags:", f"{key}: {value}\ntags:", fm, count=1, flags=re.M)
    else:
        fm = fm + f"\n{key}: {value}"
    return "---\n" + fm + "\n---" + text[m.end():]


TAG_BLOCK_RE = re.compile(r"^tags:[ \t]*(\[[^\]\n]*\])?[ \t]*\n((?:[ \t]+-[^\n]*\n)*)", re.M)


def get_tags(text):
    fm = frontmatter(text)
    block = TAG_BLOCK_RE.search(fm + "\n") if fm is not None else None
    if not block:
        return []
    if block.group(1):
        return [t.strip() for t in block.group(1).strip("[]").split(",") if t.strip()]
    return [re.sub(r"^[ \t]+-[ \t]*", "", l).strip() for l in block.group(2).splitlines() if l.strip()]


def set_tags(text, tags):
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return text
    fm = m.group(1) + "\n"
    rendered = "tags: []\n" if not tags else "tags:\n" + "".join(f"  - {t}\n" for t in tags)
    block = TAG_BLOCK_RE.search(fm)
    fm = fm[:block.start()] + rendered + fm[block.end():] if block else fm + rendered
    return "---\n" + fm.rstrip("\n") + "\n---" + text[m.end():]


def album_notes():
    """Yield (path, text, crlf) for every album note (any note with a tidal_id)."""
    for root, dirs, files in os.walk(VAULT):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS and not d.startswith("."))
        for name in sorted(files):
            if not name.endswith(".md"):
                continue
            path = os.path.join(root, name)
            text, crlf = read_note(path)
            fm = frontmatter(text)
            if fm and re.search(r"^tidal_id:", fm, re.M):
                yield path, text, crlf


def unquote(value):
    v = (value or "").strip()
    if len(v) >= 2 and v[0] == v[-1] == '"':
        try:
            return json.loads(v)
        except ValueError:
            return v[1:-1]
    return v


def create_genre_page(tag, dry_run=False):
    os.makedirs(GENRES_FOLDER, exist_ok=True)
    if dry_run or any(f.lower() == f"{tag}.md".lower() for f in os.listdir(GENRES_FOLDER)):
        return
    path = os.path.join(GENRES_FOLDER, f"{tag}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(GENRE_STUB)
    print(f"   Created genre page: {tag}")


# ── MusicBrainz ───────────────────────────────────────────
_last_mb_request = 0.0


def mb_get(url, params):
    """GET from MusicBrainz at no more than ~1 request/second, retrying when it
    answers 503 (its "slow down" response) instead of losing the lookup."""
    import requests
    global _last_mb_request
    for attempt in range(5):
        wait = 1.1 - (time.time() - _last_mb_request)
        if wait > 0:
            time.sleep(wait)
        _last_mb_request = time.time()
        response = requests.get(url, params=params, headers={"User-Agent": MUSICBRAINZ_APP}, timeout=15)
        if response.status_code == 503 and attempt < 4:
            time.sleep(2 ** attempt * 2)  # 2, 4, 8, 16 seconds
            continue
        response.raise_for_status()
        return response


def musicbrainz_lookup(artist, album):
    """-> (genre tags, release id, original release year). Empty values if not found."""
    try:
        data = mb_get("https://musicbrainz.org/ws/2/release/", {
            "query": f'release:"{album}" AND artist:"{artist}"',
            "fmt": "json", "limit": 5, "inc": "release-groups",
        }).json()
        releases = data.get("releases", [])
        if not releases:
            return [], None, None
        mbid = releases[0].get("id")
        rg_id = releases[0].get("release-group", {}).get("id")
        if not rg_id:
            return [], mbid, None
        rg = mb_get(f"https://musicbrainz.org/ws/2/release-group/{rg_id}",
                    {"fmt": "json", "inc": "tags+genres"}).json()
        source = rg.get("genres") or rg.get("tags") or []
        tags = [g["name"] for g in sorted(source, key=lambda x: x.get("count", 0), reverse=True)]
        first = (rg.get("first-release-date") or "")[:4]
        return tags, mbid, int(first) if first.isdigit() else None
    except Exception as e:
        print(f"   MusicBrainz error: {e}")
        return [], None, None


def musicbrainz_tracklist(mbid):
    if not mbid:
        return []
    try:
        data = mb_get(f"https://musicbrainz.org/ws/2/release/{mbid}", {"fmt": "json", "inc": "recordings"}).json()
        media = data.get("media", [])
        tracks = []
        for medium in media:
            for t in medium.get("tracks", []):
                ms = t.get("length") or t.get("recording", {}).get("length")
                m, s = divmod(int(ms) // 1000, 60) if ms else (0, 0)
                num = t.get("position", "")
                tracks.append({
                    "num": f"{medium.get('position', 1)}-{num}" if len(media) > 1 else str(num),
                    "title": t.get("title") or t.get("recording", {}).get("title", ""),
                    "duration": f"{m}:{s:02d}" if ms else "",
                })
        return tracks
    except Exception as e:
        print(f"   MusicBrainz tracklist error: {e}")
        return []
