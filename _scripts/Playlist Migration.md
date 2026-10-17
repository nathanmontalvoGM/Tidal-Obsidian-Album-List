```dataviewjs
const FOLDER = "00 Dashboard/Playlists";
const VIEW = "_scripts/playlist";
const DRY_RUN = true;

const files = app.vault.getFiles().filter(f => f.path.startsWith(FOLDER + "/") && f.extension === "md");
const log = dv.container.createEl("pre");

for (const file of files) {
    const text = await app.vault.read(file);
    if (text.includes(`dv.view("${VIEW}"`)) { log.textContent += `ALREADY DONE: ${file.path}\n`; continue; }

    const tagM  = text.match(/const TAGS\s*=\s*(\[[\s\S]*?\]);/);
    const idM   = text.match(/const ALBUM_IDS\s*=\s*(\[[\s\S]*?\]);/);
    const dateM = text.match(/\*\*Created:\*\*\s*(\d{4}-\d{2}-\d{2})/);
    const date  = dateM ? dateM[1] : new Date().toISOString().split("T")[0];

    let body;
    try {
        if (tagM) {
            const tags = Array.from(new Set(JSON.parse(tagM[1]))).sort((a,b) => a.localeCompare(b, undefined, {sensitivity:"base"}));
            body = `# ${file.basename}
**Created:** ${date} | **Tags:** ${tags.join(", ")}

\`\`\`dataviewjs
const TAGS = ${JSON.stringify(tags)};
await dv.view("${VIEW}", { tags: TAGS });
\`\`\`
`;
        } else if (idM) {
            const ids = JSON.parse(idM[1]);
            body = `# ${file.basename}
**Created:** ${date} | **Albums:** ${ids.length}

\`\`\`dataviewjs
const ALBUM_IDS = ${JSON.stringify(ids)};
await dv.view("${VIEW}", { ids: ALBUM_IDS });
\`\`\`
`;
        } else {
            log.textContent += `SKIP (no TAGS/ALBUM_IDS): ${file.path}\n`;
            continue;
        }
    } catch(e) {
        log.textContent += `SKIP (parse error: ${e.message}): ${file.path}\n`;
        continue;
    }

    if (DRY_RUN) log.textContent += `WOULD REWRITE: ${file.path} (${tagM ? "tags" : "ids"})\n`;
    else { await app.vault.modify(file, body); log.textContent += `REWROTE: ${file.path}\n`; }
}
log.textContent += DRY_RUN ? "\nDry run complete." : "\nDone.";
```