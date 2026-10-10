
```dataviewjs
const allPages = dv.pages().where(p => p.tidal_id);
const allCovers = app.vault.getFiles().filter(f => f.path.includes("_covers"));

function getCover(page) {
    const albumTitle = page.file.name.replace(/\s\(\d{4}\)$/, "");
    const expectedPath = `_covers/${page.artist} - ${albumTitle}.jpg`;
    return allCovers.find(f => f.path === expectedPath);
}

// ── Modal System ──────────────────────────────────────────
function createModal(title) {
    const overlay = document.body.createEl("div");
    overlay.style.cssText = `
        position: fixed; inset: 0;
        background: rgba(0,0,0,0.85);
        z-index: 9999;
        display: flex;
        align-items: flex-end;
        justify-content: center;
    `;
    const modal = overlay.createEl("div");
    modal.style.cssText = `
        background: #1a1a1a;
        border-radius: 20px 20px 0 0;
        width: 100%;
        max-width: 100%;
        max-height: 92vh;
        display: flex;
        flex-direction: column;
        box-shadow: 0 -8px 40px rgba(0,0,0,0.8);
        overflow: hidden;
    `;
    const handle = modal.createEl("div");
    handle.style.cssText = `
        width: 40px; height: 4px;
        background: #444; border-radius: 2px;
        margin: 12px auto 0 auto;
        flex-shrink: 0;
    `;
    const header = modal.createEl("div");
    header.style.cssText = `
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 14px 20px;
        border-bottom: 1px solid #333;
        flex-shrink: 0;
    `;
    const titleEl = header.createEl("div");
    titleEl.textContent = title;
    titleEl.style.cssText = "color:#fff; font-size:18px; font-weight:bold;";
    const closeBtn = header.createEl("button");
    closeBtn.textContent = "✕";
    closeBtn.style.cssText = `
        background: #333; border: none; border-radius: 8px;
        color: #aaa; font-size:18px; width:40px; height:40px;
        cursor:pointer; flex-shrink:0;
    `;
    closeBtn.onclick = () => overlay.remove();
    overlay.onclick = (e) => { if (e.target === overlay) overlay.remove(); };
    const body = modal.createEl("div");
    body.style.cssText = "padding: 16px 16px 32px 16px; overflow-y: auto; flex: 1; -webkit-overflow-scrolling: touch;";
    return { overlay, modal, body, titleEl };
}

// ── Shared: Build tag-based playlist note ─────────────────
function buildPlaylistNote(name, tagsArray, pages) {
    const tagsJson = JSON.stringify(tagsArray);
    const date = new Date().toISOString().split("T")[0];
    return `# ${name}
**Created:** ${date} | **Tags:** ${tagsArray.join(", ")} | **Albums:** ${pages.length}

\`\`\`dataviewjs
const btn = dv.container.createEl("a");
btn.textContent = "← Library";
btn.style.cssText = \`
    display: inline-block;
    padding: 10px 20px;
    background: #7c3aed;
    color: #fff;
    border-radius: 10px;
    font-size: 15px;
    font-weight: bold;
    text-decoration: none;
    cursor: pointer;
    margin-bottom: 16px;
\`;
btn.onclick = (e) => {
    e.preventDefault();
    app.workspace.openLinkText("Library", "", false);
};
\`\`\`

\`\`\`dataviewjs
const TAGS = ${tagsJson};
const allCovers = app.vault.getFiles().filter(f => f.path.includes("_covers"));
function getCover(page) {
    const albumTitle = page.file.name.replace(/\\s\\(\\d{4}\\)$/, "");
    const expectedPath = \`_covers/\${page.artist} - \${albumTitle}.jpg\`;
    return allCovers.find(f => f.path === expectedPath);
}
const controls = dv.container.createEl("div");
controls.style.cssText = "display:flex; flex-wrap:wrap; gap:10px; align-items:center; padding:12px; background:#111; border-radius:10px; margin-bottom:20px;";
const searchInput = controls.createEl("input");
searchInput.type = "text";
searchInput.placeholder = "Search by title or artist...";
searchInput.style.cssText = "flex:1; min-width:200px; padding:6px 12px; background:#222; border:1px solid #444; border-radius:6px; color:#fff; font-size:13px;";
const genreSelect = controls.createEl("select");
genreSelect.style.cssText = "padding:6px 12px; background:#222; border:1px solid #444; border-radius:6px; color:#fff; font-size:13px;";
const allOpt = genreSelect.createEl("option");
allOpt.value = ""; allOpt.textContent = "All Genres";
for (let tag of TAGS) {
    const opt = genreSelect.createEl("option");
    opt.value = tag; opt.textContent = tag;
}
const sortSelect = controls.createEl("select");
sortSelect.style.cssText = "padding:6px 12px; background:#222; border:1px solid #444; border-radius:6px; color:#fff; font-size:13px;";
for (let [value, label] of [["artist","Artist A-Z"],["artist_desc","Artist Z-A"],["title","Title A-Z"],["year_desc","Newest"],["year_asc","Oldest"]]) {
    const el = sortSelect.createEl("option");
    el.value = value; el.textContent = label;
}
const resultsCount = controls.createEl("div");
resultsCount.style.cssText = "color:#666; font-size:12px; margin-left:auto;";
const mainArea = dv.container.createEl("div");
function sortPages(pages, sortBy) {
    const arr = pages.array ? pages.array() : Array.from(pages);
    switch (sortBy) {
        case "artist": return arr.sort((a,b) => (a.artist||"").localeCompare(b.artist||""));
        case "artist_desc": return arr.sort((a,b) => (b.artist||"").localeCompare(a.artist||""));
        case "title": return arr.sort((a,b) => (a.title||a.file.name).localeCompare(b.title||b.file.name));
        case "year_desc": return arr.sort((a,b) => (b.year||0)-(a.year||0));
        case "year_asc": return arr.sort((a,b) => (a.year||0)-(b.year||0));
        default: return arr;
    }
}
function renderCards(container, pages) {
    container.innerHTML = "";
    if (pages.length === 0) {
        const empty = container.createEl("div");
        empty.style.cssText = "color:#666; font-style:italic; padding:10px;";
        empty.textContent = "No albums found.";
        return;
    }
    container.style.cssText = "display:flex; flex-wrap:wrap; gap:12px; padding:10px 0 30px 0;";
    for (let page of pages) {
        const card = container.createEl("div");
        card.style.cssText = "width:140px; background:#1a1a1a; border-radius:10px; overflow:hidden; cursor:pointer; box-shadow:0 4px 10px rgba(0,0,0,0.4);";
        const img = card.createEl("img");
        img.style.cssText = "width:140px; height:140px; object-fit:cover; display:block;";
        const coverFile = getCover(page);
        if (coverFile) img.src = app.vault.getResourcePath(coverFile);
        else img.style.cssText += "background:#333;";
        const info = card.createEl("div");
        info.style.cssText = "padding:8px 10px;";
        const title = info.createEl("div");
        title.style.cssText = "color:#fff; font-weight:bold; font-size:12px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;";
        title.textContent = page.title || page.file.name;
        const artist = info.createEl("div");
        artist.style.cssText = "color:#aaa; font-size:11px; margin-top:2px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;";
        artist.textContent = page.artist || "";
        card.onclick = () => app.workspace.openLinkText(page.file.path, "", false);
        container.appendChild(card);
    }
}
function renderAll() {
    mainArea.innerHTML = "";
    const search = searchInput.value.toLowerCase();
    const filterTag = genreSelect.value;
    const sortBy = sortSelect.value;
    const activeTags = filterTag ? [filterTag] : TAGS;
    let totalShown = 0;
    for (let TAG of activeTags) {
        let pages = dv.pages().where(p =>
            p.tidal_id && p.tags &&
            p.tags.some(t => t.toLowerCase() === TAG.toLowerCase() || t.toLowerCase() === "#" + TAG.toLowerCase())
        );
        if (search) pages = pages.where(p =>
            (p.title || p.file.name).toLowerCase().includes(search) ||
            (p.artist || "").toLowerCase().includes(search)
        );
        const sorted = sortPages(pages, sortBy);
        if (sorted.length === 0) continue;
        totalShown += sorted.length;
        const header = mainArea.createEl("h2");
        header.textContent = TAG;
        header.style.cssText = "margin-top:30px; margin-bottom:4px; border-bottom:1px solid #333; padding-bottom:6px;";
        const countEl = mainArea.createEl("div");
        countEl.style.cssText = "color:#666; font-size:12px; margin-bottom:8px;";
        countEl.textContent = sorted.length + " albums";
        const container = mainArea.createEl("div");
        renderCards(container, sorted);
    }
    resultsCount.textContent = totalShown + " albums shown";
    if (totalShown === 0) {
        const empty = mainArea.createEl("div");
        empty.style.cssText = "color:#666; font-style:italic; padding:20px;";
        empty.textContent = "No albums match.";
    }
}
searchInput.addEventListener("input", renderAll);
genreSelect.addEventListener("change", renderAll);
sortSelect.addEventListener("change", renderAll);
renderAll();
\`\`\`
`;
}

// ── Shared: Build album ID-based playlist note ────────────
function buildAlbumPlaylistNote(name, pages) {
    const tidalIds = JSON.stringify(pages.map(p => p.tidal_id));
    const date = new Date().toISOString().split("T")[0];
    return `# ${name}
**Created:** ${date} | **Albums:** ${pages.length}

\`\`\`dataviewjs
const btn = dv.container.createEl("a");
btn.textContent = "← Library";
btn.style.cssText = \`
    display: inline-block;
    padding: 10px 20px;
    background: #7c3aed;
    color: #fff;
    border-radius: 10px;
    font-size: 15px;
    font-weight: bold;
    text-decoration: none;
    cursor: pointer;
    margin-bottom: 16px;
\`;
btn.onclick = (e) => {
    e.preventDefault();
    app.workspace.openLinkText("Library", "", false);
};
\`\`\`
\`\`\`dataviewjs
const ALBUM_IDS = ${tidalIds};
const allCovers = app.vault.getFiles().filter(f => f.path.includes("_covers"));
function getCover(page) {
    const albumTitle = page.file.name.replace(/\\s\\(\\d{4}\\)$/, "");
    const expectedPath = \`_covers/\${page.artist} - \${albumTitle}.jpg\`;
    return allCovers.find(f => f.path === expectedPath);
}
const controls = dv.container.createEl("div");
controls.style.cssText = "display:flex; flex-wrap:wrap; gap:10px; align-items:center; padding:12px; background:#111; border-radius:10px; margin-bottom:20px;";
const searchInput = controls.createEl("input");
searchInput.type = "text";
searchInput.placeholder = "Search by title or artist...";
searchInput.style.cssText = "flex:1; min-width:200px; padding:6px 12px; background:#222; border:1px solid #444; border-radius:6px; color:#fff; font-size:13px;";
const sortSelect = controls.createEl("select");
sortSelect.style.cssText = "padding:6px 12px; background:#222; border:1px solid #444; border-radius:6px; color:#fff; font-size:13px;";
for (let [value, label] of [["artist","Artist A-Z"],["artist_desc","Artist Z-A"],["title","Title A-Z"],["year_desc","Newest"],["year_asc","Oldest"]]) {
    const el = sortSelect.createEl("option");
    el.value = value; el.textContent = label;
}
const resultsCount = controls.createEl("div");
resultsCount.style.cssText = "color:#666; font-size:12px; margin-left:auto;";
const mainArea = dv.container.createEl("div");
function sortPages(arr, sortBy) {
    switch (sortBy) {
        case "artist": return arr.sort((a,b) => (a.artist||"").localeCompare(b.artist||""));
        case "artist_desc": return arr.sort((a,b) => (b.artist||"").localeCompare(a.artist||""));
        case "title": return arr.sort((a,b) => (a.title||a.file.name).localeCompare(b.title||b.file.name));
        case "year_desc": return arr.sort((a,b) => (b.year||0)-(a.year||0));
        case "year_asc": return arr.sort((a,b) => (a.year||0)-(b.year||0));
        default: return arr;
    }
}
function renderAll() {
    mainArea.innerHTML = "";
    const search = searchInput.value.toLowerCase();
    const sortBy = sortSelect.value;
    let pages = dv.pages().where(p => p.tidal_id && ALBUM_IDS.includes(p.tidal_id)).array();
    if (search) pages = pages.filter(p =>
        (p.title || p.file.name || "").toLowerCase().includes(search) ||
        (p.artist || "").toLowerCase().includes(search)
    );
    const sorted = sortPages(pages, sortBy);
    resultsCount.textContent = sorted.length + " albums";
    const grid = mainArea.createEl("div");
    grid.style.cssText = "display:flex; flex-wrap:wrap; gap:12px; padding:10px 0;";
    if (sorted.length === 0) {
        const empty = grid.createEl("div");
        empty.style.cssText = "color:#666; font-style:italic; padding:10px;";
        empty.textContent = "No albums found.";
        return;
    }
    for (let page of sorted) {
        const card = grid.createEl("div");
        card.style.cssText = "width:140px; background:#1a1a1a; border-radius:10px; overflow:hidden; cursor:pointer; box-shadow:0 4px 10px rgba(0,0,0,0.4);";
        const img = card.createEl("img");
        img.style.cssText = "width:140px; height:140px; object-fit:cover; display:block;";
        const coverFile = getCover(page);
        if (coverFile) img.src = app.vault.getResourcePath(coverFile);
        else img.style.cssText += "background:#333;";
        const info = card.createEl("div");
        info.style.cssText = "padding:8px 10px;";
        const title = info.createEl("div");
        title.style.cssText = "color:#fff; font-weight:bold; font-size:12px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;";
        title.textContent = page.title || page.file.name;
        const artist = info.createEl("div");
        artist.style.cssText = "color:#aaa; font-size:11px; margin-top:2px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;";
        artist.textContent = page.artist || "";
        card.onclick = () => app.workspace.openLinkText(page.file.path, "", false);
        grid.appendChild(card);
    }
}
searchInput.addEventListener("input", renderAll);
sortSelect.addEventListener("change", renderAll);
renderAll();
\`\`\`
`;
}

// ── Shared: Save playlist note ────────────────────────────
async function savePlaylistNote(name, content, overlay) {
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

// ── Tool: Playlist Type Picker ────────────────────────────
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
        card.style.cssText = `
            background: #222; border: 1px solid #333; border-radius: 14px;
            padding: 22px 20px; cursor: pointer;
            display: flex; align-items: center; gap: 18px;
        `;
        card.onclick = opt.action;

        const icon = card.createEl("div");
        icon.textContent = opt.icon;
        icon.style.cssText = "font-size:36px; flex-shrink:0;";

        const text = card.createEl("div");
        const name = text.createEl("div");
        name.textContent = opt.name;
        name.style.cssText = "color:#fff; font-size:17px; font-weight:bold; margin-bottom:4px;";
        const desc = text.createEl("div");
        desc.textContent = opt.desc;
        desc.style.cssText = "color:#666; font-size:13px; line-height:1.4;";
    }
}

// ── Tool: Create Playlist by Tag ──────────────────────────
function openPlaylistByTag() {
    const { overlay, body } = createModal("🏷 Create Playlist by Tag");

    const tagCategories = {
        "Metal": ["PowerMetal","AlternativeMetal","AvantGardeMetal","BlackMetal","Blackgaze","Deathcore","DoomMetal","FolkMetal","GothicMetal","MathCore","MelodicDeathMetal","MelodicMetalcore","NoiseMetal","NuMetal","ProgMetal","ProgMetalCore","ProgDeathMetal","SludgeMetal","StonerMetal","SymphonicMetal","TechnicalDeathMetal","ThrashMetal","FunMetalThings"],
        "Rock": ["AlternativeRock","ArtRock","BritPop","DancePunk","ExperimentalRock","FolkRock","GaragePunk","GlamRock","HardRock","IndieRock","IndustrialRock","MathRock","NoiseRock","PopRock","PostPunkRevival","PostRock","PsychedelicRock","Shoegaze","SpaceRock"],
        "Hip Hop": ["AbstractHipHop","BoomBap","ConsciousHipHop","EastCoastHipHop","ExperimentalHipHop","HardcoreHipHop","HipHop","IndustrialHipHop","JazzRap","LoFiHipHop","PopRap","RapMetal"],
        "Alternative": ["AltPop","AlternativeDance","ArtPop","ChamberPop","DreamPop","Emo","IndieFolk","Indietronica","MidwestEmo","NeoPsychedelia","NewWave","NoisePop","PostHardcore","ProgressivePop","PsychedelicPop"],
        "Electronic": ["Ambient","AmbientTechno","Bitpop","Breakcore","Cybergrind","DancePop","DigitalHardcore","DrumandBass","Dubstep","EDM","ElectroHouse","Electropop","Folktronica","HyperPop","Synthpop"],
        "Jazz & Soul": ["JazzFunk","JazzFusion","JazzPop","Soul","Funk","VocalJazz","BluesRock"],
        "Folk & Acoustic": ["AltCountry","Folk","FolkRock","IndieFolk","SingerSongwriter"],
        "Prog & Art": ["AvantProg","PostRock","ProgRock","SymphonicProg","RockOpera","ModernClassical"],
    };

    const tagSet = new Set();
    for (let page of allPages) {
        if (page.tags) for (let t of page.tags) tagSet.add(t.replace(/^#/,""));
    }
    const knownTags = new Set(Object.values(tagCategories).flat());
    const otherTags = Array.from(tagSet).filter(t => !knownTags.has(t)).sort();
    if (otherTags.length > 0) tagCategories["Other"] = otherTags;

    let selectedTags = new Set();
    let matchMode = "any";
    let activeCategory = "All";

    const nameRow = body.createEl("div");
    nameRow.style.cssText = "display:flex; align-items:center; gap:12px; margin-bottom:16px;";
    const nameLabel = nameRow.createEl("label");
    nameLabel.textContent = "Name:";
    nameLabel.style.cssText = "color:#aaa; font-size:14px; white-space:nowrap;";
    const nameInput = nameRow.createEl("input");
    nameInput.type = "text";
    nameInput.value = "My Playlist";
    nameInput.style.cssText = "flex:1; padding:10px 12px; background:#222; border:1px solid #444; border-radius:8px; color:#fff; font-size:16px;";

    const matchRow = body.createEl("div");
    matchRow.style.cssText = "display:flex; gap:10px; align-items:center; margin-bottom:14px;";
    const matchLabel = matchRow.createEl("div");
    matchLabel.textContent = "Match:";
    matchLabel.style.cssText = "color:#aaa; font-size:14px;";
    const anyBtn = matchRow.createEl("button");
    anyBtn.textContent = "Any (OR)";
    anyBtn.style.cssText = "flex:1; padding:10px; border-radius:20px; border:1px solid #7c3aed; background:#7c3aed; color:#fff; font-size:14px; cursor:pointer;";
    const allBtn = matchRow.createEl("button");
    allBtn.textContent = "All (AND)";
    allBtn.style.cssText = "flex:1; padding:10px; border-radius:20px; border:1px solid #444; background:#222; color:#aaa; font-size:14px; cursor:pointer;";

    anyBtn.onclick = () => {
        matchMode = "any";
        anyBtn.style.cssText = "flex:1; padding:10px; border-radius:20px; border:1px solid #7c3aed; background:#7c3aed; color:#fff; font-size:14px; cursor:pointer;";
        allBtn.style.cssText = "flex:1; padding:10px; border-radius:20px; border:1px solid #444; background:#222; color:#aaa; font-size:14px; cursor:pointer;";
        renderPreview();
    };
    allBtn.onclick = () => {
        matchMode = "all";
        allBtn.style.cssText = "flex:1; padding:10px; border-radius:20px; border:1px solid #7c3aed; background:#7c3aed; color:#fff; font-size:14px; cursor:pointer;";
        anyBtn.style.cssText = "flex:1; padding:10px; border-radius:20px; border:1px solid #444; background:#222; color:#aaa; font-size:14px; cursor:pointer;";
        renderPreview();
    };

    const searchInput = body.createEl("input");
    searchInput.type = "text";
    searchInput.placeholder = "Search tags...";
    searchInput.style.cssText = "width:100%; padding:10px 12px; background:#222; border:1px solid #444; border-radius:8px; color:#fff; font-size:15px; box-sizing:border-box; margin-bottom:12px;";

    const catRow = body.createEl("div");
    catRow.style.cssText = "display:flex; flex-wrap:wrap; gap:8px; margin-bottom:12px;";

    function renderCatPills() {
        catRow.innerHTML = "";
        for (let cat of ["All", ...Object.keys(tagCategories)]) {
            const pill = catRow.createEl("button");
            pill.textContent = cat;
            pill.style.cssText = `padding:8px 14px; border-radius:20px; font-size:13px; cursor:pointer;
                border:1px solid ${activeCategory === cat ? "#7c3aed" : "#444"};
                background:${activeCategory === cat ? "#7c3aed" : "#222"};
                color:${activeCategory === cat ? "#fff" : "#aaa"};`;
            pill.onclick = () => { activeCategory = cat; renderCatPills(); renderTagGrid(); };
        }
    }
    renderCatPills();

    const tagGrid = body.createEl("div");
    tagGrid.style.cssText = "display:flex; flex-wrap:wrap; gap:8px; margin-bottom:16px; max-height:180px; overflow-y:auto; padding:4px;";

    function getVisibleTags() {
        const search = searchInput.value.toLowerCase();
        let tags = activeCategory === "All" ? Array.from(tagSet).sort() : (tagCategories[activeCategory] || []);
        if (search) tags = tags.filter(t => t.toLowerCase().includes(search));
        return tags;
    }

    function renderTagGrid() {
        tagGrid.innerHTML = "";
        for (let tag of getVisibleTags()) {
            const btn = tagGrid.createEl("button");
            btn.textContent = tag;
            btn.style.cssText = `padding:8px 14px; border-radius:20px; font-size:13px; cursor:pointer;
                border:1px solid ${selectedTags.has(tag) ? "#7c3aed" : "#444"};
                background:${selectedTags.has(tag) ? "#7c3aed" : "#222"};
                color:${selectedTags.has(tag) ? "#fff" : "#aaa"};`;
            btn.onclick = () => {
                selectedTags.has(tag) ? selectedTags.delete(tag) : selectedTags.add(tag);
                renderTagGrid();
                renderPreview();
            };
        }
    }
    renderTagGrid();
    searchInput.addEventListener("input", renderTagGrid);

    const selectedRow = body.createEl("div");
    selectedRow.style.cssText = "margin-bottom:12px;";
    const previewLabel = body.createEl("div");
    previewLabel.style.cssText = "color:#aaa; font-size:13px; margin-bottom:8px;";
    const previewGrid = body.createEl("div");
    previewGrid.style.cssText = "display:flex; flex-wrap:wrap; gap:10px; margin-bottom:16px; max-height:200px; overflow-y:auto;";

    function getMatchingPages() {
        if (selectedTags.size === 0) return [];
        const selected = Array.from(selectedTags);
        return allPages.where(p => {
            if (!p.tags) return false;
            const pageTags = p.tags.map(t => t.replace(/^#/,"").toLowerCase());
            return matchMode === "any"
                ? selected.some(tag => pageTags.includes(tag.toLowerCase()))
                : selected.every(tag => pageTags.includes(tag.toLowerCase()));
        }).array().sort((a,b) => (a.artist||"").localeCompare(b.artist||""));
    }

    function renderPreview() {
        previewGrid.innerHTML = "";
        selectedRow.innerHTML = "";
        if (selectedTags.size > 0) {
            const selLabel = selectedRow.createEl("div");
            selLabel.textContent = "Selected:";
            selLabel.style.cssText = "color:#aaa; font-size:13px; margin-bottom:6px;";
            const selPills = selectedRow.createEl("div");
            selPills.style.cssText = "display:flex; flex-wrap:wrap; gap:6px; margin-bottom:10px;";
            for (let tag of selectedTags) {
                const pill = selPills.createEl("span");
                pill.textContent = tag + " ✕";
                pill.style.cssText = "padding:6px 12px; background:#7c3aed; border-radius:20px; color:#fff; font-size:13px; cursor:pointer;";
                pill.onclick = () => { selectedTags.delete(tag); renderTagGrid(); renderPreview(); };
            }
        }
        const matches = getMatchingPages();
        previewLabel.textContent = selectedTags.size === 0 ? "Select tags above to preview" : `${matches.length} albums match`;
        for (let page of matches) {
            const card = previewGrid.createEl("div");
            card.style.cssText = "width:90px; background:#111; border-radius:8px; overflow:hidden; cursor:pointer;";
            card.onclick = () => app.workspace.openLinkText(page.file.path, "", false);
            const img = card.createEl("img");
            img.style.cssText = "width:90px; height:90px; object-fit:cover; display:block;";
            const coverFile = getCover(page);
            if (coverFile) img.src = app.vault.getResourcePath(coverFile);
            else img.style.cssText += "background:#333;";
            const info = card.createEl("div");
            info.style.cssText = "padding:4px 6px;";
            const t = info.createEl("div");
            t.style.cssText = "color:#fff; font-size:9px; font-weight:bold; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;";
            t.textContent = page.title || page.file.name;
            const a = info.createEl("div");
            a.style.cssText = "color:#aaa; font-size:8px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;";
            a.textContent = page.artist || "";
        }
    }
    renderPreview();

    const createBtn = body.createEl("button");
    createBtn.textContent = "Create Playlist";
    createBtn.style.cssText = "padding:14px 24px; background:#7c3aed; border:none; border-radius:12px; color:#fff; font-size:16px; font-weight:bold; cursor:pointer; width:100%; margin-top:8px;";
    createBtn.onclick = async () => {
        const matches = getMatchingPages();
        if (matches.length === 0) { alert("No albums match!"); return; }
        const name = nameInput.value.trim() || "My Playlist";
        const content = buildPlaylistNote(name, Array.from(selectedTags), matches);
        await savePlaylistNote(name, content, overlay);
    };
}

// ── Tool: Create Playlist by Album ────────────────────────
function openPlaylistByAlbum() {
    const { overlay, body } = createModal("💿 Create Playlist by Album");

    let selectedAlbums = new Map();

    const nameRow = body.createEl("div");
    nameRow.style.cssText = "display:flex; align-items:center; gap:12px; margin-bottom:16px;";
    const nameLabel = nameRow.createEl("label");
    nameLabel.textContent = "Name:";
    nameLabel.style.cssText = "color:#aaa; font-size:14px; white-space:nowrap;";
    const nameInput = nameRow.createEl("input");
    nameInput.type = "text";
    nameInput.value = "My Playlist";
    nameInput.style.cssText = "flex:1; padding:10px 12px; background:#222; border:1px solid #444; border-radius:8px; color:#fff; font-size:16px;";

    const searchInput = body.createEl("input");
    searchInput.type = "text";
    searchInput.placeholder = "Search albums by title or artist...";
    searchInput.style.cssText = "width:100%; padding:10px 12px; background:#222; border:1px solid #444; border-radius:8px; color:#fff; font-size:15px; box-sizing:border-box; margin-bottom:10px;";

    const resultsLabel = body.createEl("div");
    resultsLabel.style.cssText = "color:#aaa; font-size:13px; margin-bottom:8px;";
    resultsLabel.textContent = "Search for albums to add...";

    const resultsGrid = body.createEl("div");
    resultsGrid.style.cssText = "display:flex; flex-wrap:wrap; gap:10px; max-height:200px; overflow-y:auto; margin-bottom:16px; padding:4px;";

    function renderResults() {
        resultsGrid.innerHTML = "";
        const query = searchInput.value.toLowerCase().trim();
        if (!query) { resultsLabel.textContent = "Search for albums to add..."; return; }
        const results = allPages.where(p =>
            (p.title || p.file.name || "").toLowerCase().includes(query) ||
            (p.artist || "").toLowerCase().includes(query)
        ).array().sort((a,b) => (a.artist||"").localeCompare(b.artist||""));
        resultsLabel.textContent = `${results.length} results — tap to add`;
        for (let page of results) {
            const isSelected = selectedAlbums.has(page.tidal_id);
            const card = resultsGrid.createEl("div");
            card.style.cssText = `width:100px; background:${isSelected ? "#2d1f4e" : "#111"}; border-radius:8px; overflow:hidden; cursor:pointer;
                border:2px solid ${isSelected ? "#7c3aed" : "transparent"};`;
            const img = card.createEl("img");
            img.style.cssText = "width:100px; height:100px; object-fit:cover; display:block;";
            const coverFile = getCover(page);
            if (coverFile) img.src = app.vault.getResourcePath(coverFile);
            else img.style.cssText += "background:#333;";
            const info = card.createEl("div");
            info.style.cssText = "padding:5px 7px;";
            const t = info.createEl("div");
            t.style.cssText = "color:#fff; font-size:10px; font-weight:bold; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;";
            t.textContent = page.title || page.file.name;
            const a = info.createEl("div");
            a.style.cssText = "color:#aaa; font-size:9px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;";
            a.textContent = page.artist || "";
            card.onclick = () => {
                selectedAlbums.has(page.tidal_id) ? selectedAlbums.delete(page.tidal_id) : selectedAlbums.set(page.tidal_id, page);
                renderResults();
                renderSelected();
            };
        }
    }
    searchInput.addEventListener("input", renderResults);

    const selectedLabel = body.createEl("div");
    selectedLabel.style.cssText = "color:#aaa; font-size:13px; margin-bottom:8px;";

    const selectedGrid = body.createEl("div");
    selectedGrid.style.cssText = "display:flex; flex-wrap:wrap; gap:10px; max-height:200px; overflow-y:auto; margin-bottom:16px; padding:4px;";

    function renderSelected() {
        selectedGrid.innerHTML = "";
        selectedLabel.textContent = selectedAlbums.size === 0 ? "No albums selected yet" : `${selectedAlbums.size} albums — tap to remove`;
        for (let [id, page] of selectedAlbums) {
            const card = selectedGrid.createEl("div");
            card.style.cssText = "width:100px; background:#2d1f4e; border-radius:8px; overflow:hidden; cursor:pointer; border:2px solid #7c3aed; position:relative;";
            const img = card.createEl("img");
            img.style.cssText = "width:100px; height:100px; object-fit:cover; display:block; opacity:0.8;";
            const coverFile = getCover(page);
            if (coverFile) img.src = app.vault.getResourcePath(coverFile);
            else img.style.cssText += "background:#333;";
            const removeBtn = card.createEl("div");
            removeBtn.textContent = "✕";
            removeBtn.style.cssText = "position:absolute; top:5px; right:5px; background:rgba(0,0,0,0.8); color:#fff; border-radius:50%; width:22px; height:22px; display:flex; align-items:center; justify-content:center; font-size:12px;";
            const info = card.createEl("div");
            info.style.cssText = "padding:5px 7px;";
            const t = info.createEl("div");
            t.style.cssText = "color:#fff; font-size:10px; font-weight:bold; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;";
            t.textContent = page.title || page.file.name;
            const a = info.createEl("div");
            a.style.cssText = "color:#aaa; font-size:9px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;";
            a.textContent = page.artist || "";
            card.onclick = () => { selectedAlbums.delete(id); renderResults(); renderSelected(); };
        }
    }
    renderSelected();

    const createBtn = body.createEl("button");
    createBtn.textContent = "Create Playlist";
    createBtn.style.cssText = "padding:14px 24px; background:#7c3aed; border:none; border-radius:12px; color:#fff; font-size:16px; font-weight:bold; cursor:pointer; width:100%; margin-top:8px;";
    createBtn.onclick = async () => {
        if (selectedAlbums.size === 0) { alert("No albums selected!"); return; }
        const name = nameInput.value.trim() || "My Playlist";
        const pages = Array.from(selectedAlbums.values());
        const content = buildAlbumPlaylistNote(name, pages);
        await savePlaylistNote(name, content, overlay);
    };
}

// ── Tool: Add to Favorites ────────────────────────────────
function openAddToFavorites() {
    const { body } = createModal("Add to Favorites");

    const subtitle = body.createEl("div");
    subtitle.textContent = "Tap an album to toggle its Favorite tag.";
    subtitle.style.cssText = "color:#aaa; font-size:13px; margin-bottom:16px;";

    const searchInput = body.createEl("input");
    searchInput.type = "text";
    searchInput.placeholder = "Search albums by title or artist...";
    searchInput.style.cssText = "width:100%; padding:10px 12px; background:#222; border:1px solid #444; border-radius:8px; color:#fff; font-size:15px; box-sizing:border-box; margin-bottom:10px;";

    const resultsLabel = body.createEl("div");
    resultsLabel.style.cssText = "color:#aaa; font-size:13px; margin-bottom:8px;";

    const resultsGrid = body.createEl("div");
    resultsGrid.style.cssText = "display:flex; flex-wrap:wrap; gap:10px; overflow-y:auto; margin-bottom:16px; padding:4px;";

    const statusEl = body.createEl("div");
    statusEl.style.cssText = "font-size:13px; min-height:20px; text-align:center; padding:4px 0;";

    const FAVE_TAG = "Favorite";

    function isFavorited(page) {
        if (!page.tags) return false;
        return page.tags.some(t => t.replace(/^#/, "") === FAVE_TAG);
    }

    async function toggleFavorite(page) {
        const file = app.vault.getAbstractFileByPath(page.file.path);
        if (!file) { statusEl.textContent = "Could not find file."; return; }
        try {
            await app.fileManager.processFrontMatter(file, (fm) => {
                if (!fm.tags) fm.tags = [];
                if (typeof fm.tags === "string") fm.tags = [fm.tags];
                const idx = fm.tags.findIndex(t => t.replace(/^#/, "") === FAVE_TAG);
                if (idx >= 0) {
                    fm.tags.splice(idx, 1);
                    statusEl.style.color = "#aaa";
                    statusEl.textContent = `Removed: ${page.title || page.file.name}`;
                } else {
                    fm.tags.unshift(FAVE_TAG);
                    statusEl.style.color = "#f59e0b";
                    statusEl.textContent = `Added to Favorites: ${page.title || page.file.name}`;
                }
            });
        } catch(e) {
            statusEl.style.color = "#ef4444";
            statusEl.textContent = "Error: " + e.message;
        }
        setTimeout(() => renderResults(), 300);
    }

    function renderResults() {
        resultsGrid.innerHTML = "";
        const query = searchInput.value.toLowerCase().trim();
        const freshPages = dv.pages().where(p => p.tidal_id);
        let results;
        if (!query) {
            results = freshPages.where(p => isFavorited(p))
                .array().sort((a,b) => (a.artist||"").localeCompare(b.artist||""));
            resultsLabel.textContent = results.length > 0
                ? `${results.length} favorited albums — tap to remove`
                : "No favorites yet. Search to add some.";
        } else {
            results = freshPages.where(p =>
                (p.title || p.file.name || "").toLowerCase().includes(query) ||
                (p.artist || "").toLowerCase().includes(query)
            ).array().sort((a,b) => (a.artist||"").localeCompare(b.artist||""));
            resultsLabel.textContent = `${results.length} results — tap to toggle`;
        }
        for (let page of results) {
            const favorited = isFavorited(page);
            const card = resultsGrid.createEl("div");
            card.style.cssText = `
                width: 110px; background: ${favorited ? "#2d1f4e" : "#111"};
                border-radius: 8px; overflow: hidden; cursor: pointer;
                border: 2px solid ${favorited ? "#7c3aed" : "transparent"};
                position: relative;
            `;
            const badge = card.createEl("div");
            badge.textContent = favorited ? "★" : "☆";
            badge.style.cssText = `
                position:absolute; top:5px; left:5px;
                background:rgba(0,0,0,0.75); color:${favorited ? "#f59e0b" : "#666"};
                border-radius:50%; width:22px; height:22px;
                display:flex; align-items:center; justify-content:center;
                font-size:13px; z-index:1;
            `;
            const img = card.createEl("img");
            img.style.cssText = "width:110px; height:110px; object-fit:cover; display:block;";
            const coverFile = getCover(page);
            if (coverFile) img.src = app.vault.getResourcePath(coverFile);
            else img.style.cssText += "background:#333;";
            const info = card.createEl("div");
            info.style.cssText = "padding:6px 8px;";
            const t = info.createEl("div");
            t.style.cssText = "color:#fff; font-size:10px; font-weight:bold; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;";
            t.textContent = page.title || page.file.name;
            const a = info.createEl("div");
            a.style.cssText = "color:#aaa; font-size:9px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;";
            a.textContent = page.artist || "";
            card.onclick = () => toggleFavorite(page);
            resultsGrid.appendChild(card);
        }
    }

    searchInput.addEventListener("input", renderResults);
    renderResults();
    setTimeout(() => searchInput.focus(), 100);
}

// ── Tool: Recently Added ──────────────────────────────────
function openRecentlyAdded() {
    const { body } = createModal("🕐 Recently Added");
    const pages = allPages.array()
        .sort((a,b) => (b.file.ctime||0) - (a.file.ctime||0))
        .slice(0, 50);
    const grid = body.createEl("div");
    grid.style.cssText = "display:flex; flex-wrap:wrap; gap:12px;";
    for (let page of pages) {
        const card = grid.createEl("div");
        card.style.cssText = "width:110px; background:#111; border-radius:10px; overflow:hidden; cursor:pointer;";
        card.onclick = () => app.workspace.openLinkText(page.file.path, "", false);
        const img = card.createEl("img");
        img.style.cssText = "width:110px; height:110px; object-fit:cover; display:block;";
        const coverFile = getCover(page);
        if (coverFile) img.src = app.vault.getResourcePath(coverFile);
        else img.style.cssText += "background:#333;";
        const info = card.createEl("div");
        info.style.cssText = "padding:7px 8px;";
        const t = info.createEl("div");
        t.style.cssText = "color:#fff; font-size:11px; font-weight:bold; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;";
        t.textContent = page.title || page.file.name;
        const a = info.createEl("div");
        a.style.cssText = "color:#aaa; font-size:10px; margin-top:2px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;";
        a.textContent = page.artist || "";
        const d = info.createEl("div");
        d.style.cssText = "color:#555; font-size:9px; margin-top:2px;";
        d.textContent = page.file.ctime ? new Date(page.file.ctime).toLocaleDateString() : "";
    }
}

// ── Tool: Search Albums ───────────────────────────────────
function openSearchAlbums() {
    const { body } = createModal("🔍 Search Albums");
    const searchInput = body.createEl("input");
    searchInput.type = "text";
    searchInput.placeholder = "Search by title, artist, year or tag...";
    searchInput.style.cssText = "width:100%; padding:10px 14px; background:#222; border:1px solid #444; border-radius:8px; color:#fff; font-size:15px; box-sizing:border-box; margin-bottom:10px;";
    const resultsLabel = body.createEl("div");
    resultsLabel.style.cssText = "color:#666; font-size:13px; margin-bottom:10px;";
    resultsLabel.textContent = "Start typing to search...";
    const grid = body.createEl("div");
    grid.style.cssText = "display:flex; flex-wrap:wrap; gap:12px;";

    function doSearch() {
        grid.innerHTML = "";
        const query = searchInput.value.toLowerCase().trim();
        if (!query) { resultsLabel.textContent = "Start typing to search..."; return; }
        const results = allPages.where(p =>
            (p.title || p.file.name || "").toLowerCase().includes(query) ||
            (p.artist || "").toLowerCase().includes(query) ||
            String(p.year || "").includes(query) ||
            (p.tags && p.tags.some(t => t.toLowerCase().includes(query)))
        ).array().sort((a,b) => (a.artist||"").localeCompare(b.artist||""));
        resultsLabel.textContent = `${results.length} results`;
        for (let page of results) {
            const card = grid.createEl("div");
            card.style.cssText = "width:110px; background:#111; border-radius:10px; overflow:hidden; cursor:pointer;";
            card.onclick = () => app.workspace.openLinkText(page.file.path, "", false);
            const img = card.createEl("img");
            img.style.cssText = "width:110px; height:110px; object-fit:cover; display:block;";
            const coverFile = getCover(page);
            if (coverFile) img.src = app.vault.getResourcePath(coverFile);
            else img.style.cssText += "background:#333;";
            const info = card.createEl("div");
            info.style.cssText = "padding:7px 8px;";
            const t = info.createEl("div");
            t.style.cssText = "color:#fff; font-size:11px; font-weight:bold; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;";
            t.textContent = page.title || page.file.name;
            const a = info.createEl("div");
            a.style.cssText = "color:#aaa; font-size:10px; margin-top:2px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;";
            a.textContent = page.artist || "";
            const y = info.createEl("div");
            y.style.cssText = "color:#555; font-size:9px; margin-top:2px;";
            y.textContent = page.year || "";
        }
    }
    searchInput.addEventListener("input", doSearch);
    setTimeout(() => searchInput.focus(), 100);
}

// ── Hub Grid ──────────────────────────────────────────────
const hub = dv.container.createEl("div");
hub.style.cssText = "display:grid; grid-template-columns: repeat(2, 1fr); gap:14px; padding:10px 0;";

const tools = [
    { icon: "🎵", name: "Create Playlist", desc: "Build a playlist by tag or album", action: openPlaylistPicker },
    { icon: "★",  name: "Favorites",       desc: "Toggle the Favorite tag on albums", action: openAddToFavorites },
    { icon: "🕐", name: "Recently Added",  desc: "Your 50 most recently added albums", action: openRecentlyAdded },
    { icon: "🔍", name: "Search Albums",   desc: "Search by title, artist, year or tag", action: openSearchAlbums },
];

for (let tool of tools) {
    const card = hub.createEl("div");
    card.style.cssText = `
        background: #1a1a1a;
        border-radius: 16px;
        padding: 22px 16px;
        cursor: pointer;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.4);
        active-background: #222;
    `;
    card.onclick = tool.action;
    const icon = card.createEl("div");
    icon.textContent = tool.icon;
    icon.style.cssText = "font-size:32px; margin-bottom:10px;";
    const name = card.createEl("div");
    name.textContent = tool.name;
    name.style.cssText = "color:#fff; font-size:15px; font-weight:bold; margin-bottom:5px;";
    const desc = card.createEl("div");
    desc.textContent = tool.desc;
    desc.style.cssText = "color:#666; font-size:11px; line-height:1.4;";
}
```
```dataviewjs
const btn = dv.container.createEl("a");
btn.textContent = "Library";
btn.style.cssText = `
    display: inline-block;
    padding: 10px 20px;
    background: #7c3aed;
    color: #fff;
    border-radius: 10px;
    font-size: 15px;
    font-weight: bold;
    text-decoration: none;
    cursor: pointer;
    margin-bottom: 16px;
`;
btn.onclick = (e) => {
    e.preventDefault();
    app.workspace.openLinkText("Library", "", false);
};
```
