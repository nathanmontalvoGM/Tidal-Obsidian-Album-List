
```dataviewjs
window._toolsPages = dv.pages().where(p => p.tidal_id);
window._toolsCovers = app.vault.getFiles().filter(f => f.path.includes("_covers"));

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
window._toolsGetCover = findCover;

window._toolsCreateModal = function(title) {
    const overlay = document.body.createEl("div");
    overlay.style.cssText = "position:fixed; inset:0; background:rgba(0,0,0,0.85); z-index:9999; display:flex; align-items:flex-end; justify-content:center;";
    const modal = overlay.createEl("div");
    modal.style.cssText = "background:#1a1a1a; border-radius:20px 20px 0 0; width:100%; max-height:92vh; display:flex; flex-direction:column; box-shadow:0 -8px 40px rgba(0,0,0,0.8); overflow:hidden;";
    const handle = modal.createEl("div");
    handle.style.cssText = "width:40px; height:4px; background:#444; border-radius:2px; margin:12px auto 0 auto; flex-shrink:0;";
    const header = modal.createEl("div");
    header.style.cssText = "display:flex; align-items:center; justify-content:space-between; padding:14px 20px; border-bottom:1px solid #333; flex-shrink:0;";
    const titleEl = header.createEl("div");
    titleEl.textContent = title;
    titleEl.style.cssText = "color:#fff; font-size:18px; font-weight:bold;";
    const closeBtn = header.createEl("button");
    closeBtn.textContent = "✕";
    closeBtn.style.cssText = "background:#333; border:none; border-radius:8px; color:#aaa; font-size:18px; width:40px; height:40px; cursor:pointer; flex-shrink:0;";
    closeBtn.onclick = () => overlay.remove();
    overlay.onclick = (e) => { if (e.target === overlay) overlay.remove(); };
    const body = modal.createEl("div");
    body.style.cssText = "padding:16px 16px 32px 16px; overflow-y:auto; flex:1; -webkit-overflow-scrolling:touch;";
    return { overlay, modal, body, titleEl };
}

window._toolsSavePlaylist = async function(name, content, overlay) {
    const folder = "00 Dashboard/Playlists";
    const filename = `${folder}/${name}.md`;
    try {
        const existing = app.vault.getAbstractFileByPath(filename);
        if (existing) await app.vault.modify(existing, content);
        else await app.vault.create(filename, content);
        overlay.remove();
        app.workspace.openLinkText(filename, "", false);
    } catch(e) {
        try {
            await app.vault.createFolder(folder);
            await app.vault.create(filename, content);
            overlay.remove();
            app.workspace.openLinkText(filename, "", false);
        } catch(e2) { alert("Error creating playlist: " + e2); }
    }
}
```
```dataviewjs
const allPages = window._toolsPages;
const getCover = window._toolsGetCover;
const createModal = window._toolsCreateModal;
const savePlaylistNote = window._toolsSavePlaylist;
const PLAYLIST_VIEW = "00 Dashboard/_scripts/playlist";

function buildPlaylistNote(name, tagsArray, pages) {
    const tags = Array.from(new Set(tagsArray)).sort((a,b) => a.localeCompare(b, undefined, {sensitivity:"base"}));
    const date = new Date().toISOString().split("T")[0];
    return `# ${name}
**Created:** ${date} | **Tags:** ${tags.join(", ")} | **Albums:** ${pages.length}

\`\`\`dataviewjs
const TAGS = ${JSON.stringify(tags)};
await dv.view("${PLAYLIST_VIEW}", { tags: TAGS });
\`\`\`
`;
}

function buildAlbumPlaylistNote(name, pages) {
    const ids = pages.map(p => p.tidal_id);
    const date = new Date().toISOString().split("T")[0];
    return `# ${name}
**Created:** ${date} | **Albums:** ${pages.length}

\`\`\`dataviewjs
const ALBUM_IDS = ${JSON.stringify(ids)};
await dv.view("${PLAYLIST_VIEW}", { ids: ALBUM_IDS });
\`\`\`
`;
}

function openPlaylistPicker() {
    const { overlay, body } = createModal("🎵 Create Playlist");
    const subtitle = body.createEl("div");
    subtitle.textContent = "How would you like to build your playlist?";
    subtitle.style.cssText = "color:#aaa; font-size:14px; margin-bottom:24px;";
    const optionsCol = body.createEl("div");
    optionsCol.style.cssText = "display:flex; flex-direction:column; gap:16px;";
    const options = [
        { icon: "🏷", name: "By Tag", desc: "Select genres and tags to include all matching albums", action: () => { overlay.remove(); openPlaylistByTag(); } },
        { icon: "💿", name: "By Album Title", desc: "Search and hand-pick specific albums one by one", action: () => { overlay.remove(); openPlaylistByAlbum(); } },
    ];
    for (let opt of options) {
        const card = optionsCol.createEl("div");
        card.style.cssText = "background:#222; border:1px solid #333; border-radius:14px; padding:22px 20px; cursor:pointer; display:flex; align-items:center; gap:18px;";
        card.onclick = opt.action;
        const icon = card.createEl("div"); icon.textContent = opt.icon; icon.style.cssText = "font-size:36px; flex-shrink:0;";
        const text = card.createEl("div");
        const name = text.createEl("div"); name.textContent = opt.name; name.style.cssText = "color:#fff; font-size:17px; font-weight:bold; margin-bottom:4px;";
        const desc = text.createEl("div"); desc.textContent = opt.desc; desc.style.cssText = "color:#666; font-size:13px; line-height:1.4;";
    }
}

async function openPlaylistByTag() {
    const { overlay, body } = createModal("🏷 Create Playlist by Tag");
    // Categories come from _scripts/tags.json, so they always use the same tag names as the albums.
    const tagCounts = new Map();
    for (let page of allPages) {
        if (!page.tags) continue;
        for (let t of (Array.isArray(page.tags) ? page.tags : [page.tags])) {
            const tag = String(t).replace(/^#/, "");
            tagCounts.set(tag, (tagCounts.get(tag) || 0) + 1);
        }
    }
    const tagSet = new Set(tagCounts.keys());
    const byLower = new Map(Array.from(tagSet).map(t => [t.toLowerCase(), t]));
    let ruleCategories = {};
    try {
        ruleCategories = JSON.parse(await app.vault.adapter.read("_scripts/tags.json")).categories || {};
    } catch (e) {
        console.error("Could not read _scripts/tags.json", e);
    }
    const tagCategories = {};
    const categorized = new Set();
    for (const [cat, list] of Object.entries(ruleCategories)) {
        const present = list.map(t => byLower.get(String(t).toLowerCase())).filter(Boolean);
        present.forEach(t => categorized.add(t));
        if (present.length) tagCategories[cat] = present.sort((x, y) => x.localeCompare(y));
    }
    const otherTags = Array.from(tagSet).filter(t => !categorized.has(t)).sort((x, y) => x.localeCompare(y));
    if (otherTags.length) tagCategories["Other"] = Array.from(new Set([...(tagCategories["Other"] || []), ...otherTags])).sort((x, y) => x.localeCompare(y));
    let selectedTags = new Set();
    let matchMode = "any";
    let activeCategory = "All";

    const nameRow = body.createEl("div"); nameRow.style.cssText = "display:flex; align-items:center; gap:12px; margin-bottom:16px;";
    const nameLabel = nameRow.createEl("label"); nameLabel.textContent = "Name:"; nameLabel.style.cssText = "color:#aaa; font-size:14px; white-space:nowrap;";
    const nameInput = nameRow.createEl("input"); nameInput.type = "text"; nameInput.value = "My Playlist"; nameInput.style.cssText = "flex:1; padding:10px 12px; background:#222; border:1px solid #444; border-radius:8px; color:#fff; font-size:16px;";

    const matchRow = body.createEl("div"); matchRow.style.cssText = "display:flex; gap:10px; align-items:center; margin-bottom:14px;";
    const matchLabel = matchRow.createEl("div"); matchLabel.textContent = "Match:"; matchLabel.style.cssText = "color:#aaa; font-size:14px;";
    const anyBtn = matchRow.createEl("button"); anyBtn.textContent = "Any (OR)"; anyBtn.style.cssText = "flex:1; padding:10px; border-radius:20px; border:1px solid #7c3aed; background:#7c3aed; color:#fff; font-size:14px; cursor:pointer;";
    const allBtn = matchRow.createEl("button"); allBtn.textContent = "All (AND)"; allBtn.style.cssText = "flex:1; padding:10px; border-radius:20px; border:1px solid #444; background:#222; color:#aaa; font-size:14px; cursor:pointer;";
    anyBtn.onclick = () => { matchMode = "any"; anyBtn.style.cssText = "flex:1; padding:10px; border-radius:20px; border:1px solid #7c3aed; background:#7c3aed; color:#fff; font-size:14px; cursor:pointer;"; allBtn.style.cssText = "flex:1; padding:10px; border-radius:20px; border:1px solid #444; background:#222; color:#aaa; font-size:14px; cursor:pointer;"; renderPreview(); };
    allBtn.onclick = () => { matchMode = "all"; allBtn.style.cssText = "flex:1; padding:10px; border-radius:20px; border:1px solid #7c3aed; background:#7c3aed; color:#fff; font-size:14px; cursor:pointer;"; anyBtn.style.cssText = "flex:1; padding:10px; border-radius:20px; border:1px solid #444; background:#222; color:#aaa; font-size:14px; cursor:pointer;"; renderPreview(); };

    const searchInput = body.createEl("input"); searchInput.type = "text"; searchInput.placeholder = "Search tags..."; searchInput.style.cssText = "width:100%; padding:10px 12px; background:#222; border:1px solid #444; border-radius:8px; color:#fff; font-size:15px; box-sizing:border-box; margin-bottom:12px;";
    const catRow = body.createEl("div"); catRow.style.cssText = "display:flex; flex-wrap:wrap; gap:8px; margin-bottom:12px;";
    function renderCatPills() {
        catRow.innerHTML = "";
        for (let cat of ["All", ...Object.keys(tagCategories)]) {
            const pill = catRow.createEl("button"); pill.textContent = cat;
            pill.style.cssText = `padding:8px 14px; border-radius:20px; font-size:13px; cursor:pointer; border:1px solid ${activeCategory===cat?"#7c3aed":"#444"}; background:${activeCategory===cat?"#7c3aed":"#222"}; color:${activeCategory===cat?"#fff":"#aaa"};`;
            pill.onclick = () => { activeCategory = cat; renderCatPills(); renderTagGrid(); };
        }
    }
    renderCatPills();
    const tagGrid = body.createEl("div"); tagGrid.style.cssText = "display:flex; flex-wrap:wrap; gap:8px; margin-bottom:16px; max-height:180px; overflow-y:auto; padding:4px;";
    function getVisibleTags() {
        const search = searchInput.value.toLowerCase();
        let tags = activeCategory === "All" ? Array.from(tagSet).sort((x, y) => x.localeCompare(y)) : (tagCategories[activeCategory] || []);
        if (search) tags = tags.filter(t => t.toLowerCase().includes(search));
        return tags;
    }
    function renderTagGrid() {
        tagGrid.innerHTML = "";
        for (let tag of getVisibleTags()) {
            const btn = tagGrid.createEl("button"); btn.textContent = `${tag} · ${tagCounts.get(tag) || 0}`;
            btn.style.cssText = `padding:8px 14px; border-radius:20px; font-size:13px; cursor:pointer; border:1px solid ${selectedTags.has(tag)?"#7c3aed":"#444"}; background:${selectedTags.has(tag)?"#7c3aed":"#222"}; color:${selectedTags.has(tag)?"#fff":"#aaa"};`;
            btn.onclick = () => { selectedTags.has(tag) ? selectedTags.delete(tag) : selectedTags.add(tag); renderTagGrid(); renderPreview(); };
        }
    }
    renderTagGrid();
    searchInput.addEventListener("input", renderTagGrid);

    const selectedRow = body.createEl("div"); selectedRow.style.cssText = "margin-bottom:12px;";
    const previewLabel = body.createEl("div"); previewLabel.style.cssText = "color:#aaa; font-size:13px; margin-bottom:8px;";
    const previewGrid = body.createEl("div"); previewGrid.style.cssText = "display:flex; flex-wrap:wrap; gap:10px; margin-bottom:16px; max-height:200px; overflow-y:auto;";

    function getMatchingPages() {
        if (selectedTags.size === 0) return [];
        const selected = Array.from(selectedTags);
        return allPages.where(p => {
            if (!p.tags) return false;
            const pageTags = p.tags.map(t => String(t).replace(/^#/,"").toLowerCase());
            return matchMode === "any" ? selected.some(tag => pageTags.includes(tag.toLowerCase())) : selected.every(tag => pageTags.includes(tag.toLowerCase()));
        }).array().sort((a,b) => (a.artist||"").localeCompare(b.artist||""));
    }
    function renderPreview() {
        previewGrid.innerHTML = ""; selectedRow.innerHTML = "";
        if (selectedTags.size > 0) {
            const sl = selectedRow.createEl("div"); sl.textContent = "Selected:"; sl.style.cssText = "color:#aaa; font-size:13px; margin-bottom:6px;";
            const sp = selectedRow.createEl("div"); sp.style.cssText = "display:flex; flex-wrap:wrap; gap:6px; margin-bottom:10px;";
            for (let tag of selectedTags) { const pill = sp.createEl("span"); pill.textContent = tag+" ✕"; pill.style.cssText = "padding:6px 12px; background:#7c3aed; border-radius:20px; color:#fff; font-size:13px; cursor:pointer;"; pill.onclick = () => { selectedTags.delete(tag); renderTagGrid(); renderPreview(); }; }
        }
        const matches = getMatchingPages();
        previewLabel.textContent = selectedTags.size === 0 ? "Select tags above to preview" : `${matches.length} albums match`;
        for (let page of matches) {
            const card = previewGrid.createEl("div"); card.style.cssText = "width:90px; background:#111; border-radius:8px; overflow:hidden; cursor:pointer;";
            card.onclick = () => app.workspace.openLinkText(page.file.path, "", false);
            const img = card.createEl("img"); img.style.cssText = "width:90px; height:90px; object-fit:cover; display:block;";
            const coverFile = getCover(page);
            if (coverFile) img.src = app.vault.getResourcePath(coverFile); else img.style.cssText += "background:#333;";
            const info = card.createEl("div"); info.style.cssText = "padding:4px 6px;";
            const t = info.createEl("div"); t.style.cssText = "color:#fff; font-size:9px; font-weight:bold; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;"; t.textContent = page.title || page.file.name;
            const a = info.createEl("div"); a.style.cssText = "color:#aaa; font-size:8px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;"; a.textContent = page.artist || "";
        }
    }
    renderPreview();

    const createBtn = body.createEl("button"); createBtn.textContent = "Create Playlist"; createBtn.style.cssText = "padding:14px 24px; background:#7c3aed; border:none; border-radius:12px; color:#fff; font-size:16px; font-weight:bold; cursor:pointer; width:100%; margin-top:8px;";
    createBtn.onclick = async () => {
        const matches = getMatchingPages();
        if (matches.length === 0) { alert("No albums match!"); return; }
        const name = nameInput.value.trim() || "My Playlist";
        await savePlaylistNote(name, buildPlaylistNote(name, Array.from(selectedTags), matches), overlay);
    };
}

function openPlaylistByAlbum() {
    const { overlay, body } = createModal("💿 Create Playlist by Album");
    let selectedAlbums = new Map();

    const nameRow = body.createEl("div"); nameRow.style.cssText = "display:flex; align-items:center; gap:12px; margin-bottom:16px;";
    const nameLabel = nameRow.createEl("label"); nameLabel.textContent = "Name:"; nameLabel.style.cssText = "color:#aaa; font-size:14px; white-space:nowrap;";
    const nameInput = nameRow.createEl("input"); nameInput.type = "text"; nameInput.value = "My Playlist"; nameInput.style.cssText = "flex:1; padding:10px 12px; background:#222; border:1px solid #444; border-radius:8px; color:#fff; font-size:16px;";

    const searchInput = body.createEl("input"); searchInput.type = "text"; searchInput.placeholder = "Search albums by title or artist..."; searchInput.style.cssText = "width:100%; padding:10px 12px; background:#222; border:1px solid #444; border-radius:8px; color:#fff; font-size:15px; box-sizing:border-box; margin-bottom:10px;";
    const resultsLabel = body.createEl("div"); resultsLabel.style.cssText = "color:#aaa; font-size:13px; margin-bottom:8px;"; resultsLabel.textContent = "Search for albums to add...";
    const resultsGrid = body.createEl("div"); resultsGrid.style.cssText = "display:flex; flex-wrap:wrap; gap:10px; max-height:200px; overflow-y:auto; margin-bottom:16px; padding:4px;";

    function renderResults() {
        resultsGrid.innerHTML = "";
        const query = searchInput.value.toLowerCase().trim();
        if (!query) { resultsLabel.textContent = "Search for albums to add..."; return; }
        const results = allPages.where(p => (p.title||p.file.name||"").toLowerCase().includes(query) || (p.artist||"").toLowerCase().includes(query)).array().sort((a,b) => (a.artist||"").localeCompare(b.artist||""));
        resultsLabel.textContent = `${results.length} results — tap to add`;
        for (let page of results) {
            const isSelected = selectedAlbums.has(page.tidal_id);
            const card = resultsGrid.createEl("div"); card.style.cssText = `width:100px; background:${isSelected?"#2d1f4e":"#111"}; border-radius:8px; overflow:hidden; cursor:pointer; border:2px solid ${isSelected?"#7c3aed":"transparent"};`;
            const img = card.createEl("img"); img.style.cssText = "width:100px; height:100px; object-fit:cover; display:block;";
            const coverFile = getCover(page);
            if (coverFile) img.src = app.vault.getResourcePath(coverFile); else img.style.cssText += "background:#333;";
            const info = card.createEl("div"); info.style.cssText = "padding:5px 7px;";
            const t = info.createEl("div"); t.style.cssText = "color:#fff; font-size:10px; font-weight:bold; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;"; t.textContent = page.title || page.file.name;
            const a = info.createEl("div"); a.style.cssText = "color:#aaa; font-size:9px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;"; a.textContent = page.artist || "";
            card.onclick = () => { selectedAlbums.has(page.tidal_id) ? selectedAlbums.delete(page.tidal_id) : selectedAlbums.set(page.tidal_id, page); renderResults(); renderSelected(); };
        }
    }
    searchInput.addEventListener("input", renderResults);

    const selectedLabel = body.createEl("div"); selectedLabel.style.cssText = "color:#aaa; font-size:13px; margin-bottom:8px;";
    const selectedGrid = body.createEl("div"); selectedGrid.style.cssText = "display:flex; flex-wrap:wrap; gap:10px; max-height:200px; overflow-y:auto; margin-bottom:16px; padding:4px;";

    function renderSelected() {
        selectedGrid.innerHTML = "";
        selectedLabel.textContent = selectedAlbums.size === 0 ? "No albums selected yet" : `${selectedAlbums.size} albums — tap to remove`;
        for (let [id, page] of selectedAlbums) {
            const card = selectedGrid.createEl("div"); card.style.cssText = "width:100px; background:#2d1f4e; border-radius:8px; overflow:hidden; cursor:pointer; border:2px solid #7c3aed; position:relative;";
            const img = card.createEl("img"); img.style.cssText = "width:100px; height:100px; object-fit:cover; display:block; opacity:0.8;";
            const coverFile = getCover(page);
            if (coverFile) img.src = app.vault.getResourcePath(coverFile); else img.style.cssText += "background:#333;";
            const rb = card.createEl("div"); rb.textContent = "✕"; rb.style.cssText = "position:absolute; top:5px; right:5px; background:rgba(0,0,0,0.8); color:#fff; border-radius:50%; width:22px; height:22px; display:flex; align-items:center; justify-content:center; font-size:12px;";
            const info = card.createEl("div"); info.style.cssText = "padding:5px 7px;";
            const t = info.createEl("div"); t.style.cssText = "color:#fff; font-size:10px; font-weight:bold; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;"; t.textContent = page.title || page.file.name;
            const a = info.createEl("div"); a.style.cssText = "color:#aaa; font-size:9px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;"; a.textContent = page.artist || "";
            card.onclick = () => { selectedAlbums.delete(id); renderResults(); renderSelected(); };
        }
    }
    renderSelected();

    const createBtn = body.createEl("button"); createBtn.textContent = "Create Playlist"; createBtn.style.cssText = "padding:14px 24px; background:#7c3aed; border:none; border-radius:12px; color:#fff; font-size:16px; font-weight:bold; cursor:pointer; width:100%; margin-top:8px;";
    createBtn.onclick = async () => {
        if (selectedAlbums.size === 0) { alert("No albums selected!"); return; }
        const name = nameInput.value.trim() || "My Playlist";
        await savePlaylistNote(name, buildAlbumPlaylistNote(name, Array.from(selectedAlbums.values())), overlay);
    };
}

window._toolsOpenPlaylistPicker = openPlaylistPicker;
```
```dataviewjs
const allPages = window._toolsPages;
const getCover = window._toolsGetCover;
const createModal = window._toolsCreateModal;

function openAddToFavorites() {
    const { body } = createModal("Add to Favorites");
    const subtitle = body.createEl("div"); subtitle.textContent = "Tap an album to toggle its Favorite tag."; subtitle.style.cssText = "color:#aaa; font-size:13px; margin-bottom:16px;";
    const searchInput = body.createEl("input"); searchInput.type = "text"; searchInput.placeholder = "Search albums by title or artist..."; searchInput.style.cssText = "width:100%; padding:10px 12px; background:#222; border:1px solid #444; border-radius:8px; color:#fff; font-size:15px; box-sizing:border-box; margin-bottom:10px;";
    const resultsLabel = body.createEl("div"); resultsLabel.style.cssText = "color:#aaa; font-size:13px; margin-bottom:8px;";
    const resultsGrid = body.createEl("div"); resultsGrid.style.cssText = "display:flex; flex-wrap:wrap; gap:10px; overflow-y:auto; margin-bottom:16px; padding:4px;";
    const statusEl = body.createEl("div"); statusEl.style.cssText = "font-size:13px; min-height:20px; text-align:center; padding:4px 0;";
    const FAVE_TAG = "Favorite";
    function isFavorited(page) { return page.tags && page.tags.some(t => String(t).replace(/^#/,"") === FAVE_TAG); }
    async function toggleFavorite(page) {
        const file = app.vault.getAbstractFileByPath(page.file.path);
        if (!file) { statusEl.textContent = "Could not find file."; return; }
        try {
            await app.fileManager.processFrontMatter(file, (fm) => {
                if (!fm.tags) fm.tags = [];
                if (typeof fm.tags === "string") fm.tags = [fm.tags];
                const idx = fm.tags.findIndex(t => String(t).replace(/^#/,"") === FAVE_TAG);
                if (idx >= 0) { fm.tags.splice(idx, 1); statusEl.style.color = "#aaa"; statusEl.textContent = `Removed: ${page.title||page.file.name}`; }
                else { fm.tags.unshift(FAVE_TAG); statusEl.style.color = "#f59e0b"; statusEl.textContent = `Added to Favorites: ${page.title||page.file.name}`; }
            });
        } catch(e) { statusEl.style.color = "#ef4444"; statusEl.textContent = "Error: " + e.message; }
        setTimeout(() => renderResults(), 300);
    }
    function renderResults() {
        resultsGrid.innerHTML = "";
        const query = searchInput.value.toLowerCase().trim();
        const freshPages = dv.pages().where(p => p.tidal_id);
        let results;
        if (!query) {
            results = freshPages.where(p => isFavorited(p)).array().sort((a,b) => (a.artist||"").localeCompare(b.artist||""));
            resultsLabel.textContent = results.length > 0 ? `${results.length} favorited albums — tap to remove` : "No favorites yet. Search to add some.";
        } else {
            results = freshPages.where(p => (p.title||p.file.name||"").toLowerCase().includes(query) || (p.artist||"").toLowerCase().includes(query)).array().sort((a,b) => (a.artist||"").localeCompare(b.artist||""));
            resultsLabel.textContent = `${results.length} results — tap to toggle`;
        }
        for (let page of results) {
            const favorited = isFavorited(page);
            const card = resultsGrid.createEl("div"); card.style.cssText = `width:110px; background:${favorited?"#2d1f4e":"#111"}; border-radius:8px; overflow:hidden; cursor:pointer; border:2px solid ${favorited?"#7c3aed":"transparent"}; position:relative;`;
            const badge = card.createEl("div"); badge.textContent = favorited?"★":"☆"; badge.style.cssText = `position:absolute; top:5px; left:5px; background:rgba(0,0,0,0.75); color:${favorited?"#f59e0b":"#666"}; border-radius:50%; width:22px; height:22px; display:flex; align-items:center; justify-content:center; font-size:13px; z-index:1;`;
            const img = card.createEl("img"); img.style.cssText = "width:110px; height:110px; object-fit:cover; display:block;";
            const coverFile = getCover(page);
            if (coverFile) img.src = app.vault.getResourcePath(coverFile); else img.style.cssText += "background:#333;";
            const info = card.createEl("div"); info.style.cssText = "padding:6px 8px;";
            const t = info.createEl("div"); t.style.cssText = "color:#fff; font-size:10px; font-weight:bold; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;"; t.textContent = page.title || page.file.name;
            const a = info.createEl("div"); a.style.cssText = "color:#aaa; font-size:9px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;"; a.textContent = page.artist || "";
            card.onclick = () => toggleFavorite(page);
            resultsGrid.appendChild(card);
        }
    }
    searchInput.addEventListener("input", renderResults);
    renderResults();
    setTimeout(() => searchInput.focus(), 100);
}

function openRecentlyAdded() {
    const { body } = createModal("🕐 Recently Added");
    const pages = allPages.array().sort((a,b) => (b.file.ctime||0)-(a.file.ctime||0)).slice(0,50);
    const grid = body.createEl("div"); grid.style.cssText = "display:flex; flex-wrap:wrap; gap:12px;";
    for (let page of pages) {
        const card = grid.createEl("div"); card.style.cssText = "width:110px; background:#111; border-radius:10px; overflow:hidden; cursor:pointer;";
        card.onclick = () => app.workspace.openLinkText(page.file.path, "", false);
        const img = card.createEl("img"); img.style.cssText = "width:110px; height:110px; object-fit:cover; display:block;";
        const coverFile = getCover(page);
        if (coverFile) img.src = app.vault.getResourcePath(coverFile); else img.style.cssText += "background:#333;";
        const info = card.createEl("div"); info.style.cssText = "padding:7px 8px;";
        const t = info.createEl("div"); t.style.cssText = "color:#fff; font-size:11px; font-weight:bold; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;"; t.textContent = page.title || page.file.name;
        const a = info.createEl("div"); a.style.cssText = "color:#aaa; font-size:10px; margin-top:2px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;"; a.textContent = page.artist || "";
        const d = info.createEl("div"); d.style.cssText = "color:#555; font-size:9px; margin-top:2px;"; d.textContent = page.file.ctime ? new Date(page.file.ctime).toLocaleDateString() : "";
    }
}

function openSearchAlbums() {
    const { body } = createModal("🔍 Search Albums");
    const searchInput = body.createEl("input"); searchInput.type = "text"; searchInput.placeholder = "Search by title, artist, year or tag..."; searchInput.style.cssText = "width:100%; padding:10px 14px; background:#222; border:1px solid #444; border-radius:8px; color:#fff; font-size:15px; box-sizing:border-box; margin-bottom:10px;";
    const resultsLabel = body.createEl("div"); resultsLabel.style.cssText = "color:#666; font-size:13px; margin-bottom:10px;"; resultsLabel.textContent = "Start typing to search...";
    const grid = body.createEl("div"); grid.style.cssText = "display:flex; flex-wrap:wrap; gap:12px;";
    function doSearch() {
        grid.innerHTML = "";
        const query = searchInput.value.toLowerCase().trim();
        if (!query) { resultsLabel.textContent = "Start typing to search..."; return; }
        const results = allPages.where(p => (p.title||p.file.name||"").toLowerCase().includes(query) || (p.artist||"").toLowerCase().includes(query) || String(p.year||"").includes(query) || (p.tags && p.tags.some(t => String(t).toLowerCase().includes(query)))).array().sort((a,b) => (a.artist||"").localeCompare(b.artist||""));
        resultsLabel.textContent = `${results.length} results`;
        for (let page of results) {
            const card = grid.createEl("div"); card.style.cssText = "width:110px; background:#111; border-radius:10px; overflow:hidden; cursor:pointer;";
            card.onclick = () => app.workspace.openLinkText(page.file.path, "", false);
            const img = card.createEl("img"); img.style.cssText = "width:110px; height:110px; object-fit:cover; display:block;";
            const coverFile = getCover(page);
            if (coverFile) img.src = app.vault.getResourcePath(coverFile); else img.style.cssText += "background:#333;";
            const info = card.createEl("div"); info.style.cssText = "padding:7px 8px;";
            const t = info.createEl("div"); t.style.cssText = "color:#fff; font-size:11px; font-weight:bold; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;"; t.textContent = page.title || page.file.name;
            const a = info.createEl("div"); a.style.cssText = "color:#aaa; font-size:10px; margin-top:2px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;"; a.textContent = page.artist || "";
            const y = info.createEl("div"); y.style.cssText = "color:#555; font-size:9px; margin-top:2px;"; y.textContent = page.year || "";
        }
    }
    searchInput.addEventListener("input", doSearch);
    setTimeout(() => searchInput.focus(), 100);
}

window._toolsOpenFavorites = openAddToFavorites;
window._toolsOpenRecent = openRecentlyAdded;
window._toolsOpenSearch = openSearchAlbums;
```
```dataviewjs
const allPages = window._toolsPages;
const getCover = window._toolsGetCover;
const createModal = window._toolsCreateModal;

function openUntagged() {
    const { body } = createModal("🏷 Untagged Albums");

    const freshPages = dv.pages().where(p => p.tidal_id);
    const untagged = freshPages.where(p =>
        !p.tags || p.tags.length === 0 ||
        (Array.isArray(p.tags) && p.tags.every(t => !String(t).trim()))
    ).array().sort((a,b) => (a.artist||"").localeCompare(b.artist||""));

    const countEl = body.createEl("div");
    countEl.style.cssText = "color:#aaa; font-size:13px; margin-bottom:16px;";
    countEl.textContent = untagged.length === 0 ? "🎉 All albums are tagged!" : `${untagged.length} albums without tags`;

    if (untagged.length === 0) return;

    const searchInput = body.createEl("input");
    searchInput.type = "text";
    searchInput.placeholder = "Search by title or artist...";
    searchInput.style.cssText = "width:100%; padding:10px 12px; background:#222; border:1px solid #444; border-radius:8px; color:#fff; font-size:15px; box-sizing:border-box; margin-bottom:12px;";

    const grid = body.createEl("div");
    grid.style.cssText = "display:flex; flex-wrap:wrap; gap:12px;";

    function renderGrid() {
        grid.innerHTML = "";
        const query = searchInput.value.toLowerCase().trim();
        const results = query
            ? untagged.filter(p => (p.title||p.file.name||"").toLowerCase().includes(query) || (p.artist||"").toLowerCase().includes(query))
            : untagged;

        countEl.textContent = `${results.length} of ${untagged.length} untagged albums shown`;

        for (let page of results) {
            const card = grid.createEl("div");
            card.style.cssText = "width:110px; background:#111; border-radius:10px; overflow:hidden; cursor:pointer;";
            card.onclick = () => app.workspace.openLinkText(page.file.path, "", false);
            const img = card.createEl("img");
            img.style.cssText = "width:110px; height:110px; object-fit:cover; display:block;";
            const coverFile = getCover(page);
            if (coverFile) img.src = app.vault.getResourcePath(coverFile); else img.style.cssText += "background:#333;";
            const info = card.createEl("div");
            info.style.cssText = "padding:7px 8px;";
            const t = info.createEl("div");
            t.style.cssText = "color:#fff; font-size:11px; font-weight:bold; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;";
            t.textContent = page.title || page.file.name;
            const a = info.createEl("div");
            a.style.cssText = "color:#aaa; font-size:10px; margin-top:2px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;";
            a.textContent = page.artist || "";
        }
    }

    searchInput.addEventListener("input", renderGrid);
    renderGrid();
}

window._toolsOpenUntagged = openUntagged;
```
```dataviewjs
const ALBUM_VIEW = "_scripts/album";
const createModal = window._toolsCreateModal;

function convertAlbumText(text) {
    text = text.replace(/\r\n/g, "\n");
    const fm = text.match(/^---\n[\s\S]*?\n---\n?/);
    if (!fm) return { status: "skip", reason: "no frontmatter" };
    const rest = text.slice(fm[0].length);
    if (rest.includes(`dv.view("${ALBUM_VIEW}")`)) return { status: "done" };
    const lines = rest.split("\n");
    const start = lines.findIndex(l => /^\|\s*#\s*\|/.test(l));
    if (start < 0) return { status: "skip", reason: "no tracklist table" };
    let end = start;
    while (end < lines.length && lines[end].trim().startsWith("|")) end++;
    const table = lines.slice(start, end).join("\n");
    const after = lines.slice(end).join("\n").trim();
    const body = `${fm[0].trimEnd()}\n\n\`\`\`dataviewjs\nawait dv.view("${ALBUM_VIEW}");\n\`\`\`\n\n${table}\n${after ? `\n${after}\n` : ""}`;
    return { status: "convert", body };
}

async function openConvertAlbums() {
    const { body } = createModal("🔄 Update Album Notes");
    const status = body.createEl("div");
    status.style.cssText = "color:#aaa; font-size:14px; margin-bottom:12px;";
    status.textContent = "Scanning album notes...";

    const pending = [], skipped = [];
    let total = 0;
    for (const p of dv.pages().where(p => p.tidal_id).array()) {
        total++;
        const file = app.vault.getAbstractFileByPath(p.file.path);
        if (!file) continue;
        const res = convertAlbumText(await app.vault.cachedRead(file));
        if (res.status === "convert") pending.push({ file, body: res.body });
        else if (res.status === "skip") skipped.push({ file, reason: res.reason });
    }

    if (pending.length === 0) {
        status.textContent = `All ${total} album notes are up to date.`;
    } else {
        status.textContent = `${pending.length} of ${total} album notes use the old format.`;
        const warn = body.createEl("div");
        warn.style.cssText = "color:#f59e0b; font-size:13px; margin-bottom:12px; line-height:1.4;";
        warn.textContent = "Converting replaces everything above each tracklist with the shared template. Frontmatter, the tracklist table, and anything below it are kept. Back up your album notes before the first run.";

        const list = body.createEl("div");
        list.style.cssText = "max-height:180px; overflow-y:auto; background:#111; border-radius:8px; padding:8px 12px; margin-bottom:12px; font-size:12px; color:#ccc;";
        for (const { file } of pending) list.createEl("div").textContent = file.basename;

        const details = body.createEl("details");
        details.style.cssText = "margin-bottom:16px; color:#aaa; font-size:12px;";
        details.createEl("summary").textContent = `Preview: ${pending[0].file.basename}`;
        const pre = details.createEl("pre");
        pre.style.cssText = "white-space:pre-wrap; background:#111; padding:10px; border-radius:8px; max-height:200px; overflow-y:auto;";
        pre.textContent = pending[0].body;

        const btn = body.createEl("button");
        btn.textContent = `Convert ${pending.length} notes`;
        btn.style.cssText = "padding:14px; background:#7c3aed; border:none; border-radius:12px; color:#fff; font-size:16px; font-weight:bold; cursor:pointer; width:100%;";
        btn.onclick = async () => {
            btn.disabled = true;
            let done = 0;
            for (const { file } of pending) {
                await app.vault.process(file, text => {
                    const res = convertAlbumText(text);
                    return res.status === "convert" ? res.body : text;
                });
                done++;
                btn.textContent = `Converting... ${done} / ${pending.length}`;
            }
            btn.textContent = `Done — converted ${done} notes`;
            btn.style.background = "#16a34a";
        };
    }

    if (skipped.length > 0) {
        const sk = body.createEl("div");
        sk.style.cssText = "margin-top:16px; color:#ef4444; font-size:12px;";
        sk.createEl("div").textContent = `${skipped.length} skipped (fix by hand):`;
        for (const { file, reason } of skipped) sk.createEl("div").textContent = `• ${file.basename} — ${reason}`;
    }
}

window._toolsOpenConvertAlbums = openConvertAlbums;
```

```dataviewjs
const ICON_FOLDER = "_tools/icons";
const MEDIA_HEIGHT = 130;
const MEDIA_FIT = "cover";
const ANIMATE_ON_HOVER = false;

const tools = [
    { gif: "library.gif",   name: "Library", action: () => app.workspace.openLinkText("00 Dashboard/Library", "", false) },
    { gif: "playlist.jpg",  name: "Create Playlist", action: () => window._toolsOpenPlaylistPicker() },
    { gif: "favorite.gif", name: "Favorites", action: () => window._toolsOpenFavorites() },
    { gif: "recent.gif",    name: "Recently Added", action: () => window._toolsOpenRecent() },
    { gif: "search.gif",    name: "Search Albums", action: () => window._toolsOpenSearch() },
    { gif: "untagged.gif",  name: "Untagged Albums", action: () => window._toolsOpenUntagged() },
    { gif: "update.gif",    name: "Update Albums", action: () => window._toolsOpenConvertAlbums() },
];
function gifSrc(name) {
    if (!name) return null;
    if (/^https?:\/\//.test(name)) return name;
    const f = app.vault.getAbstractFileByPath(`${ICON_FOLDER}/${name}`);
    return f ? app.vault.getResourcePath(f) : null;
}

function renderMedia(card, tool) {
    const wrap = card.createDiv();
    wrap.style.cssText = `position:relative; width:100%; height:${MEDIA_HEIGHT}px; background:#111; overflow:hidden;`;
    const src = gifSrc(tool.gif);
    if (!src) return;

    const fit = `width:100%; height:100%; object-fit:${MEDIA_FIT}; display:block;`;
    const img = wrap.createEl("img");
    img.style.cssText = fit;

    if (ANIMATE_ON_HOVER && /\.(gif|webp)(\?|$)/i.test(tool.gif)) {
        const canvas = wrap.createEl("canvas");
        canvas.style.cssText = `position:absolute; inset:0; ${fit}`;
        img.style.visibility = "hidden";
        img.onload = () => {
            canvas.width = img.naturalWidth;
            canvas.height = img.naturalHeight;
            canvas.getContext("2d").drawImage(img, 0, 0);
        };
        card.addEventListener("mouseenter", () => { canvas.style.visibility = "hidden"; img.style.visibility = "visible"; });
        card.addEventListener("mouseleave", () => { canvas.style.visibility = "visible"; img.style.visibility = "hidden"; });
    }

    img.src = src;
}

const hub = dv.container.createEl("div");
hub.style.cssText = "display:grid; grid-template-columns: repeat(2, 1fr); gap:14px; padding:10px 0;";

for (let tool of tools) {
    const card = hub.createEl("div");
    card.style.cssText = "background:#1a1a1a; border-radius:16px; overflow:hidden; cursor:pointer; box-shadow:0 4px 12px rgba(0,0,0,0.4); transition:transform 0.15s, background 0.15s;";
    card.addEventListener("mouseenter", () => { card.style.transform = "translateY(-2px)"; card.style.background = "#202020"; });
    card.addEventListener("mouseleave", () => { card.style.transform = ""; card.style.background = "#1a1a1a"; });
    card.onclick = tool.action;
    renderMedia(card, tool);
    const text = card.createDiv();
    text.style.cssText = "padding:12px 14px 14px; text-align:center;";
    const name = text.createEl("div"); name.textContent = tool.name; name.style.cssText = "color:#fff; font-size:15px; font-weight:bold;";
    if (tool.desc) { const desc = text.createEl("div"); desc.textContent = tool.desc; desc.style.cssText = "color:#666; font-size:11px; line-height:1.4; margin-top:4px;"; }
}
```