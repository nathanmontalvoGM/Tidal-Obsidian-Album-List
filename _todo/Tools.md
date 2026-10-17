# 🎵 Tools
```dataviewjs
const allPages = dv.pages().where(p => p.tidal_id);

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

// ── Modal System ──────────────────────────────────────────
function createModal(title) {
    const overlay = document.body.createEl("div");
    overlay.style.cssText = `
        position: fixed; inset: 0;
        background: rgba(0,0,0,0.75);
        z-index: 9999;
        display: flex;
        align-items: center;
        justify-content: center;
    `;

    const modal = overlay.createEl("div");
    modal.style.cssText = `
        background: #1a1a1a;
        border-radius: 14px;
        width: 90vw;
        max-width: 1000px;
        max-height: 85vh;
        display: flex;
        flex-direction: column;
        box-shadow: 0 20px 60px rgba(0,0,0,0.8);
        overflow: hidden;
    `;

    // Header
    const header = modal.createEl("div");
    header.style.cssText = `
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 16px 20px;
        border-bottom: 1px solid #333;
        flex-shrink: 0;
    `;
    const titleEl = header.createEl("div");
    titleEl.textContent = title;
    titleEl.style.cssText = "color:#fff; font-size:18px; font-weight:bold;";

    const closeBtn = header.createEl("button");
    closeBtn.textContent = "✕";
    closeBtn.style.cssText = `
        background: #333; border: none; border-radius: 6px;
        color: #aaa; font-size:16px; width:32px; height:32px;
        cursor:pointer; display:flex; align-items:center; justify-content:center;
    `;
    closeBtn.onclick = () => overlay.remove();
    overlay.onclick = (e) => { if (e.target === overlay) overlay.remove(); };

    // Body
    const body = modal.createEl("div");
    body.style.cssText = "padding: 20px; overflow-y: auto; flex: 1;";

    return { overlay, modal, body };
}

// ── Tool: Create Playlist by Tag ──────────────────────────
function openPlaylistTool() {
    const { overlay, body } = createModal("🎵 Create Playlist by Tag");

    // Get all tags grouped by category
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

    // Also collect any tags from albums not in categories
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

    // ── Playlist name ──
    const nameRow = body.createEl("div");
    nameRow.style.cssText = "display:flex; align-items:center; gap:12px; margin-bottom:16px;";
    const nameLabel = nameRow.createEl("label");
    nameLabel.textContent = "Playlist Name:";
    nameLabel.style.cssText = "color:#aaa; font-size:13px; white-space:nowrap;";
    const nameInput = nameRow.createEl("input");
    nameInput.type = "text";
    nameInput.value = "My Playlist";
    nameInput.style.cssText = "flex:1; padding:8px 12px; background:#222; border:1px solid #444; border-radius:6px; color:#fff; font-size:14px;";

    // ── Search + match mode row ──
    const controlRow = body.createEl("div");
    controlRow.style.cssText = "display:flex; gap:10px; align-items:center; margin-bottom:14px; flex-wrap:wrap;";

    const searchInput = controlRow.createEl("input");
    searchInput.type = "text";
    searchInput.placeholder = "Search tags...";
    searchInput.style.cssText = "flex:1; min-width:160px; padding:7px 12px; background:#222; border:1px solid #444; border-radius:6px; color:#fff; font-size:13px;";

    const matchLabel = controlRow.createEl("div");
    matchLabel.textContent = "Match:";
    matchLabel.style.cssText = "color:#aaa; font-size:13px;";

    function modeBtn(label, mode) {
        const btn = controlRow.createEl("button");
        btn.textContent = label;
        btn.style.cssText = `padding:5px 14px; border-radius:20px; border:1px solid #444; background:#222; color:#aaa; font-size:12px; cursor:pointer;`;
        btn.onclick = () => {
            matchMode = mode;
            renderTagGrid();
            renderPreview();
            anyBtn.style.background = matchMode === "any" ? "#7c3aed" : "#222";
            anyBtn.style.borderColor = matchMode === "any" ? "#7c3aed" : "#444";
            anyBtn.style.color = matchMode === "any" ? "#fff" : "#aaa";
            allBtn.style.background = matchMode === "all" ? "#7c3aed" : "#222";
            allBtn.style.borderColor = matchMode === "all" ? "#7c3aed" : "#444";
            allBtn.style.color = matchMode === "all" ? "#fff" : "#aaa";
        };
        return btn;
    }
    const anyBtn = modeBtn("Any (OR)", "any");
    const allBtn = modeBtn("All (AND)", "all");
    anyBtn.style.background = "#7c3aed"; anyBtn.style.borderColor = "#7c3aed"; anyBtn.style.color = "#fff";

    // ── Category filter pills ──
    const catRow = body.createEl("div");
    catRow.style.cssText = "display:flex; flex-wrap:wrap; gap:6px; margin-bottom:12px;";

    function renderCatPills() {
        catRow.innerHTML = "";
        const cats = ["All", ...Object.keys(tagCategories)];
        for (let cat of cats) {
            const pill = catRow.createEl("button");
            pill.textContent = cat;
            pill.style.cssText = `
                padding:4px 12px; border-radius:20px; font-size:12px; cursor:pointer;
                border:1px solid ${activeCategory === cat ? "#7c3aed" : "#444"};
                background:${activeCategory === cat ? "#7c3aed" : "#222"};
                color:${activeCategory === cat ? "#fff" : "#aaa"};
            `;
            pill.onclick = () => { activeCategory = cat; renderCatPills(); renderTagGrid(); };
        }
    }
    renderCatPills();

    // ── Tag grid ──
    const tagGrid = body.createEl("div");
    tagGrid.style.cssText = "display:flex; flex-wrap:wrap; gap:6px; margin-bottom:16px; max-height:160px; overflow-y:auto; padding:4px;";

    function getVisibleTags() {
        const search = searchInput.value.toLowerCase();
        let tags = activeCategory === "All"
            ? Array.from(tagSet).sort()
            : (tagCategories[activeCategory] || []);
        if (search) tags = tags.filter(t => t.toLowerCase().includes(search));
        return tags;
    }

    function renderTagGrid() {
        tagGrid.innerHTML = "";
        for (let tag of getVisibleTags()) {
            const btn = tagGrid.createEl("button");
            btn.textContent = tag;
            btn.style.cssText = `
                padding:4px 12px; border-radius:20px; font-size:12px; cursor:pointer;
                border:1px solid ${selectedTags.has(tag) ? "#7c3aed" : "#444"};
                background:${selectedTags.has(tag) ? "#7c3aed" : "#222"};
                color:${selectedTags.has(tag) ? "#fff" : "#aaa"};
                transition: all 0.15s;
            `;
            btn.onclick = () => {
                selectedTags.has(tag) ? selectedTags.delete(tag) : selectedTags.add(tag);
                renderTagGrid();
                renderPreview();
            };
        }
    }
    renderTagGrid();
    searchInput.addEventListener("input", renderTagGrid);

    // ── Selected tags display ──
    const selectedRow = body.createEl("div");
    selectedRow.style.cssText = "margin-bottom:12px;";

    // ── Preview ──
    const previewLabel = body.createEl("div");
    previewLabel.style.cssText = "color:#aaa; font-size:13px; margin-bottom:8px;";

    const previewGrid = body.createEl("div");
    previewGrid.style.cssText = "display:flex; flex-wrap:wrap; gap:10px; margin-bottom:16px; max-height:220px; overflow-y:auto;";

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

        // Show selected tags
        if (selectedTags.size > 0) {
            const selLabel = selectedRow.createEl("div");
            selLabel.textContent = "Selected: ";
            selLabel.style.cssText = "color:#aaa; font-size:12px; margin-bottom:6px;";
            const selPills = selectedRow.createEl("div");
            selPills.style.cssText = "display:flex; flex-wrap:wrap; gap:5px;";
            for (let tag of selectedTags) {
                const pill = selPills.createEl("span");
                pill.textContent = tag + " ✕";
                pill.style.cssText = "padding:3px 10px; background:#7c3aed; border-radius:20px; color:#fff; font-size:11px; cursor:pointer;";
                pill.onclick = () => { selectedTags.delete(tag); renderTagGrid(); renderPreview(); };
            }
        }

        const matches = getMatchingPages();
        previewLabel.textContent = selectedTags.size === 0
            ? "Select tags above to preview albums"
            : `${matches.length} albums match`;

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

    // ── Create button ──
    const createBtn = body.createEl("button");
    createBtn.textContent = "Create Playlist Note";
    createBtn.style.cssText = "padding:10px 24px; background:#7c3aed; border:none; border-radius:8px; color:#fff; font-size:14px; font-weight:bold; cursor:pointer; width:100%;";
    createBtn.onclick = async () => {
        const matches = getMatchingPages();
        if (matches.length === 0) { alert("No albums match!"); return; }
        const name = nameInput.value.trim() || "My Playlist";
        const date = new Date().toISOString().split("T")[0];
        let noteContent = `# ${name}\n**Created:** ${date} | **Tags:** ${Array.from(selectedTags).join(", ")} | **Albums:** ${matches.length}\n\n---\n\n`;
        for (let page of matches) {
            const albumTitle = page.file.name.replace(/\s\(\d{4}\)$/, "");
            const coverFile = getCover(page);
            noteContent += `## ${page.title || albumTitle}\n`;
            noteContent += `**Artist:** ${page.artist||""} | **Year:** ${page.year||""}\n\n`;
            if (coverFile) noteContent += `![[${coverFile.path}]]\n\n`;
            noteContent += `[[${page.file.path}|Open Note]] | [Play on Tidal](tidal://album/${page.tidal_id})\n\n---\n\n`;
        }
        const filename = `Playlists/${name}.md`;
        try {
            const existing = app.vault.getAbstractFileByPath(filename);
            if (existing) await app.vault.modify(existing, noteContent);
            else await app.vault.create(filename, noteContent);
            overlay.remove();
            app.workspace.openLinkText(filename, "", false);
        } catch(e) {
            try {
                await app.vault.createFolder("Playlists");
                await app.vault.create(filename, noteContent);
                overlay.remove();
                app.workspace.openLinkText(filename, "", false);
            } catch(e2) { alert("Error: " + e2); }
        }
    };
}

// ── Tool: Recently Added ──────────────────────────────────
function openRecentlyAdded() {
    const { body } = createModal("🕐 Recently Added");

    const pages = allPages.array()
        .sort((a,b) => (b.file.ctime || 0) - (a.file.ctime || 0))
        .slice(0, 50);

    const grid = body.createEl("div");
    grid.style.cssText = "display:flex; flex-wrap:wrap; gap:14px;";

    for (let page of pages) {
        const card = grid.createEl("div");
        card.style.cssText = "width:140px; background:#111; border-radius:10px; overflow:hidden; cursor:pointer; transition:transform 0.2s;";
        card.onmouseenter = () => card.style.transform = "scale(1.05)";
        card.onmouseleave = () => card.style.transform = "scale(1.0)";
        card.onclick = () => app.workspace.openLinkText(page.file.path, "", false);

        const img = card.createEl("img");
        img.style.cssText = "width:140px; height:140px; object-fit:cover; display:block;";
        const coverFile = getCover(page);
        if (coverFile) img.src = app.vault.getResourcePath(coverFile);
        else img.style.cssText += "background:#333;";

        const info = card.createEl("div");
        info.style.cssText = "padding:8px;";
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

    const searchRow = body.createEl("div");
    searchRow.style.cssText = "display:flex; gap:10px; margin-bottom:16px;";

    const searchInput = searchRow.createEl("input");
    searchInput.type = "text";
    searchInput.placeholder = "Search by title, artist, year or tag...";
    searchInput.style.cssText = "flex:1; padding:9px 14px; background:#222; border:1px solid #444; border-radius:8px; color:#fff; font-size:14px;";

    const resultsLabel = body.createEl("div");
    resultsLabel.style.cssText = "color:#666; font-size:12px; margin-bottom:10px;";
    resultsLabel.textContent = "Start typing to search...";

    const grid = body.createEl("div");
    grid.style.cssText = "display:flex; flex-wrap:wrap; gap:14px;";

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
            card.style.cssText = "width:140px; background:#111; border-radius:10px; overflow:hidden; cursor:pointer; transition:transform 0.2s;";
            card.onmouseenter = () => card.style.transform = "scale(1.05)";
            card.onmouseleave = () => card.style.transform = "scale(1.0)";
            card.onclick = () => app.workspace.openLinkText(page.file.path, "", false);

            const img = card.createEl("img");
            img.style.cssText = "width:140px; height:140px; object-fit:cover; display:block;";
            const coverFile = getCover(page);
            if (coverFile) img.src = app.vault.getResourcePath(coverFile);
            else img.style.cssText += "background:#333;";

            const info = card.createEl("div");
            info.style.cssText = "padding:8px;";
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
hub.style.cssText = "display:flex; flex-wrap:wrap; gap:20px; padding:10px 0;";

const tools = [
    {
        icon: "🎵",
        name: "Create Playlist",
        desc: "Build a playlist by selecting tags",
        action: openPlaylistTool
    },
    {
        icon: "🕐",
        name: "Recently Added",
        desc: "Browse your 50 most recently added albums",
        action: openRecentlyAdded
    },
    {
        icon: "🔍",
        name: "Search Albums",
        desc: "Search by title, artist, year or tag",
        action: openSearchAlbums
    },
];

for (let tool of tools) {
    const card = hub.createEl("div");
    card.style.cssText = `
        width: 200px;
        background: #1a1a1a;
        border-radius: 14px;
        padding: 24px 20px;
        cursor: pointer;
        transition: transform 0.2s, background 0.2s;
        box-shadow: 0 4px 12px rgba(0,0,0,0.4);
        text-align: center;
    `;
    card.onmouseenter = () => { card.style.transform = "scale(1.04)"; card.style.background = "#222"; };
    card.onmouseleave = () => { card.style.transform = "scale(1.0)"; card.style.background = "#1a1a1a"; };
    card.onclick = tool.action;

    const icon = card.createEl("div");
    icon.textContent = tool.icon;
    icon.style.cssText = "font-size:36px; margin-bottom:12px;";

    const name = card.createEl("div");
    name.textContent = tool.name;
    name.style.cssText = "color:#fff; font-size:15px; font-weight:bold; margin-bottom:6px;";

    const desc = card.createEl("div");
    desc.textContent = tool.desc;
    desc.style.cssText = "color:#666; font-size:12px; line-height:1.4;";
}
```