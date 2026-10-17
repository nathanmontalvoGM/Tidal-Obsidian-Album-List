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

const cover = app.vault.getAbstractFileByPath(`_covers/${artist} - ${baseName}.jpg`);
const coverSrc = cover ? app.vault.getResourcePath(cover) : null;

const trackRows = content.split("\n").filter(l => /^\|\s*\d+(-\d+)?\s*\|/.test(l));
const tracks = trackRows.map(r => {
    const cols = r.split("|").map(c => c.trim());
    return { duration: cols[cols.length - 3], rating: parseFloat(cols[cols.length - 2]) };
});
const ratings = tracks.map(t => t.rating).filter(v => !isNaN(v) && v > 0);
const avg = ratings.length ? ratings.reduce((a, b) => a + b, 0) / ratings.length : null;

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
.view-content:has(.av-root) table { width: 100% !important; margin-left: 0 !important; margin-right: 0 !important; }

.av-root { --av-accent: #7c3aed; container-type: inline-size; }

.av-hero { position: relative; overflow: hidden; border-radius: 20px; padding: 20px 22px 24px; margin-bottom: 26px; background: #141414; }
.av-hero-bg { position: absolute; inset: -60px; background-size: cover; background-position: center; filter: blur(45px) brightness(0.45) saturate(1.4); }
.av-hero-inner { position: relative; }

.av-back { display: inline-block; padding: 6px 14px; border-radius: 999px; background: rgba(255,255,255,0.12); color: #fff; font-size: 13px; font-weight: 600; cursor: pointer; margin-bottom: 20px; }
.av-back:hover { background: rgba(255,255,255,0.22); }

.av-main { display: flex; flex-wrap: wrap; gap: 24px; align-items: flex-end; }
.av-cover { width: 210px; height: 210px; border-radius: 12px; object-fit: cover; box-shadow: 0 14px 36px rgba(0,0,0,0.6); background: #2a2a2a; flex-shrink: 0; }
.av-cover-empty { display: flex; align-items: center; justify-content: center; font-size: 64px; color: #555; }

.av-info { flex: 1; min-width: 220px; }
.av-kicker { font-size: 11px; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; color: rgba(255,255,255,0.6); }
.av-title { font-size: 32px; font-weight: 800; color: #fff; line-height: 1.1; margin: 6px 0 6px; }
.av-artist { font-size: 17px; font-weight: 600; color: rgba(255,255,255,0.88); }
.av-meta { font-size: 13px; color: rgba(255,255,255,0.55); margin-top: 4px; }

.av-tags { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 12px; }
.av-tag { font-size: 11px; padding: 3px 10px; border-radius: 999px; background: rgba(255,255,255,0.1); color: rgba(255,255,255,0.8); }

.av-actions { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 16px; }
.av-btn { padding: 9px 18px; border-radius: 999px; font-size: 14px; font-weight: 700; color: #fff; background: rgba(255,255,255,0.12); cursor: pointer; transition: background 0.15s; }
.av-btn:hover { background: rgba(255,255,255,0.22); }
.av-btn.primary { background: var(--av-accent); }
.av-btn.primary:hover { filter: brightness(1.15); }

.av-score { display: flex; flex-direction: column; align-items: center; justify-content: center; min-width: 96px; padding: 14px 16px; border-radius: 16px; background: rgba(0,0,0,0.35); margin-left: auto; }
.av-score-num { font-size: 36px; font-weight: 800; line-height: 1; }
.av-score-sub { font-size: 11px; color: rgba(255,255,255,0.6); margin-top: 6px; white-space: nowrap; }

.av-section { display: flex; align-items: baseline; justify-content: space-between; gap: 12px; margin: 0 2px 10px; }
.av-section-title { font-size: 13px; font-weight: 800; letter-spacing: 0.14em; text-transform: uppercase; color: rgba(255,255,255,0.75); }
.av-section-sub { font-size: 12px; color: #666; }

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

const back = inner.createDiv({ cls: "av-back", text: "← Library" });
back.onclick = () => app.workspace.openLinkText("00 Dashboard/Library", "", false);

const main = inner.createDiv({ cls: "av-main" });
if (coverSrc) main.createEl("img", { cls: "av-cover", attr: { src: coverSrc } });
else main.createDiv({ cls: "av-cover av-cover-empty", text: "♪" });

const info = main.createDiv({ cls: "av-info" });
info.createDiv({ cls: "av-kicker", text: ["Album", year].filter(Boolean).join(" · ") });
info.createDiv({ cls: "av-title", text: title });
info.createDiv({ cls: "av-artist", text: artist });
info.createDiv({ cls: "av-meta", text: [`${tracks.length} tracks`, totalSec ? fmtTime(totalSec) : null].filter(Boolean).join(" · ") });

if (tags.length) {
    const tagRow = info.createDiv({ cls: "av-tags" });
    for (const t of tags) tagRow.createSpan({ cls: "av-tag", text: t });
}

const actions = info.createDiv({ cls: "av-actions" });
function button(label, url, primary) {
    const b = actions.createDiv({ cls: primary ? "av-btn primary" : "av-btn", text: label });
    b.onclick = () => window.open(url);
}
if (tidalId) button("▶ Play on Tidal", `tidal://album/${tidalId}`, true);
button("Album of the Year", `https://www.albumoftheyear.org/search/?q=${encodeURIComponent(`${artist} ${title}`)}`, false);

const score = main.createDiv({ cls: "av-score" });
const scoreNum = score.createDiv({ cls: "av-score-num", text: avg !== null ? avg.toFixed(1) : "—" });
scoreNum.style.color = scoreColor(avg);
score.createDiv({ cls: "av-score-sub", text: avg !== null ? `${ratings.length} / ${tracks.length} rated` : "Not rated yet" });

const section = root.createDiv({ cls: "av-section" });
section.createDiv({ cls: "av-section-title", text: "Tracklist" });
section.createDiv({ cls: "av-section-sub", text: "Rate tracks in the last column" });