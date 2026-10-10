---
title: Persona
artist: half·alive
year: 2024
tidal_id: 387255275
tags:
  - Indiepop
  - Indierock
  - Poprock
  - Synthpop
rating:
---

# Persona
**Artist:** half·alive
**Year:** 2024

![[_covers/half·alive - Persona.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/387255275
```
^button-090p
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=half%C2%B7alive%20Persona
```
^button-fg9n

## Tracklist

```dataviewjs
const page = dv.current();
const content = await app.vault.read(app.vault.getAbstractFileByPath(page.file.path));
const rows = content.match(/^\|\s*[\d-]+\s*\|.+\|\s*([0-9.]+)\s*\|$/gm) || [];
const ratings = rows.map(r => {
    const cols = r.split('|').map(c => c.trim());
    return parseFloat(cols[cols.length - 2]);
}).filter(v => !isNaN(v) && v > 0);
const el = dv.container.createEl('div');
el.style.cssText = 'font-size:18px; font-weight:bold; color:#fff; padding:6px 0 12px 0;';
if (ratings.length > 0) {
    const avg = (ratings.reduce((a, b) => a + b, 0) / ratings.length).toFixed(1);
    el.textContent = 'Overall Rating: ' + avg + ' / 10 (' + ratings.length + ' tracks rated)';
} else {
    el.style.color = '#666';
    el.textContent = 'Overall Rating: No tracks rated yet';
}
```

| # | Title | Duration | Rating /10 |
|---|-------|----------|------------|
| 1 | Persona | 0:32 |  |
| 2 | Sophie’s House | 4:15 |  |
| 3 | Automatic | 3:13 |  |
| 4 | People | 3:26 |  |
| 5 | Bleed It Out | 2:45 |  |
| 6 | Long Drive | 3:57 |  |
| 7 | Lie, Lie | 2:32 |  |
| 8 | All My Love (Imperative) | 2:08 |  |
| 9 | The Point | 2:43 |  |
| 10 | Songs | 3:20 |  |
| 11 | Thank You | 2:58 |  |
