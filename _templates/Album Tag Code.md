# 🏷 PowerMetal
```dataviewjs
const TAG = "PowerMetal"; // <- Change this for each new note


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
function getCover(page) { return findCover(page); }

const pages = dv.pages().where(p =>
    p.tidal_id &&
    p.tags &&
    p.tags.some(t => t.toLowerCase() === TAG.toLowerCase() || t.toLowerCase() === "#" + TAG.toLowerCase())
).sort(p => p.artist);

dv.container.style.cssText = "display:flex; flex-wrap:wrap; gap:16px; padding:10px 0;";

if (pages.length === 0) {
    const empty = dv.container.createEl("div");
    empty.style.cssText = "color:#666; font-style:italic; padding:10px;";
    empty.textContent = "No albums tagged with " + TAG + " yet.";
} else {
    for (let page of pages) {
        const card = dv.container.createEl("div");
        card.style.cssText = `
            width: 160px;
            background: #1a1a1a;
            border-radius: 10px;
            overflow: hidden;
            cursor: pointer;
            transition: transform 0.2s;
            box-shadow: 0 4px 10px rgba(0,0,0,0.4);
        `;
        card.onmouseenter = () => card.style.transform = "scale(1.05)";
        card.onmouseleave = () => card.style.transform = "scale(1.0)";

        const img = card.createEl("img");
        img.style.cssText = "width:160px; height:160px; object-fit:cover; display:block;";
        const coverFile = getCover(page);
        if (coverFile) {
            img.src = app.vault.getResourcePath(coverFile);
        } else {
            img.style.cssText += "background:#333;";
        }

        const info = card.createEl("div");
        info.style.cssText = "padding: 8px 10px;";

        const title = info.createEl("div");
        title.style.cssText = "color:#fff; font-weight:bold; font-size:12px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;";
        title.textContent = page.title || page.file.name;

        const artist = info.createEl("div");
        artist.style.cssText = "color:#aaa; font-size:11px; margin-top:2px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;";
        artist.textContent = page.artist || "";

        const year = info.createEl("div");
        year.style.cssText = "color:#666; font-size:10px; margin-top:2px;";
        year.textContent = page.year || "";

        card.onclick = () => app.workspace.openLinkText(page.file.path, "", false);
        dv.container.appendChild(card);
    }
}
```