const TAGS = input.tags || null;
const ALBUM_IDS = input.ids || null;
const GENRE = !!input.genre; // genre pages: one tag, taken from the note's name, not editable

const seen = new Set();
const SORTED_TAGS = TAGS ? TAGS
    .filter(t => { const k = t.toLowerCase(); if (seen.has(k)) return false; seen.add(k); return true; })
    .sort((a,b) => a.localeCompare(b, undefined, {sensitivity:"base"})) : [];

// ── One-time indexes ──────────────────────────────────────
const allAlbums = dv.pages().where(p => p.tidal_id).array();
const byTag = new Map();
for (let p of allAlbums) {
    if (!p.tags) continue;
    const tags = Array.isArray(p.tags) ? p.tags : [p.tags];
    for (let t of tags) {
        const k = String(t).replace(/^#/, "").toLowerCase();
        if (!byTag.has(k)) byTag.set(k, []);
        byTag.get(k).push(p);
    }
}
const idSet = ALBUM_IDS ? new Set(ALBUM_IDS.map(String)) : null;
const idAlbums = idSet ? allAlbums.filter(p => idSet.has(String(p.tidal_id))) : [];


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

// ── Nav row ───────────────────────────────────────────────
const nav = dv.container.createEl("div");
nav.style.cssText = "display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;";

const backBtn = nav.createEl("a");
backBtn.textContent = "← Library";
backBtn.style.cssText = "display:inline-block; padding:10px 20px; background:#7c3aed; color:#fff; border-radius:10px; font-size:15px; font-weight:bold; text-decoration:none; cursor:pointer;";
backBtn.onclick = (e) => { e.preventDefault(); app.workspace.openLinkText("00 Dashboard/Library", "", false); };

const editBtn = nav.createEl("div");
editBtn.textContent = "Edit Tags";
editBtn.style.cssText = "padding:10px 20px; background:#1a1a1a; color:#fff; border-radius:10px; font-size:14px; font-weight:bold; cursor:pointer; box-shadow:0 4px 12px rgba(0,0,0,0.4);";
editBtn.onmouseenter = () => editBtn.style.background = "#222";
editBtn.onmouseleave = () => editBtn.style.background = "#1a1a1a";
if (!TAGS || GENRE) editBtn.style.display = "none";

editBtn.onclick = async () => {
    const file = app.vault.getAbstractFileByPath(dv.current().file.path);
    const content = await app.vault.read(file);

    const tagMatch = content.match(/const TAGS\s*=\s*(\[.*?\]);/s);
    if (!tagMatch) { alert("Could not find TAGS in this playlist."); return; }
    let currentTags;
    try {
        const cleaned = tagMatch[1].replace(/\n/g, "").replace(/\s+/g, " ").trim();
        currentTags = JSON.parse(cleaned);
    } catch(e) { alert("Could not parse TAGS: " + e.message); return; }

    const vaultTagSet = new Set();
    for (let page of allAlbums) {
        if (!page.tags) continue;
        const t = Array.isArray(page.tags) ? page.tags : [page.tags];
        for (let x of t) vaultTagSet.add(String(x).replace(/^#/, ""));
    }

    let selectedTags = new Set(currentTags);

    const overlay = document.body.createEl("div");
    overlay.style.cssText = "position:fixed; inset:0; background:rgba(0,0,0,0.85); z-index:9999; display:flex; align-items:flex-end; justify-content:center;";
    overlay.onclick = (e) => { if (e.target === overlay) overlay.remove(); };

    const modal = overlay.createEl("div");
    modal.style.cssText = "background:#1a1a1a; border-radius:20px 20px 0 0; width:100%; max-height:92vh; display:flex; flex-direction:column; overflow:hidden;";

    const handle = modal.createEl("div");
    handle.style.cssText = "width:40px; height:4px; background:#444; border-radius:2px; margin:12px auto 0 auto;";

    const header = modal.createEl("div");
    header.style.cssText = "display:flex; align-items:center; justify-content:space-between; padding:14px 20px; border-bottom:1px solid #333; flex-shrink:0;";
    const headerTitle = header.createEl("div");
    headerTitle.textContent = "✏️ Edit Tags";
    headerTitle.style.cssText = "color:#fff; font-size:18px; font-weight:bold;";
    const closeBtn = header.createEl("button");
    closeBtn.textContent = "✕";
    closeBtn.style.cssText = "background:#333; border:none; border-radius:8px; color:#aaa; font-size:18px; width:40px; height:40px; cursor:pointer;";
    closeBtn.onclick = () => overlay.remove();

    const body = modal.createEl("div");
    body.style.cssText = "padding:16px; overflow-y:auto; flex:1;";

    const currentLabel = body.createEl("div");
    currentLabel.textContent = "Current tags — tap to remove:";
    currentLabel.style.cssText = "color:#aaa; font-size:13px; margin-bottom:8px;";

    const currentPills = body.createEl("div");
    currentPills.style.cssText = "display:flex; flex-wrap:wrap; gap:8px; margin-bottom:16px; min-height:36px;";

    function renderCurrentPills() {
        currentPills.innerHTML = "";
        if (selectedTags.size === 0) {
            const empty = currentPills.createEl("div");
            empty.style.cssText = "color:#555; font-style:italic; font-size:12px;";
            empty.textContent = "No tags selected";
            return;
        }
        for (let tag of selectedTags) {
            const pill = currentPills.createEl("span");
            pill.textContent = tag + " ✕";
            pill.style.cssText = "padding:6px 14px; background:#7c3aed; border-radius:20px; color:#fff; font-size:13px; cursor:pointer;";
            pill.onclick = () => { selectedTags.delete(tag); renderCurrentPills(); renderAvailable(); };
        }
    }

    const tagSearch = body.createEl("input");
    tagSearch.type = "text";
    tagSearch.placeholder = "Search tags to add...";
    tagSearch.style.cssText = "width:100%; padding:10px 12px; background:#222; border:1px solid #444; border-radius:8px; color:#fff; font-size:15px; box-sizing:border-box; margin-bottom:10px;";

    const availableLabel = body.createEl("div");
    availableLabel.style.cssText = "color:#aaa; font-size:13px; margin-bottom:8px;";

    const availableGrid = body.createEl("div");
    availableGrid.style.cssText = "display:flex; flex-wrap:wrap; gap:8px; max-height:200px; overflow-y:auto; margin-bottom:16px;";

    function renderAvailable() {
        availableGrid.innerHTML = "";
        const query = tagSearch.value.toLowerCase().trim();
        let tags = Array.from(vaultTagSet).sort((a,b) => a.localeCompare(b, undefined, {sensitivity:"base"}));
        if (query) tags = tags.filter(t => t.toLowerCase().includes(query));
        const selLower = new Set(Array.from(selectedTags).map(t => t.toLowerCase()));
        const unselected = tags.filter(t => !selLower.has(t.toLowerCase()));
        availableLabel.textContent = `${unselected.length} tags available — tap to add`;
        for (let tag of unselected) {
            const pill = availableGrid.createEl("span");
            pill.textContent = tag;
            pill.style.cssText = "padding:6px 14px; background:#222; border:1px solid #444; border-radius:20px; color:#aaa; font-size:13px; cursor:pointer;";
            pill.onmouseenter = () => { pill.style.background = "#7c3aed"; pill.style.color = "#fff"; pill.style.borderColor = "#7c3aed"; };
            pill.onmouseleave = () => { pill.style.background = "#222"; pill.style.color = "#aaa"; pill.style.borderColor = "#444"; };
            pill.onclick = () => { selectedTags.add(tag); renderCurrentPills(); renderAvailable(); };
        }
    }

    tagSearch.addEventListener("input", renderAvailable);
    renderCurrentPills();
    renderAvailable();

    const saveBtn = body.createEl("button");
    saveBtn.textContent = "Save";
    saveBtn.style.cssText = "padding:14px; background:#7c3aed; border:none; border-radius:12px; color:#fff; font-size:16px; font-weight:bold; cursor:pointer; width:100%; margin-top:8px;";
    saveBtn.onclick = async () => {
        const newTags = JSON.stringify(Array.from(selectedTags).sort((a,b) => a.localeCompare(b, undefined, {sensitivity:"base"})));
        const newContent = content.replace(/const TAGS\s*=\s*\[.*?\];/s, `const TAGS = ${newTags};`);
        await app.vault.modify(file, newContent);
        overlay.remove();
        location.reload();
    };

    document.body.appendChild(overlay);
};
function playlistPool() {
    let pool;
    if (TAGS) {
        const filterTag = genreSelect.value;
        const activeTags = filterTag ? [filterTag] : SORTED_TAGS;
        const seenIds = new Set();
        pool = [];
        for (let TAG of activeTags) {
            for (let p of byTag.get(TAG.toLowerCase()) || []) {
                const id = String(p.tidal_id);
                if (!seenIds.has(id)) { seenIds.add(id); pool.push(p); }
            }
        }
    } else {
        pool = idAlbums;
    }
    const search = searchInput.value.toLowerCase().trim();
    if (search) pool = pool.filter(p => matchesSearch(p, search));
    return pool;
}

const randomBtn = nav.createEl("div");
randomBtn.textContent = "Random Album";
randomBtn.style.cssText = "padding:10px 20px; background:#1a1a1a; color:#fff; border-radius:10px; font-size:14px; font-weight:bold; cursor:pointer; box-shadow:0 4px 12px rgba(0,0,0,0.4);";
randomBtn.onmouseenter = () => randomBtn.style.background = "#222";
randomBtn.onmouseleave = () => randomBtn.style.background = "#1a1a1a";
randomBtn.onclick = () => {
    const pool = playlistPool();
    if (pool.length === 0) { alert("No albums to pick from."); return; }
    const pick = pool[Math.floor(Math.random() * pool.length)];
    app.workspace.openLinkText(pick.file.path, "", false);
};
// ── Genre page title (spelled the way the albums spell the tag) ──
if (GENRE && TAGS) {
    const low = TAGS[0].toLowerCase();
    let shown = TAGS[0];
    for (const p of allAlbums) {
        const hit = (Array.isArray(p.tags) ? p.tags : [p.tags]).map(x => String(x).replace(/^#/, "")).find(x => x.toLowerCase() === low);
        if (hit) { shown = hit; break; }
    }
    const style = document.getElementById("genre-page-style") || document.head.appendChild(Object.assign(document.createElement("style"), { id: "genre-page-style" }));
    style.textContent = ".view-content:has(.pl-genre-title) .inline-title { display: none !important; }";
    const h = dv.container.createEl("div", { cls: "pl-genre-title" });
    h.style.cssText = "font-size:30px; font-weight:800; color:#fff; margin:4px 0 2px 0;";
    h.textContent = shown;
    const sub = dv.container.createEl("div");
    sub.style.cssText = "font-size:12px; font-weight:700; letter-spacing:0.14em; text-transform:uppercase; color:rgba(255,255,255,0.5); margin-bottom:14px;";
    sub.textContent = `Genre · ${(byTag.get(low) || []).length} albums`;
}

// ── Controls Bar ──────────────────────────────────────────
const controls = dv.container.createEl("div");
controls.style.cssText = "display:flex; flex-wrap:wrap; gap:10px; align-items:center; padding:12px; background:#111; border-radius:10px; margin-bottom:20px;";

const searchInput = controls.createEl("input");
searchInput.type = "text";
searchInput.placeholder = "Search by title or artist...";
searchInput.style.cssText = "flex:1; min-width:200px; padding:6px 12px; background:#222; border:1px solid #444; border-radius:6px; color:#fff; font-size:13px;";

const genreSelect = controls.createEl("select");
genreSelect.style.cssText = "padding:6px 12px; background:#222; border:1px solid #444; border-radius:6px; color:#fff; font-size:13px;";
const allOption = genreSelect.createEl("option"); allOption.value = ""; allOption.textContent = "All Genres";
for (let tag of SORTED_TAGS) { const opt = genreSelect.createEl("option"); opt.value = tag; opt.textContent = tag; }
if (!TAGS || SORTED_TAGS.length < 2) genreSelect.style.display = "none";

const sortSelect = controls.createEl("select");
sortSelect.style.cssText = "padding:6px 12px; background:#222; border:1px solid #444; border-radius:6px; color:#fff; font-size:13px;";
for (let [value, label] of [["artist","Sort: Artist A-Z"],["artist_desc","Sort: Artist Z-A"],["title","Sort: Title A-Z"],["year_desc","Sort: Newest First"],["year_asc","Sort: Oldest First"]]) {
    const el = sortSelect.createEl("option"); el.value = value; el.textContent = label;
}

const resultsCount = controls.createEl("div");
resultsCount.style.cssText = "color:#666; font-size:12px; margin-left:auto;";

const mainArea = dv.container.createEl("div");

function sortPages(arr, sortBy) {
    const a2 = arr.slice();
    switch (sortBy) {
        case "artist":      return a2.sort((a,b) => (a.artist||"").localeCompare(b.artist||""));
        case "artist_desc": return a2.sort((a,b) => (b.artist||"").localeCompare(a.artist||""));
        case "title":       return a2.sort((a,b) => (a.title||a.file.name).localeCompare(b.title||b.file.name));
        case "year_desc":   return a2.sort((a,b) => (b.year||0) - (a.year||0));
        case "year_asc":    return a2.sort((a,b) => (a.year||0) - (b.year||0));
        default:            return a2;
    }
}

function renderCards(container, pages) {
    container.style.cssText = "display:flex; flex-wrap:wrap; gap:16px; padding:10px 0 30px 0;";
    const frag = document.createDocumentFragment();
    for (let page of pages) {
        const card = document.createElement("div");
        card.style.cssText = "width:160px; background:#1a1a1a; border-radius:10px; overflow:hidden; cursor:pointer; transition:transform 0.2s; box-shadow:0 4px 10px rgba(0,0,0,0.4);";
        card.onmouseenter = () => card.style.transform = "scale(1.05)";
        card.onmouseleave = () => card.style.transform = "scale(1.0)";

        const img = document.createElement("img");
        img.loading = "lazy";
        img.style.cssText = "width:160px; height:160px; object-fit:cover; display:block; background:#333;";
        const coverFile = getCover(page);
        if (coverFile) img.src = app.vault.getResourcePath(coverFile);
        card.appendChild(img);

        const info = document.createElement("div");
        info.style.cssText = "padding:8px 10px;";
        const title = document.createElement("div");
        title.style.cssText = "color:#fff; font-weight:bold; font-size:12px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;";
        title.textContent = page.title || page.file.name;
        const artist = document.createElement("div");
        artist.style.cssText = "color:#aaa; font-size:11px; margin-top:2px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;";
        artist.textContent = page.artist || "";
        const year = document.createElement("div");
        year.style.cssText = "color:#666; font-size:10px; margin-top:2px;";
        year.textContent = page.year || "";
        info.append(title, artist, year);
        card.appendChild(info);

        card.onclick = () => app.workspace.openLinkText(page.file.path, "", false);
        frag.appendChild(card);
    }
    container.appendChild(frag);
}

function matchesSearch(p, search) {
    return (p.title || p.file.name).toLowerCase().includes(search) ||
           (p.artist || "").toLowerCase().includes(search);
}

function renderSection(label, pages, sortBy) {
    const sorted = sortPages(pages, sortBy);
    if (label) {
        const header = mainArea.createEl("h2");
        header.textContent = "🏷 " + label;
        header.style.cssText = "margin-top:30px; margin-bottom:4px; border-bottom:1px solid #333; padding-bottom:6px;";
    }
    const countEl = mainArea.createEl("div");
    countEl.style.cssText = "color:#666; font-size:12px; margin-bottom:8px;";
    countEl.textContent = sorted.length + " albums";
    renderCards(mainArea.createEl("div"), sorted);
    return sorted.length;
}

function renderAll() {
    mainArea.innerHTML = "";
    const search = searchInput.value.toLowerCase().trim();
    const sortBy = sortSelect.value;
    let totalShown = 0;

    if (TAGS) {
        const filterTag = genreSelect.value;
        const activeTags = filterTag ? [filterTag] : SORTED_TAGS;
        for (let TAG of activeTags) {
            let pages = byTag.get(TAG.toLowerCase()) || [];
            if (search) pages = pages.filter(p => matchesSearch(p, search));
            if (pages.length === 0) continue;
            totalShown += renderSection(SORTED_TAGS.length > 1 ? TAG : null, pages, sortBy);
        }
    } else if (ALBUM_IDS) {
        let pages = idAlbums;
        if (search) pages = pages.filter(p => matchesSearch(p, search));
        if (pages.length > 0) totalShown += renderSection(null, pages, sortBy);
    }

    resultsCount.textContent = totalShown + " albums shown";
    if (totalShown === 0) {
        const empty = mainArea.createEl("div");
        empty.style.cssText = "color:#666; font-style:italic; padding:20px;";
        empty.textContent = "No albums match your search.";
    }
}

// Debounce search so we don't rebuild the DOM on every keystroke
let searchTimer;
searchInput.addEventListener("input", () => { clearTimeout(searchTimer); searchTimer = setTimeout(renderAll, 150); });
genreSelect.addEventListener("change", renderAll);
sortSelect.addEventListener("change", renderAll);
renderAll();