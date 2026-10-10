---
title: "SLICE"
artist: "O."
year: 2023
tidal_id: 329837716
tags:
  - Nmf231124
  - Experimentalrock
  - Jazzrock
rating:
---

# SLICE
**Artist:** O.
**Year:** 2023

![[_covers/O - SLICE.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/329837716
```
^button-y5rx
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=O.%20SLICE
```
^button-5gkf

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
| 1 | Slice | 3:24 |  |
| 2 | Moon | 4:43 |  |
| 3 | Grouchy | 3:30 |  |
| 4 | ATM | 6:12 |  |
