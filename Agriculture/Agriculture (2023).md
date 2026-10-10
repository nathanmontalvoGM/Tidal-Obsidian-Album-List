---
title: "Agriculture"
artist: "Agriculture"
year: 2023
tidal_id: 286990986
tags:
  - Blackgaze
  - Blackmetal
  - Postmetal
  - Avantgardemetal
rating:
---

# Agriculture
**Artist:** Agriculture
**Year:** 2023

![[_covers/Agriculture - Agriculture.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/286990986
```
^button-tkqx
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Agriculture%20Agriculture
```
^button-4sqp

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
| 1 | The Glory of the Ocean | 8:08 |  |
| 2 | The Well | 1:54 |  |
| 3 | Look, Pt. 1 | 2:11 |  |
| 4 | Look, Pt. 2 | 5:50 |  |
| 5 | Look, Pt. 3 | 6:23 |  |
| 6 | Relier | 6:53 |  |
