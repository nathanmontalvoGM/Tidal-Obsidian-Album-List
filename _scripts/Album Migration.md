```dataviewjs
const DRY_RUN = true;
const VIEW = "_scripts/album";

const albums = dv.pages().where(p => p.tidal_id).array();
const log = dv.container.createEl("pre");
let rewrote = 0, skipped = 0, already = 0, preview = null;

for (const p of albums) {
    const file = app.vault.getAbstractFileByPath(p.file.path);
    const text = (await app.vault.read(file)).replace(/\r\n/g, "\n");

    const fm = text.match(/^---\n[\s\S]*?\n---\n?/);
    if (!fm) { log.textContent += `SKIP (no frontmatter): ${file.path}\n`; skipped++; continue; }

    const rest = text.slice(fm[0].length);
    if (rest.includes(`dv.view("${VIEW}")`)) { already++; continue; }

    const lines = rest.split("\n");
    const start = lines.findIndex(l => /^\|\s*#\s*\|/.test(l));
    if (start < 0) { log.textContent += `SKIP (no tracklist table): ${file.path}\n`; skipped++; continue; }
    let end = start;
    while (end < lines.length && lines[end].trim().startsWith("|")) end++;

    const table = lines.slice(start, end).join("\n");
    const after = lines.slice(end).join("\n").trim();

    const body = `${fm[0].trimEnd()}\n\n\`\`\`dataviewjs\nawait dv.view("${VIEW}");\n\`\`\`\n\n${table}\n${after ? `\n${after}\n` : ""}`;

    if (!preview) preview = `── Preview: ${file.path} ──\n${body}\n`;
    if (!DRY_RUN) await app.vault.modify(file, body);
    rewrote++;
}

log.textContent += `\n${DRY_RUN ? "Would rewrite" : "Rewrote"}: ${rewrote} | Already converted: ${already} | Skipped: ${skipped}\n\n${preview || ""}`;
```