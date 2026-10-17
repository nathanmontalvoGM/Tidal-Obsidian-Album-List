
```dataviewjs
const PLAYLISTS_FOLDER = "00 Dashboard/Playlists";
const HOME_NOTE = "_tools/Home";

const backBtn = dv.container.createEl("a");
backBtn.textContent = "← Home";
backBtn.style.cssText = "display:inline-block; padding:10px 20px; background:#7c3aed; color:#fff; border-radius:10px; font-size:15px; font-weight:bold; text-decoration:none; cursor:pointer; margin-bottom:16px;";
backBtn.onclick = (e) => { e.preventDefault(); app.workspace.openLinkText(HOME_NOTE, "", false); };

const allPages = dv.pages().where(p => p.tidal_id).array();

const playlistFiles = app.vault.getFiles().filter(f =>
    f.path.startsWith(PLAYLISTS_FOLDER + "/") && f.extension === "md"
);

const grid = dv.container.createEl("div");
grid.style.cssText = "display:grid; grid-template-columns: repeat(2, 1fr); gap:14px; padding:10px 0;";

function normTags(page) {
    if (!page.tags) return [];
    const arr = Array.isArray(page.tags) ? page.tags : [page.tags];
    return arr.map(t => String(t).replace(/^#/, "").toLowerCase());
}

function pageHasAnyTag(page, tags) {
    const pt = normTags(page);
    return tags.some(tag => pt.includes(String(tag).toLowerCase()));
}

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
function coverFor(page) {
    const f = findCover(page);
    return f ? app.vault.getResourcePath(f) : null;
}

function coversFrom(pages) {
    const out = [];
    for (let p of pages) {
        if (out.length >= 4) break;
        const c = coverFor(p);
        if (c) out.push(c);
    }
    return out;
}

function renderCard(playlist, covers, count) {
    const card = grid.createEl("div");
    card.style.cssText = "background:#1a1a1a; border-radius:16px; overflow:hidden; cursor:pointer; box-shadow:0 4px 12px rgba(0,0,0,0.5);";
    card.onclick = () => app.workspace.openLinkText(playlist.path, "", false);

    const coverGrid = card.createEl("div");
    coverGrid.style.cssText = "display:grid; grid-template-columns:1fr 1fr; width:100%; aspect-ratio:1;";
    for (let i = 0; i < 4; i++) {
        const cell = coverGrid.createEl("div");
        cell.style.cssText = "overflow:hidden; background:#333; aspect-ratio:1;";
        if (covers[i]) {
            const img = cell.createEl("img");
            img.src = covers[i];
            img.style.cssText = "width:100%; height:100%; object-fit:cover; display:block;";
        }
    }

    const info = card.createEl("div");
    info.style.cssText = "padding:12px 14px;";
    const name = info.createEl("div");
    name.style.cssText = "color:#fff; font-size:16px; font-weight:bold; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;";
    name.textContent = playlist.basename;
    const countEl = info.createEl("div");
    countEl.style.cssText = "color:#aaa; font-size:12px; margin-top:3px;";
    countEl.textContent = count + " albums";
}

for (let file of playlistFiles) {
    app.vault.cachedRead(file).then(text => {
        const tagMatch = text.match(/const TAGS\s*=\s*(\[[\s\S]*?\]);/);
        const idMatch  = text.match(/const ALBUM_IDS\s*=\s*(\[[\s\S]*?\]);/);
        try {
            if (tagMatch) {
                const tags = JSON.parse(tagMatch[1]);
                const matches = allPages.filter(p => pageHasAnyTag(p, tags));
                renderCard(file, coversFrom(matches), matches.length);
            } else if (idMatch) {
                const ids = JSON.parse(idMatch[1]).map(String);
                const matches = allPages.filter(p => ids.includes(String(p.tidal_id)));
                renderCard(file, coversFrom(matches), matches.length);
            } else {
                renderCard(file, [], 0);
            }
        } catch(e) {
            console.error("Playlist card failed:", file.path, e);
            renderCard(file, [], 0);
        }
    });
}
```