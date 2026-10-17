---
title: "Landfall"
artist: "Wage War"
year: 2026
tidal_id: 566410214
tags:
  - Alternativemetal
  - Melodicmetalcore
  - Metalcore
  - Numetal
rating:
---

# Landfall
**Artist:** Wage War
**Year:** 2026

![[_covers/Wage War - Landfall.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/566410214
```
^button-xrm8
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Wage%20War%20Landfall
```
^button-eef9

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
| 1 | Landfall | 3:42 |  |
| 2 | Sweet Dreams | 3:07 |  |
| 3 | Silk | 3:10 |  |
| 4 | Figure 8 | 3:05 |  |
| 5 | God Complex | 2:55 |  |
| 6 | Stay With Me | 3:39 |  |
| 7 | Silence Has Spoken | 3:11 |  |
| 8 | Way of Pain | 3:03 |  |
| 9 | Red Dot | 2:10 |  |
| 10 | Blindfold | 3:14 |  |
| 11 | Spellbound | 3:23 |  |
| 12 | Song of the Swamp | 3:18 |  |
| 13 | Silhouette | 4:56 |  |
