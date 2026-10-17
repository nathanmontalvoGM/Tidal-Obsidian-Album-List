const page = dv.current();
const file = app.vault.getAbstractFileByPath(page.file.path);
const content = (await app.vault.cachedRead(file)).replace(/\r\n/g, "\n");

const baseName = page.file.name.replace(/\s\(\d{4}\)$/, "");
const title = page.title || baseName;
const artist = page.artist || "";
const year = page.year || "";
const tidalId = page.tidal_id;

function findCover(page) {
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
    return h ? `${h}:${String(m).padStart(2, "0")}:${String(sec).padStart(2, "0")}` : `${m}:${String(sec).padStart(2, "0")}`;
};

const nav = dv.container.createEl("div");
nav.style.cssText = "display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;";
const backBtn = nav.createEl("a");
backBtn.textContent = "← Library";
backBtn.style.cssText = "display:inline-block; padding:10px 20px; background:#7c3aed; color:#fff; border-radius:10px; font-size:15px; font-weight:bold; text-decoration:none; cursor:pointer;";
backBtn.onclick = e => { e.preventDefault(); app.workspace.openLinkText("00 Dashboard/Library", "", false); };

const header = dv.container.createEl("div");
header.style.cssText = "display:flex; flex-wrap:wrap; gap:20px; align-items:flex-end; margin-bottom:20px;";

const img = header.createEl("img");
img.style.cssText = "width:220px; height:220px; object-fit:cover; border-radius:12px; box-shadow:0 8px 24px rgba(0,0,0,0.5); background:#333;";
if (cover) img.src = app.vault.getResourcePath(cover);

const info = header.createEl("div");
info.style.cssText = "flex:1; min-width:200px;";
const t = info.createEl("div"); t.textContent = title; t.style.cssText = "color:#fff; font-size:26px; font-weight:bold; line-height:1.2;";
const a = info.createEl("div"); a.textContent = artist; a.style.cssText = "color:#aaa; font-size:17px; margin-top:4px;";
const meta = info.createEl("div");
meta.textContent = [year, `${tracks.length} tracks`, totalSec ? fmtTime(totalSec) : null].filter(Boolean).join(" · ");
meta.style.cssText = "color:#666; font-size:13px; margin-top:6px;";

const btnRow = info.createEl("div");
btnRow.style.cssText = "display:flex; flex-wrap:wrap; gap:10px; margin-top:14px;";
function linkButton(label, url, primary) {
    const b = btnRow.createEl("div");
    b.textContent = label;
    b.style.cssText = `padding:10px 18px; border-radius:10px; font-size:14px; font-weight:bold; cursor:pointer; color:#fff; background:${primary ? "#7c3aed" : "#1a1a1a"}; box-shadow:0 4px 12px rgba(0,0,0,0.4);`;
    b.onclick = () => window.open(url);
}
if (tidalId) linkButton("▶ Play on Tidal", `tidal://album/${tidalId}`, true);
linkButton("Album of the Year", `https://www.albumoftheyear.org/search/?q=${encodeURIComponent(`${artist} ${title}`)}`, false);

const ratingEl = dv.container.createEl("div");
ratingEl.style.cssText = "font-size:18px; font-weight:bold; padding:6px 0 4px 0; color:" + (avg !== null ? "#fff" : "#666") + ";";
ratingEl.textContent = avg !== null
    ? `Overall Rating: ${avg.toFixed(1)} / 10 (${ratings.length} of ${tracks.length} tracks rated)`
    : "Overall Rating: No tracks rated yet";

const th = dv.container.createEl("h2");
th.textContent = "Tracklist";
th.style.cssText = "margin-top:16px;";