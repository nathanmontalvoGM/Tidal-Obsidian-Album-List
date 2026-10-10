---
title: "Corpo-Mente"
artist: "Corpo-Mente"
year: 2015
tidal_id: 41875776
tags:
  - Experimentalrock
  - Avantgarde
  - Downtempo
  - Electronicore
rating:
---

# Corpo-Mente
**Artist:** Corpo-Mente
**Year:** 2015

![[_covers/Corpo-Mente - Corpo-Mente.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/41875776
```
^button-83hu
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Corpo-Mente%20Corpo-Mente
```
^button-kcxa

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
| 1 | Scylla | 4:22 |  |
| 2 | Arsalein | 4:07 |  |
| 3 | Fia | 3:45 |  |
| 4 | Velandi | 3:30 |  |
| 5 | Dorma | 5:23 |  |
| 6 | Dulcin | 5:44 |  |
| 7 | Equus | 2:47 |  |
| 8 | Ort | 3:57 |  |
| 9 | Saelli | 3:38 |  |
| 10 | Encell | 3:14 |  |
