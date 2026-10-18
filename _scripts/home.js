// Home hub: the tool cards and every tool's pop-up, in one script.
// _tools/Home.md is just:  await dv.view("_scripts/home");
// Albums are read fresh each time a tool opens, so new imports show up without reopening Home.

const ICON_FOLDER = "_tools/icons";
const PLAYLIST_FOLDER = "00 Dashboard/Playlists";
const MEDIA_HEIGHT = 130;
const MEDIA_FIT = "cover";
const FAVE_TAG = "Favorite";

const TOOLS = [
    { gif: "library.gif",  name: "Library",         action: () => openNote("00 Dashboard/Library") },
    { gif: "playlist.jpg", name: "Create Playlist", action: () => openPlaylistPicker() },
    { gif: "favorite.gif", name: "Favorites",       action: () => openFavorites() },
    { gif: "recent.gif",   name: "Recently Added",  action: () => openRecentlyAdded() },
    { gif: "search.gif",   name: "Search Albums",   action: () => openSearch() },
    { gif: "untagged.gif", name: "Untagged Albums", action: () => openUntagged() },
];

// ── Album data ────────────────────────────────────────────
const albums = () => dv.pages().where(p => p.tidal_id).array();
const tagsOf = p => (Array.isArray(p.tags) ? p.tags : p.tags ? [p.tags] : [])
    .map(t => String(t).replace(/^#/, "").trim()).filter(Boolean);
const titleOf = p => p.title || p.file.name.replace(/\s\(\d{4}\)$/, "");
const byArtist = (a, b) => String(a.artist || "").localeCompare(String(b.artist || ""));
const byName = (a, b) => a.localeCompare(b, undefined, { sensitivity: "base" });
const matches = (p, q) => titleOf(p).toLowerCase().includes(q) || String(p.artist || "").toLowerCase().includes(q);
const openNote = path => app.workspace.openLinkText(path, "", false);

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

// 'added' = the day you favorited it on Tidal (set by _code/sync_tidal.py); file dates reset whenever git checks files out
function addedTime(p) {
    const v = p.added;
    if (v && v.toMillis) return v.toMillis();
    const t = v ? Date.parse(String(v)) : NaN;
    return isNaN(t) ? (+p.file.ctime || 0) : t;
}

// ── UI pieces ─────────────────────────────────────────────
const S = {
    input: "width:100%; padding:10px 12px; background:#222; border:1px solid #444; border-radius:8px; color:#fff; font-size:15px; box-sizing:border-box; margin-bottom:10px;",
    label: "color:#aaa; font-size:13px; margin-bottom:8px;",
    grid: "display:flex; flex-wrap:wrap; gap:10px; padding:4px;",
    pill: on => `padding:8px 14px; border-radius:20px; font-size:13px; cursor:pointer; border:1px solid ${on ? "#7c3aed" : "#444"}; background:${on ? "#7c3aed" : "#222"}; color:${on ? "#fff" : "#aaa"};`,
    bigBtn: "padding:14px 24px; background:#7c3aed; border:none; border-radius:12px; color:#fff; font-size:16px; font-weight:bold; cursor:pointer; width:100%; margin-top:8px;",
};

function createModal(title) {
    const overlay = document.body.createEl("div");
    overlay.style.cssText = "position:fixed; inset:0; background:rgba(0,0,0,0.85); z-index:9999; display:flex; align-items:flex-end; justify-content:center;";
    const modal = overlay.createEl("div");
    modal.style.cssText = "background:#1a1a1a; border-radius:20px 20px 0 0; width:100%; max-height:92vh; display:flex; flex-direction:column; box-shadow:0 -8px 40px rgba(0,0,0,0.8); overflow:hidden;";
    modal.createEl("div").style.cssText = "width:40px; height:4px; background:#444; border-radius:2px; margin:12px auto 0 auto; flex-shrink:0;";
    const header = modal.createEl("div");
    header.style.cssText = "display:flex; align-items:center; justify-content:space-between; padding:14px 20px; border-bottom:1px solid #333; flex-shrink:0;";
    const titleEl = header.createEl("div", { text: title });
    titleEl.style.cssText = "color:#fff; font-size:18px; font-weight:bold;";
    const closeBtn = header.createEl("button", { text: "✕" });
    closeBtn.style.cssText = "background:#333; border:none; border-radius:8px; color:#aaa; font-size:18px; width:40px; height:40px; cursor:pointer; flex-shrink:0;";
    const onKey = e => { if (e.key === "Escape") close(); };
    const close = () => { overlay.remove(); document.removeEventListener("keydown", onKey); };
    closeBtn.onclick = close;
    overlay.onclick = e => { if (e.target === overlay) close(); };
    document.addEventListener("keydown", onKey);
    const body = modal.createEl("div");
    body.style.cssText = "padding:16px 16px 32px 16px; overflow-y:auto; flex:1; -webkit-overflow-scrolling:touch;";
    return { body, close };
}

// One album tile, used by every tool. opts: size, sub (extra line), selected, badge, removable, onclick
function albumCard(parent, page, opts = {}) {
    const size = opts.size || 110;
    const card = parent.createEl("div");
    card.style.cssText = `width:${size}px; background:${opts.selected ? "#2d1f4e" : "#111"}; border-radius:10px; overflow:hidden; cursor:pointer; position:relative; border:2px solid ${opts.selected ? "#7c3aed" : "transparent"};`;
    card.onclick = opts.onclick || (() => {
        app.saveLocalStorage("music-album-from", { album: page.file.path, path: dv.current().file.path, name: "Home" });
        openNote(page.file.path);
    });
    if (opts.badge) {
        const b = card.createEl("div", { text: opts.badge.text });
        b.style.cssText = `position:absolute; top:5px; left:5px; background:rgba(0,0,0,0.75); color:${opts.badge.color}; border-radius:50%; width:22px; height:22px; display:flex; align-items:center; justify-content:center; font-size:13px; z-index:1;`;
    }
    if (opts.removable) {
        const x = card.createEl("div", { text: "✕" });
        x.style.cssText = "position:absolute; top:5px; right:5px; background:rgba(0,0,0,0.8); color:#fff; border-radius:50%; width:22px; height:22px; display:flex; align-items:center; justify-content:center; font-size:12px; z-index:1;";
    }
    const img = card.createEl("img");
    img.style.cssText = `width:${size}px; height:${size}px; object-fit:cover; display:block; background:#333; pointer-events:none; user-select:none; -webkit-user-drag:none;`;
    const cover = findCover(page);
    if (cover) img.src = app.vault.getResourcePath(cover);
    const info = card.createEl("div");
    info.style.cssText = "padding:6px 8px;";
    const line = "white-space:nowrap; overflow:hidden; text-overflow:ellipsis;";
    info.createEl("div", { text: titleOf(page) }).style.cssText = `color:#fff; font-size:11px; font-weight:bold; ${line}`;
    info.createEl("div", { text: String(page.artist || "") }).style.cssText = `color:#aaa; font-size:10px; margin-top:2px; ${line}`;
    if (opts.sub) info.createEl("div", { text: String(opts.sub) }).style.cssText = "color:#555; font-size:9px; margin-top:2px;";
    return card;
}

function nameField(body) {
    const row = body.createEl("div");
    row.style.cssText = "display:flex; align-items:center; gap:12px; margin-bottom:16px;";
    row.createEl("label", { text: "Name:" }).style.cssText = "color:#aaa; font-size:14px; white-space:nowrap;";
    const input = row.createEl("input", { type: "text", value: "My Playlist" });
    input.style.cssText = "flex:1; padding:10px 12px; background:#222; border:1px solid #444; border-radius:8px; color:#fff; font-size:16px;";
    return input;
}

function searchField(body, placeholder) {
    const input = body.createEl("input", { type: "text", placeholder });
    input.style.cssText = S.input;
    return input;
}

// ── Create Playlist ───────────────────────────────────────
// Same note format as the existing playlists, so playlist.js's Edit Tags keeps working on them.
function playlistNote(kind, values) {
    const [constName, key] = kind === "tags" ? ["TAGS", "tags"] : ["ALBUM_IDS", "ids"];
    return "```dataviewjs\n" +
        `const ${constName} = ${JSON.stringify(values)};\n` +
        `await dv.view("_scripts/playlist", { ${key}: ${constName} });\n` +
        "```\n";
}

async function savePlaylist(name, content, close) {
    const safe = (name.trim() || "My Playlist").replace(/[\\/*?:"<>|#^[\]]/g, "-");
    try {
        if (!app.vault.getAbstractFileByPath(PLAYLIST_FOLDER)) await app.vault.createFolder(PLAYLIST_FOLDER);
        // Never overwrite an existing playlist: "Rock" becomes "Rock 2"
        let path = `${PLAYLIST_FOLDER}/${safe}.md`;
        for (let n = 2; app.vault.getAbstractFileByPath(path); n++) path = `${PLAYLIST_FOLDER}/${safe} ${n}.md`;
        await app.vault.create(path, content);
        close();
        openNote(path);
    } catch (e) {
        new Notice("Could not create playlist: " + e.message);
    }
}

function openPlaylistPicker() {
    const { body, close } = createModal("🎵 Create Playlist");
    body.createEl("div", { text: "How would you like to build your playlist?" }).style.cssText = "color:#aaa; font-size:14px; margin-bottom:24px;";
    const col = body.createEl("div");
    col.style.cssText = "display:flex; flex-direction:column; gap:16px;";
    const options = [
        { icon: "🏷", name: "By Tag", desc: "Select genres and tags to include all matching albums", open: openPlaylistByTag },
        { icon: "💿", name: "By Album Title", desc: "Search and hand-pick specific albums one by one", open: openPlaylistByAlbum },
    ];
    for (const opt of options) {
        const card = col.createEl("div");
        card.style.cssText = "background:#222; border:1px solid #333; border-radius:14px; padding:22px 20px; cursor:pointer; display:flex; align-items:center; gap:18px;";
        card.onclick = () => { close(); opt.open(); };
        card.createEl("div", { text: opt.icon }).style.cssText = "font-size:36px; flex-shrink:0;";
        const text = card.createEl("div");
        text.createEl("div", { text: opt.name }).style.cssText = "color:#fff; font-size:17px; font-weight:bold; margin-bottom:4px;";
        text.createEl("div", { text: opt.desc }).style.cssText = "color:#666; font-size:13px; line-height:1.4;";
    }
}

async function openPlaylistByTag() {
    const { body, close } = createModal("🏷 Create Playlist by Tag");
    const all = albums();
    const tagCounts = new Map();
    for (const p of all) for (const t of tagsOf(p)) tagCounts.set(t, (tagCounts.get(t) || 0) + 1);
    const allTags = Array.from(tagCounts.keys()).sort(byName);
    const byLower = new Map(allTags.map(t => [t.toLowerCase(), t]));

    // Categories come from _scripts/tags.json, so they always use the same tag names as the albums.
    let rules = {};
    try { rules = JSON.parse(await app.vault.adapter.read("_scripts/tags.json")).categories || {}; }
    catch (e) { console.error("Could not read _scripts/tags.json", e); }
    const categories = {};
    const categorized = new Set();
    for (const [cat, list] of Object.entries(rules)) {
        const present = list.map(t => byLower.get(String(t).toLowerCase())).filter(Boolean);
        present.forEach(t => categorized.add(t));
        if (present.length) categories[cat] = Array.from(new Set(present)).sort(byName);
    }
    const other = allTags.filter(t => !categorized.has(t));
    if (other.length) categories["Other"] = Array.from(new Set([...(categories["Other"] || []), ...other])).sort(byName);

    const selected = new Set();
    let mode = "any";
    let activeCat = "All";

    const nameInput = nameField(body);
    const matchRow = body.createEl("div");
    matchRow.style.cssText = "display:flex; gap:10px; align-items:center; margin-bottom:14px;";
    matchRow.createEl("div", { text: "Match:" }).style.cssText = "color:#aaa; font-size:14px;";
    const modeBtns = { any: matchRow.createEl("button", { text: "Any (OR)" }), all: matchRow.createEl("button", { text: "All (AND)" }) };
    const paintModes = () => { for (const [m, b] of Object.entries(modeBtns)) b.style.cssText = S.pill(mode === m) + " flex:1; padding:10px;"; };
    for (const m of Object.keys(modeBtns)) modeBtns[m].onclick = () => { mode = m; paintModes(); renderPreview(); };
    paintModes();

    const search = searchField(body, "Search tags...");
    const catRow = body.createEl("div");
    catRow.style.cssText = "display:flex; flex-wrap:wrap; gap:8px; margin-bottom:12px;";
    const tagGrid = body.createEl("div");
    tagGrid.style.cssText = "display:flex; flex-wrap:wrap; gap:8px; margin-bottom:16px; max-height:180px; overflow-y:auto; padding:4px;";
    const selectedRow = body.createEl("div");
    selectedRow.style.cssText = "margin-bottom:12px;";
    const previewLabel = body.createEl("div");
    previewLabel.style.cssText = S.label;
    const previewGrid = body.createEl("div");
    previewGrid.style.cssText = S.grid + " margin-bottom:16px; max-height:200px; overflow-y:auto;";

    function renderCats() {
        catRow.empty();
        for (const cat of ["All", ...Object.keys(categories)]) {
            const pill = catRow.createEl("button", { text: cat });
            pill.style.cssText = S.pill(activeCat === cat);
            pill.onclick = () => { activeCat = cat; renderCats(); renderTags(); };
        }
    }
    function renderTags() {
        tagGrid.empty();
        const q = search.value.toLowerCase();
        const list = (activeCat === "All" ? allTags : categories[activeCat] || []).filter(t => !q || t.toLowerCase().includes(q));
        for (const tag of list) {
            const btn = tagGrid.createEl("button", { text: `${tag} · ${tagCounts.get(tag) || 0}` });
            btn.style.cssText = S.pill(selected.has(tag));
            btn.onclick = () => { selected.has(tag) ? selected.delete(tag) : selected.add(tag); renderTags(); renderPreview(); };
        }
    }
    function matching() {
        if (!selected.size) return [];
        const want = Array.from(selected, t => t.toLowerCase());
        return all.filter(p => {
            const have = tagsOf(p).map(t => t.toLowerCase());
            return mode === "any" ? want.some(t => have.includes(t)) : want.every(t => have.includes(t));
        }).sort(byArtist);
    }
    function renderPreview() {
        previewGrid.empty();
        selectedRow.empty();
        if (selected.size) {
            selectedRow.createEl("div", { text: "Selected:" }).style.cssText = "color:#aaa; font-size:13px; margin-bottom:6px;";
            const row = selectedRow.createEl("div");
            row.style.cssText = "display:flex; flex-wrap:wrap; gap:6px; margin-bottom:10px;";
            for (const tag of selected) {
                const pill = row.createEl("span", { text: tag + " ✕" });
                pill.style.cssText = "padding:6px 12px; background:#7c3aed; border-radius:20px; color:#fff; font-size:13px; cursor:pointer;";
                pill.onclick = () => { selected.delete(tag); renderTags(); renderPreview(); };
            }
        }
        const found = matching();
        previewLabel.textContent = selected.size ? `${found.length} albums match` : "Select tags above to preview";
        for (const p of found) albumCard(previewGrid, p, { size: 90 });
    }
    search.addEventListener("input", renderTags);
    renderCats(); renderTags(); renderPreview();

    const createBtn = body.createEl("button", { text: "Create Playlist" });
    createBtn.style.cssText = S.bigBtn;
    createBtn.onclick = async () => {
        if (!matching().length) return new Notice("No albums match those tags.");
        // Tag playlists store tags, not albums, so they pick up new albums automatically.
        await savePlaylist(nameInput.value, playlistNote("tags", Array.from(selected).sort(byName)), close);
    };
}

function openPlaylistByAlbum() {
    const { body, close } = createModal("💿 Create Playlist by Album");
    const all = albums();
    const chosen = new Map();
    const nameInput = nameField(body);
    const search = searchField(body, "Search albums by title or artist...");
    const resultsLabel = body.createEl("div", { text: "Search for albums to add..." });
    resultsLabel.style.cssText = S.label;
    const resultsGrid = body.createEl("div");
    resultsGrid.style.cssText = S.grid + " max-height:200px; overflow-y:auto; margin-bottom:16px;";
    const chosenLabel = body.createEl("div");
    chosenLabel.style.cssText = S.label;
    const chosenGrid = body.createEl("div");
    chosenGrid.style.cssText = S.grid + " max-height:200px; overflow-y:auto; margin-bottom:16px;";

    const toggle = p => { const id = String(p.tidal_id); chosen.has(id) ? chosen.delete(id) : chosen.set(id, p); renderResults(); renderChosen(); };
    function renderResults() {
        resultsGrid.empty();
        const q = search.value.toLowerCase().trim();
        if (!q) { resultsLabel.textContent = "Search for albums to add..."; return; }
        const found = all.filter(p => matches(p, q)).sort(byArtist);
        resultsLabel.textContent = `${found.length} results — tap to add`;
        for (const p of found) albumCard(resultsGrid, p, { size: 100, selected: chosen.has(String(p.tidal_id)), onclick: () => toggle(p) });
    }
    function renderChosen() {
        chosenGrid.empty();
        chosenLabel.textContent = chosen.size ? `${chosen.size} albums — tap to remove` : "No albums selected yet";
        for (const p of chosen.values()) albumCard(chosenGrid, p, { size: 100, selected: true, removable: true, onclick: () => toggle(p) });
    }
    search.addEventListener("input", renderResults);
    renderChosen();

    const createBtn = body.createEl("button", { text: "Create Playlist" });
    createBtn.style.cssText = S.bigBtn;
    createBtn.onclick = async () => {
        if (!chosen.size) return new Notice("No albums selected.");
        await savePlaylist(nameInput.value, playlistNote("ids", Array.from(chosen.values(), p => p.tidal_id)), close);
    };
}

// ── Favorites ─────────────────────────────────────────────
function openFavorites() {
    const { body } = createModal("Favorites");
    body.createEl("div", { text: "Tap an album to toggle its Favorite tag." }).style.cssText = "color:#aaa; font-size:13px; margin-bottom:16px;";
    const search = searchField(body, "Search albums by title or artist...");
    const label = body.createEl("div");
    label.style.cssText = S.label;
    const grid = body.createEl("div");
    grid.style.cssText = S.grid + " margin-bottom:16px;";
    const status = body.createEl("div");
    status.style.cssText = "font-size:13px; min-height:20px; text-align:center; padding:4px 0;";
    const isFave = p => tagsOf(p).includes(FAVE_TAG);

    async function toggle(page) {
        const file = app.vault.getAbstractFileByPath(page.file.path);
        if (!file) return;
        try {
            await app.fileManager.processFrontMatter(file, fm => {
                const tags = (Array.isArray(fm.tags) ? fm.tags : fm.tags ? [fm.tags] : []).map(String);
                const i = tags.findIndex(t => t.replace(/^#/, "") === FAVE_TAG);
                if (i >= 0) tags.splice(i, 1); else tags.unshift(FAVE_TAG);
                fm.tags = tags;
                status.style.color = i >= 0 ? "#aaa" : "#f59e0b";
                status.textContent = `${i >= 0 ? "Removed" : "Added to Favorites"}: ${titleOf(page)}`;
            });
        } catch (e) { status.style.color = "#ef4444"; status.textContent = "Error: " + e.message; }
        setTimeout(render, 300); // give Dataview a moment to see the change
    }
    function render() {
        grid.empty();
        const q = search.value.toLowerCase().trim();
        const list = albums().filter(p => q ? matches(p, q) : isFave(p)).sort(byArtist);
        label.textContent = q ? `${list.length} results — tap to toggle`
            : list.length ? `${list.length} favorited albums — tap to remove` : "No favorites yet. Search to add some.";
        for (const p of list) {
            const fave = isFave(p);
            albumCard(grid, p, { selected: fave, badge: { text: fave ? "★" : "☆", color: fave ? "#f59e0b" : "#666" }, onclick: () => toggle(p) });
        }
    }
    search.addEventListener("input", render);
    render();
    setTimeout(() => search.focus(), 100);
}

// ── Recently Added / Search / Untagged ────────────────────
function openRecentlyAdded() {
    const { body } = createModal("🕐 Recently Added");
    const grid = body.createEl("div");
    grid.style.cssText = S.grid + " gap:12px;";
    for (const p of albums().sort((a, b) => addedTime(b) - addedTime(a)).slice(0, 50)) {
        const t = addedTime(p);
        albumCard(grid, p, { sub: t ? new Date(t).toLocaleDateString() : "" });
    }
}

function openSearch() {
    const { body } = createModal("🔍 Search Albums");
    const all = albums();
    const search = searchField(body, "Search by title, artist, year or tag...");
    const label = body.createEl("div", { text: "Start typing to search..." });
    label.style.cssText = S.label;
    const grid = body.createEl("div");
    grid.style.cssText = S.grid + " gap:12px;";
    search.addEventListener("input", () => {
        grid.empty();
        const q = search.value.toLowerCase().trim();
        if (!q) { label.textContent = "Start typing to search..."; return; }
        const found = all.filter(p => matches(p, q) || String(p.year || "").includes(q) || tagsOf(p).some(t => t.toLowerCase().includes(q))).sort(byArtist);
        label.textContent = `${found.length} results`;
        for (const p of found) albumCard(grid, p, { sub: p.year || "" });
    });
    setTimeout(() => search.focus(), 100);
}

function openUntagged() {
    const { body } = createModal("🏷 Untagged Albums");
    const untagged = albums().filter(p => !tagsOf(p).length).sort(byArtist);
    const count = body.createEl("div", { text: untagged.length ? `${untagged.length} albums without tags` : "🎉 All albums are tagged!" });
    count.style.cssText = "color:#aaa; font-size:13px; margin-bottom:16px;";
    if (!untagged.length) return;
    const search = searchField(body, "Search by title or artist...");
    const grid = body.createEl("div");
    grid.style.cssText = S.grid + " gap:12px;";
    const render = () => {
        grid.empty();
        const q = search.value.toLowerCase().trim();
        const list = q ? untagged.filter(p => matches(p, q)) : untagged;
        count.textContent = `${list.length} of ${untagged.length} untagged albums shown`;
        for (const p of list) albumCard(grid, p);
    };
    search.addEventListener("input", render);
    render();
}

// ── Hub ───────────────────────────────────────────────────
function iconSrc(name) {
    if (!name) return null;
    if (/^https?:\/\//.test(name)) return name;
    const f = app.vault.getAbstractFileByPath(`${ICON_FOLDER}/${name}`);
    return f ? app.vault.getResourcePath(f) : null;
}

const hub = dv.container.createEl("div");
hub.style.cssText = "display:grid; grid-template-columns: repeat(2, 1fr); gap:14px; padding:10px 0;";
for (const tool of TOOLS) {
    const card = hub.createEl("div");
    card.style.cssText = "background:#1a1a1a; border-radius:16px; overflow:hidden; cursor:pointer; box-shadow:0 4px 12px rgba(0,0,0,0.4); transition:transform 0.15s, background 0.15s;";
    card.addEventListener("mouseenter", () => { card.style.transform = "translateY(-2px)"; card.style.background = "#202020"; });
    card.addEventListener("mouseleave", () => { card.style.transform = ""; card.style.background = "#1a1a1a"; });
    card.onclick = tool.action;
    const media = card.createEl("div");
    media.style.cssText = `width:100%; height:${MEDIA_HEIGHT}px; background:#111; overflow:hidden;`;
    const src = iconSrc(tool.gif);
    if (src) media.createEl("img", { attr: { src } }).style.cssText = `width:100%; height:100%; object-fit:${MEDIA_FIT}; display:block; pointer-events:none; user-select:none; -webkit-user-drag:none;`;
    const text = card.createEl("div");
    text.style.cssText = "padding:12px 14px 14px; text-align:center;";
    text.createEl("div", { text: tool.name }).style.cssText = "color:#fff; font-size:15px; font-weight:bold;";
}
