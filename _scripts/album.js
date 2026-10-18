const page = dv.current();
const file = app.vault.getAbstractFileByPath(page.file.path);
const content = (await app.vault.cachedRead(file)).replace(/\r\n/g, "\n");

const baseName = page.file.name.replace(/\s\(\d{4}\)$/, "");
const title = page.title || baseName;
const artist = page.artist || "";
const year = page.year || "";
const tidalId = page.tidal_id;
const tags = (Array.isArray(page.tags) ? page.tags : page.tags ? [page.tags] : [])
    .map(t => String(t).replace(/^#/, "")).filter(Boolean);

function findCover(page) {
    // 1. The album's own cover property (set by the importer), e.g. cover: "[[_covers/Artist - Album.jpg]]"
    if (page.cover) {
        const link = page.cover.path || String(page.cover).replace(/^\[\[|\]\]$/g, "").split("|")[0];
        const f = app.metadataCache.getFirstLinkpathDest(link, page.file.path) || app.vault.getAbstractFileByPath(link);
        if (f) return f;
    }
    // 2. Fallback for notes without one: rebuild the filename the importer would have used
    const clean = s => String(s || "").replace(/[\\/*?:"<>|]/g, "-").replace(/…/g, "...").replace(/^[. ]+|[. ]+$/g, "");
    const title = page.file.name.replace(/\s\(\d{4}\)$/, "");
    const folder = page.file.folder.split("/").pop();
    for (const artist of [clean(page.artist), page.artist, folder]) {
        const f = app.vault.getAbstractFileByPath(`_covers/${artist} - ${title}.jpg`);
        if (f) return f;
    }
    return null;
}
const cover = findCover(page);
const coverSrc = cover ? app.vault.getResourcePath(cover) : null;

// Tracklist rows: | # | Title | Duration | Rating /10 |  (the table in the note stays the source of truth)
const TRACK_ROW = /^\|\s*(\d+(?:-\d+)?)\s*\|/;
const tracks = content.split("\n").filter(l => TRACK_ROW.test(l)).map(r => {
    const cols = r.split("|").map(c => c.trim());
    return {
        num: cols[1],
        title: cols.slice(2, cols.length - 3).join("|"),
        duration: cols[cols.length - 3],
        rating: parseFloat(cols[cols.length - 2]),
    };
});
const rated = () => tracks.map(t => t.rating).filter(v => !isNaN(v) && v > 0);
const trackAvg = () => { const r = rated(); return r.length ? r.reduce((a, b) => a + b, 0) / r.length : null; };
let albumScore = parseFloat(page.rating);
if (isNaN(albumScore)) albumScore = null;

const totalSec = tracks.reduce((sum, t) => {
    const parts = (t.duration || "").split(":").map(Number);
    if (parts.length < 2 || parts.some(isNaN)) return sum;
    return sum + parts.reduce((acc, n) => acc * 60 + n, 0);
}, 0);
const fmtTime = s => {
    const h = Math.floor(s / 3600), m = Math.floor((s % 3600) / 60), sec = s % 60;
    return h ? `${h} hr ${m} min` : `${m}:${String(sec).padStart(2, "0")}`;
};
const scoreColor = v =>
    v === null ? "rgba(255,255,255,0.4)" :
    v >= 8 ? "#4ade80" : v >= 6 ? "#facc15" : v >= 4 ? "#fb923c" : "#f87171";

const STYLE_ID = "album-view-styles";
document.getElementById(STYLE_ID)?.remove();
const style = document.createElement("style");
style.id = STYLE_ID;
style.textContent = `
.view-content:has(.av-root) .metadata-container,
.view-content:has(.av-root) .inline-title { display: none !important; }
.view-content:has(.av-root) .markdown-rendered table,
.view-content:has(.av-root) .cm-table-widget { display: none !important; }

.av-root { --av-accent: #7c3aed; container-type: inline-size; }

.av-hero { position: relative; overflow: hidden; border-radius: 20px; padding: 20px 22px 24px; margin-bottom: 26px; background: #141414; }
.av-hero-bg { position: absolute; inset: -60px; background-size: cover; background-position: center; filter: blur(45px) brightness(0.45) saturate(1.4); }
.av-hero-inner { position: relative; }

.av-nav { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 20px; }
.av-back { display: inline-block; padding: 6px 14px; border-radius: 999px; background: rgba(255,255,255,0.12); color: #fff; font-size: 13px; font-weight: 600; cursor: pointer; max-width: 100%; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.av-back:hover { background: rgba(255,255,255,0.22); }

.av-main { display: flex; flex-wrap: wrap; gap: 24px; align-items: flex-end; }
.av-cover { width: 210px; height: 210px; border-radius: 12px; object-fit: cover; box-shadow: 0 14px 36px rgba(0,0,0,0.6); background: #2a2a2a; flex-shrink: 0; }
.av-cover-empty { display: flex; align-items: center; justify-content: center; font-size: 64px; color: #555; }

.av-info { flex: 1; min-width: 220px; }
.av-kicker { font-size: 11px; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; color: rgba(255,255,255,0.6); }
.av-title { font-size: 32px; font-weight: 800; color: #fff; line-height: 1.1; margin: 6px 0 6px; }
.av-artist { font-size: 17px; font-weight: 600; color: rgba(255,255,255,0.88); }
.av-meta { font-size: 13px; color: rgba(255,255,255,0.55); margin-top: 4px; }
.av-removed { display: inline-block; margin-top: 8px; font-size: 11px; font-weight: 700; padding: 3px 10px; border-radius: 999px; background: rgba(248,113,113,0.15); color: #f87171; }

.av-tags { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 12px; }
.av-tag { font-size: 11px; padding: 3px 10px; border-radius: 999px; background: rgba(255,255,255,0.1); color: rgba(255,255,255,0.8); cursor: pointer; }
.av-tag:hover { background: rgba(255,255,255,0.22); color: #fff; }
.av-tag.edit { background: transparent; border: 1px dashed rgba(255,255,255,0.35); color: rgba(255,255,255,0.65); }

.av-te-current { display: flex; flex-wrap: wrap; gap: 8px; min-height: 34px; margin-bottom: 14px; }
.av-te-pill { padding: 7px 12px; border-radius: 999px; font-size: 13px; font-weight: 600; background: #7c3aed; color: #fff; cursor: pointer; }
.av-te-none { font-size: 13px; color: #666; padding: 8px 0; }
.av-te-input { width: 100%; box-sizing: border-box; padding: 11px 14px; border-radius: 10px; border: 1px solid #444; background: #222; color: #fff; font-size: 15px; margin-bottom: 10px; }
.av-te-sugs { display: flex; flex-wrap: wrap; gap: 8px; max-height: 160px; overflow-y: auto; }
.av-te-sug { padding: 7px 12px; border-radius: 999px; font-size: 13px; background: #262626; color: #ccc; cursor: pointer; border: 1px solid #333; }
.av-te-sug.new { border-style: dashed; color: #fff; }
.av-te-msg { font-size: 12px; color: #f87171; min-height: 16px; margin-top: 8px; }
.av-sheet-btn.primary { background: #7c3aed; color: #fff; }

.av-actions { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 16px; }
.av-btn { padding: 9px 18px; border-radius: 999px; font-size: 14px; font-weight: 700; color: #fff; background: rgba(255,255,255,0.12); cursor: pointer; transition: background 0.15s; }
.av-btn:hover { background: rgba(255,255,255,0.22); }
.av-btn.primary { background: var(--av-accent); }
.av-btn.primary:hover { filter: brightness(1.15); }
.av-btn.fave-on { background: rgba(245,158,11,0.18); color: #f59e0b; }

.av-score { display: flex; flex-direction: column; align-items: center; justify-content: center; min-width: 96px; padding: 14px 16px; border-radius: 16px; background: rgba(0,0,0,0.35); margin-left: auto; }
.av-score-num { font-size: 36px; font-weight: 800; line-height: 1; }
.av-score-sub { font-size: 11px; color: rgba(255,255,255,0.6); margin-top: 6px; white-space: nowrap; }

.av-section { display: flex; align-items: baseline; justify-content: space-between; gap: 12px; margin: 0 2px 10px; }
.av-section-title { font-size: 13px; font-weight: 800; letter-spacing: 0.14em; text-transform: uppercase; color: rgba(255,255,255,0.75); }
.av-section-sub { font-size: 12px; color: #666; }

.av-score { cursor: pointer; }
.av-tracks { display: flex; flex-direction: column; }
.av-track { display: flex; align-items: center; gap: 12px; padding: 10px 8px; border-radius: 10px; cursor: pointer; }
.av-track:hover { background: rgba(255,255,255,0.05); }
.av-track + .av-track { border-top: 1px solid rgba(255,255,255,0.05); }
.av-tnum { width: 28px; flex-shrink: 0; text-align: right; font-size: 13px; color: #666; font-variant-numeric: tabular-nums; }
.av-ttitle { flex: 1; min-width: 0; font-size: 15px; color: #eee; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.av-tdur { font-size: 13px; color: #666; font-variant-numeric: tabular-nums; }
.av-trate { min-width: 40px; text-align: center; padding: 4px 8px; border-radius: 999px; font-size: 14px; font-weight: 800; background: rgba(255,255,255,0.06); }

.av-sheet-bg { position: fixed; inset: 0; z-index: 9999; background: rgba(0,0,0,0.7); display: flex; align-items: flex-end; justify-content: center; }
.av-sheet { width: 100%; max-width: 520px; background: #1a1a1a; border-radius: 20px 20px 0 0; padding: 18px 18px 28px; box-shadow: 0 -8px 40px rgba(0,0,0,0.8); }
.av-sheet-top { display: flex; align-items: flex-start; gap: 12px; margin-bottom: 16px; }
.av-sheet-head { flex: 1; min-width: 0; }
.av-sheet-kicker { font-size: 11px; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; color: #777; }
.av-sheet-title { font-size: 18px; font-weight: 800; color: #fff; margin-top: 4px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.av-sheet-x { width: 36px; height: 36px; border-radius: 10px; background: #333; color: #aaa; display: flex; align-items: center; justify-content: center; cursor: pointer; flex-shrink: 0; }
.av-readout { text-align: center; font-size: 48px; font-weight: 800; line-height: 1; margin: 2px 0 14px; font-variant-numeric: tabular-nums; }
.av-slider { padding: 0 14px; }
.av-bar { position: relative; height: 48px; touch-action: none; cursor: pointer; user-select: none; }
.av-bar-track, .av-bar-fill { position: absolute; left: 0; top: 50%; height: 8px; margin-top: -4px; border-radius: 999px; }
.av-bar-track { right: 0; background: #333; }
.av-bar-mark { position: absolute; top: 50%; width: 2px; height: 14px; margin: -7px 0 0 -1px; background: #4a4a4a; border-radius: 1px; }
.av-bar-thumb { position: absolute; top: 50%; width: 28px; height: 28px; margin: -14px 0 0 -14px; border-radius: 50%; background: #fff; box-shadow: 0 2px 10px rgba(0,0,0,0.6); }
.av-ticks { position: relative; height: 16px; }
.av-tick { position: absolute; transform: translateX(-50%); font-size: 11px; color: #666; font-variant-numeric: tabular-nums; }
.av-hint { text-align: center; font-size: 12px; color: #555; margin-top: 10px; }
.av-sheet-row { display: flex; gap: 8px; margin-top: 12px; }
.av-sheet-btn { flex: 1; padding: 12px; border-radius: 12px; text-align: center; font-size: 14px; font-weight: 700; color: #aaa; background: #262626; cursor: pointer; }

@container (max-width: 560px) {
    .av-main { gap: 16px; }
    .av-cover { width: 140px; height: 140px; }
    .av-title { font-size: 24px; }
    .av-score { margin-left: 0; flex-direction: row; gap: 10px; padding: 10px 14px; }
    .av-score-num { font-size: 26px; }
    .av-score-sub { margin-top: 0; }
}
`;
document.head.appendChild(style);

const root = dv.container.createDiv({ cls: "av-root" });

const hero = root.createDiv({ cls: "av-hero" });
const bg = hero.createDiv({ cls: "av-hero-bg" });
if (coverSrc) bg.style.backgroundImage = `url("${coverSrc}")`;
const inner = hero.createDiv({ cls: "av-hero-inner" });

// Back buttons: the playlist (or genre page / Home) you opened this album from, then the Library.
// Playlists save where you came from when you tap an album; it only counts if it was this album.
const nav = inner.createDiv({ cls: "av-nav" });
const from = app.loadLocalStorage("music-album-from");
if (from && from.album === page.file.path && from.path && app.vault.getAbstractFileByPath(from.path)) {
    nav.createDiv({ cls: "av-back", text: `← ${from.name}` }).onclick = () => app.workspace.openLinkText(from.path, "", false);
}
nav.createDiv({ cls: "av-back", text: from && from.album === page.file.path ? "Library" : "← Library" })
    .onclick = () => app.workspace.openLinkText("00 Dashboard/Library", "", false);

const main = inner.createDiv({ cls: "av-main" });
if (coverSrc) main.createEl("img", { cls: "av-cover", attr: { src: coverSrc } });
else main.createDiv({ cls: "av-cover av-cover-empty", text: "♪" });

const info = main.createDiv({ cls: "av-info" });
info.createDiv({ cls: "av-kicker", text: ["Album", year].filter(Boolean).join(" · ") });
info.createDiv({ cls: "av-title", text: title });
info.createDiv({ cls: "av-artist", text: artist });
info.createDiv({ cls: "av-meta", text: [`${tracks.length} tracks`, totalSec ? fmtTime(totalSec) : null].filter(Boolean).join(" · ") });
if (page.removed_from_tidal) info.createDiv({ cls: "av-removed", text: "Not in your Tidal favorites anymore" });

// "Favorite" is a tag (Home's Favorites tool and the Favorite genre page use it), but it gets its own
// button instead of showing up among the genre tags.
const FAVE = "Favorite";
const isFaveTag = t => String(t).toLowerCase() === FAVE.toLowerCase();
let currentTags = [...tags];
const tagRow = info.createDiv({ cls: "av-tags" });
function paintTags() {
    tagRow.empty();
    const genres = currentTags.filter(t => !isFaveTag(t));
    for (const t of genres) {
        const pill = tagRow.createSpan({ cls: "av-tag", text: t });
        pill.onclick = () => app.workspace.openLinkText(`00 Dashboard/Genres/${t}`, "", false);
    }
    tagRow.createSpan({ cls: "av-tag edit", text: genres.length ? "✎ Edit tags" : "+ Add tags" }).onclick = () => openTagEditor();
}
paintTags();

const actions = info.createDiv({ cls: "av-actions" });
function button(label, url, primary) {
    const b = actions.createDiv({ cls: primary ? "av-btn primary" : "av-btn", text: label });
    b.onclick = () => window.open(url);
}
if (tidalId) button("▶ Play on Tidal", `tidal://album/${tidalId}`, true);

const faveBtn = actions.createDiv({ cls: "av-btn" });
function paintFave() {
    const on = currentTags.some(isFaveTag);
    faveBtn.setText(on ? "★ Favorited" : "☆ Favorite");
    faveBtn.className = on ? "av-btn fave-on" : "av-btn";
}
paintFave();
let faveBusy = false;
faveBtn.onclick = async () => {
    if (faveBusy) return;
    faveBusy = true;
    const next = currentTags.some(isFaveTag) ? currentTags.filter(t => !isFaveTag(t)) : [FAVE, ...currentTags];
    try {
        await saveTags(next, false); // favoriting isn't editing genres, so retag still fills in missing genres
        currentTags = next;
        paintFave();
    } catch (e) {
        new Notice("Could not update favorites: " + e.message);
    }
    faveBusy = false;
};
button("Album of the Year", `https://www.albumoftheyear.org/search/?q=${encodeURIComponent(`${artist} ${title}`)}`, false);

// Score: your album score (the `rating` property) if you've set one, otherwise the track average. Tap to set it.
const score = main.createDiv({ cls: "av-score" });
const scoreNum = score.createDiv({ cls: "av-score-num" });
const scoreSub = score.createDiv({ cls: "av-score-sub" });
function paintScore() {
    const avg = trackAvg();
    const shown = albumScore ?? avg;
    scoreNum.setText(shown !== null ? (albumScore !== null ? String(albumScore) : avg.toFixed(1)) : "—");
    scoreNum.style.color = scoreColor(shown);
    scoreSub.setText(albumScore !== null
        ? (avg !== null ? `Your score · tracks ${avg.toFixed(1)}` : "Your score")
        : avg !== null ? `${rated().length} / ${tracks.length} rated` : "Tap to rate");
}
paintScore();
score.onclick = () => openSheet({ album: true });

const section = root.createDiv({ cls: "av-section" });
section.createDiv({ cls: "av-section-title", text: "Tracklist" });
section.createDiv({ cls: "av-section-sub", text: tracks.length ? "Tap a track to rate it" : "No tracklist yet. Run the Tidal sync to add one" });

const list = root.createDiv({ cls: "av-tracks" });
const fmtRating = v => isNaN(v) || v === null ? "—" : String(v);
const rows = tracks.map((t, i) => {
    const row = list.createDiv({ cls: "av-track" });
    row.createDiv({ cls: "av-tnum", text: t.num });
    row.createDiv({ cls: "av-ttitle", text: t.title });
    row.createDiv({ cls: "av-tdur", text: t.duration });
    const r = row.createDiv({ cls: "av-trate" });
    row.onclick = () => openSheet({ index: i });
    return r;
});
function paintTrack(i) {
    const v = tracks[i].rating;
    rows[i].setText(fmtRating(v));
    rows[i].style.color = isNaN(v) ? "#555" : scoreColor(v);
}
tracks.forEach((_, i) => paintTrack(i));

// ── Saving ── edits only the one table cell / property line, so nothing else in the note moves
async function saveTrack(i, value) {
    const t = tracks[i];
    await app.vault.process(file, text => {
        const nl = text.includes("\r\n") ? "\r\n" : "\n";
        const lines = text.split(/\r?\n/);
        const at = lines.findIndex(l => { const m = l.match(TRACK_ROW); return m && m[1] === t.num; });
        if (at < 0) throw new Error(`Track ${t.num} not found in the note`);
        const cols = lines[at].split("|");
        cols[cols.length - 2] = ` ${value ?? ""} `;
        lines[at] = cols.join("|");
        return lines.join(nl);
    });
}
async function saveAlbumScore(value) {
    await app.vault.process(file, text => {
        const fm = text.match(/^---\r?\n([\s\S]*?)\r?\n---/);
        if (!fm) throw new Error("This note has no properties block");
        const nl = text.includes("\r\n") ? "\r\n" : "\n";
        let body = fm[1];
        const line = `rating:${value === null ? "" : " " + value}`;
        body = /^rating:.*$/m.test(body) ? body.replace(/^rating:.*$/m, line) : body + nl + line;
        return text.slice(0, fm.index) + `---${nl}${body}${nl}---` + text.slice(fm.index + fm[0].length);
    });
}

// ── Rating sheet ── after rating a track it moves on to the next one, so you can rate a whole album in one go
function openSheet(target) {
    const bgEl = document.body.createDiv({ cls: "av-sheet-bg" });
    const sheet = bgEl.createDiv({ cls: "av-sheet" });
    // Bar from 0.5 to 10 in half points: tap or drag, the readout follows, letting go saves. Arrow keys + Enter on desktop.
    const MIN = 0.5, MAX = 10, STEP = 0.5;
    const snap = v => Math.min(MAX, Math.max(MIN, Math.round(v / STEP) * STEP));
    let value = null, show = () => {};
    const onKey = e => {
        if (e.key === "Escape") return close();
        if (e.key === "ArrowRight" || e.key === "ArrowUp") { value = snap((value ?? 0) + STEP); show(value); e.preventDefault?.(); }
        if (e.key === "ArrowLeft" || e.key === "ArrowDown") { value = snap((value ?? MIN + STEP) - STEP); show(value); e.preventDefault?.(); }
        if (e.key === "Enter" && value !== null) pick(value);
    };
    const close = () => { bgEl.remove(); document.removeEventListener("keydown", onKey); };
    bgEl.onclick = e => { if (e.target === bgEl) close(); };
    document.addEventListener("keydown", onKey);

    function render() {
        sheet.empty();
        const isAlbum = !!target.album;
        const current = isAlbum ? albumScore : tracks[target.index].rating;
        const top = sheet.createDiv({ cls: "av-sheet-top" });
        const head = top.createDiv({ cls: "av-sheet-head" });
        head.createDiv({ cls: "av-sheet-kicker", text: isAlbum ? "Album score" : `Track ${target.index + 1} of ${tracks.length}` });
        head.createDiv({ cls: "av-sheet-title", text: isAlbum ? title : tracks[target.index].title });
        top.createDiv({ cls: "av-sheet-x", text: "✕" }).onclick = close;

        const readout = sheet.createDiv({ cls: "av-readout" });
        const slider = sheet.createDiv({ cls: "av-slider" });
        const bar = slider.createDiv({ cls: "av-bar" });
        bar.createDiv({ cls: "av-bar-track" });
        for (let v = 1; v < MAX; v++) bar.createDiv({ cls: "av-bar-mark" }).style.left = `${v / MAX * 100}%`;
        const fill = bar.createDiv({ cls: "av-bar-fill" });
        const thumb = bar.createDiv({ cls: "av-bar-thumb" });
        const ticks = slider.createDiv({ cls: "av-ticks" });
        for (let v = 1; v <= MAX; v++) ticks.createDiv({ cls: "av-tick", text: String(v) }).style.left = `${v / MAX * 100}%`;
        sheet.createDiv({ cls: "av-hint", text: "Tap or drag, let go to save" });

        show = v => {
            const has = v !== null && !isNaN(v);
            readout.setText(has ? fmtRating(v) : "—");
            readout.style.color = has ? scoreColor(v) : "#555";
            fill.style.width = has ? `${v / MAX * 100}%` : "0";
            fill.style.background = has ? scoreColor(v) : "transparent";
            thumb.style.display = has ? "" : "none";
            if (has) thumb.style.left = `${v / MAX * 100}%`;
        };
        value = current === null || isNaN(current) ? null : current;
        show(value);

        const valueAt = x => { const r = bar.getBoundingClientRect(); return snap((x - r.left) / r.width * MAX); };
        let dragging = false;
        bar.addEventListener("pointerdown", e => {
            dragging = true;
            bar.setPointerCapture?.(e.pointerId);
            value = valueAt(e.clientX); show(value);
            e.preventDefault?.();
        });
        bar.addEventListener("pointermove", e => { if (dragging) { value = valueAt(e.clientX); show(value); } });
        bar.addEventListener("pointerup", e => { if (!dragging) return; dragging = false; pick(valueAt(e.clientX)); });
        bar.addEventListener("pointercancel", () => { dragging = false; value = current === null || isNaN(current) ? null : current; show(value); });
        const row = sheet.createDiv({ cls: "av-sheet-row" });
        row.createDiv({ cls: "av-sheet-btn", text: "Clear" }).onclick = () => pick(null);
        if (!isAlbum && target.index < tracks.length - 1)
            row.createDiv({ cls: "av-sheet-btn", text: "Skip →" }).onclick = () => { target.index++; render(); };
    }

    async function pick(v) {
        try {
            if (target.album) {
                await saveAlbumScore(v);
                albumScore = v;
                paintScore();
                return close();
            }
            const i = target.index;
            await saveTrack(i, v);
            tracks[i].rating = v === null ? NaN : v;
            paintTrack(i);
            paintScore();
            if (i < tracks.length - 1) { target.index++; render(); } else close();
        } catch (e) {
            new Notice("Could not save rating: " + e.message);
        }
    }
    render();
}


// ── Tag editor ── same rules as the Python scripts (_scripts/tags.json): spellings are merged into one tag,
// blocklisted junk is refused. Saving marks the note tags_edited: true so `library.py retag` leaves it alone.
const GENRES = "00 Dashboard/Genres";
const GENRE_STUB = '```dataviewjs\nawait dv.view("_scripts/playlist", { tags: [dv.current().file.name], genre: true });\n```\n';
const tagKey = s => String(s).replace(/^#/, "").toLowerCase().replace(/[^a-z0-9]/g, "");

async function openTagEditor() {
    let rules = { aliases: {}, blocklist: [] };
    try { rules = JSON.parse(await app.vault.adapter.read("_scripts/tags.json")); } catch (e) { console.error("Could not read _scripts/tags.json", e); }
    const blocked = new Set(rules.blocklist || []);
    // Every tag in your library, most used first, plus the canonical names in tags.json
    const counts = new Map();
    for (const p of dv.pages().where(p => p.tidal_id)) {
        for (const t of (Array.isArray(p.tags) ? p.tags : p.tags ? [p.tags] : [])) {
            const tag = String(t).replace(/^#/, "");
            counts.set(tag, (counts.get(tag) || 0) + 1);
        }
    }
    for (const c of Object.values(rules.aliases || {})) if (!counts.has(c)) counts.set(c, 0);
    for (const k of Array.from(counts.keys())) if (isFaveTag(k)) counts.delete(k);
    const known = Array.from(counts.keys()).sort((a, b) => counts.get(b) - counts.get(a) || a.localeCompare(b));
    const knownByKey = new Map(known.map(t => [tagKey(t), t]));

    // "post rock" -> PostRock (via aliases), "math pop" -> MathPop (new); null for junk
    function normalize(raw) {
        const k = tagKey(raw);
        if (!k || blocked.has(k) || /^\d+s?$/.test(k)) return null;
        if (rules.aliases && rules.aliases[k]) return rules.aliases[k];
        if (knownByKey.has(k)) return knownByKey.get(k);
        return String(raw).replace(/^#/, "").split(/[^A-Za-z0-9]+/).filter(Boolean).map(w => w[0].toUpperCase() + w.slice(1)).join("");
    }

    let working = currentTags.filter(t => !isFaveTag(t));
    const bgEl = document.body.createDiv({ cls: "av-sheet-bg" });
    const sheet = bgEl.createDiv({ cls: "av-sheet" });
    const onKey = e => { if (e.key === "Escape") close(); };
    const close = () => { bgEl.remove(); document.removeEventListener("keydown", onKey); };
    bgEl.onclick = e => { if (e.target === bgEl) close(); };
    document.addEventListener("keydown", onKey);

    const top = sheet.createDiv({ cls: "av-sheet-top" });
    const head = top.createDiv({ cls: "av-sheet-head" });
    head.createDiv({ cls: "av-sheet-kicker", text: "Edit tags · tap a tag to remove it" });
    head.createDiv({ cls: "av-sheet-title", text: title });
    top.createDiv({ cls: "av-sheet-x", text: "✕" }).onclick = close;
    const current = sheet.createDiv({ cls: "av-te-current" });
    const input = sheet.createEl("input", { cls: "av-te-input", type: "text", placeholder: "Add a tag (search or type a new one)…" });
    const sugs = sheet.createDiv({ cls: "av-te-sugs" });
    const msg = sheet.createDiv({ cls: "av-te-msg" });
    const row = sheet.createDiv({ cls: "av-sheet-row" });
    row.createDiv({ cls: "av-sheet-btn", text: "Cancel" }).onclick = close;
    row.createDiv({ cls: "av-sheet-btn primary", text: "Save" }).onclick = save;

    const has = t => working.some(w => w.toLowerCase() === t.toLowerCase());
    function add(raw) {
        const tag = normalize(raw);
        if (!tag) { msg.setText(`"${raw}" isn't a genre (it's on the tags.json blocklist).`); return; }
        if (isFaveTag(tag)) { msg.setText("Use the ☆ Favorite button for that."); return; }
        if (!has(tag)) working.push(tag);
        input.value = ""; msg.setText("");
        paint();
    }
    function paint() {
        current.empty();
        if (!working.length) current.createDiv({ cls: "av-te-none", text: "No tags" });
        for (const t of working) {
            current.createDiv({ cls: "av-te-pill", text: `${t} ✕` }).onclick = () => { working = working.filter(w => w !== t); paint(); };
        }
        sugs.empty();
        const q = tagKey(input.value);
        const list = known.filter(t => !has(t) && (!q || tagKey(t).includes(q))).slice(0, q ? 14 : 10);
        for (const t of list) sugs.createDiv({ cls: "av-te-sug", text: counts.get(t) ? `${t} · ${counts.get(t)}` : t }).onclick = () => add(t);
        const typed = input.value.trim() && normalize(input.value);
        if (typed && !has(typed) && !list.includes(typed)) sugs.createDiv({ cls: "av-te-sug new", text: `+ Add "${typed}"` }).onclick = () => add(input.value);
    }
    input.addEventListener("input", () => { msg.setText(""); paint(); });
    input.addEventListener("keydown", e => { if (e.key === "Enter" && input.value.trim()) { e.preventDefault?.(); add(input.value); } });
    paint();
    setTimeout(() => input.focus(), 50);

    async function save() {
        try {
            const final = currentTags.some(isFaveTag) ? [FAVE, ...working] : working;
            await saveTags(final);
            for (const t of working) await ensureGenrePage(t);
            currentTags = final;
            paintTags();
            close();
        } catch (e) {
            msg.setText("Could not save: " + e.message);
        }
    }
}

async function saveTags(list, markEdited = true) {
    await app.vault.process(file, raw => {
        const crlf = raw.includes("\r\n");
        const text = raw.replace(/\r\n/g, "\n");
        const fm = text.match(/^---\n([\s\S]*?)\n---/);
        if (!fm) throw new Error("This note has no properties block");
        let body = fm[1] + "\n";
        const block = list.length ? "tags:\n" + list.map(t => `  - ${t}\n`).join("") : "tags: []\n";
        const re = /^tags:[ \t]*(\[[^\]\n]*\])?[ \t]*\n((?:[ \t]+-[^\n]*\n)*)/m;
        body = re.test(body) ? body.replace(re, block) : body + block;
        if (markEdited && !/^tags_edited:/m.test(body)) body = body.replace(/^tags:/m, "tags_edited: true\ntags:");
        const out = "---\n" + body.replace(/\n$/, "") + "\n---" + text.slice(fm[0].length);
        return crlf ? out.replace(/\n/g, "\r\n") : out;
    });
}

async function ensureGenrePage(tag) {
    const folder = app.vault.getAbstractFileByPath(GENRES);
    const exists = folder && folder.children
        ? folder.children.some(f => f.name.toLowerCase() === `${tag}.md`.toLowerCase())
        : !!app.vault.getAbstractFileByPath(`${GENRES}/${tag}.md`);
    if (exists) return;
    if (!folder) await app.vault.createFolder(GENRES);
    await app.vault.create(`${GENRES}/${tag}.md`, GENRE_STUB);
}
