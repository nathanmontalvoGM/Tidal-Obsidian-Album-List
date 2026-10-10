---
title: "The War to End All Wars"
artist: "Sabaton"
year: 2022
tidal_id: 197973453
tags:
  - Powermetal
  - Wwi
  - Heavymetal
  - Worldwari
rating:
---

# The War to End All Wars
**Artist:** Sabaton
**Year:** 2022

![[_covers/Sabaton - The War to End All Wars.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/197973453
```
^button-jc92
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Sabaton%20The%20War%20to%20End%20All%20Wars
```
^button-2kmr

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
| 1 | Stormtroopers | 3:56 |  |
| 2 | Dreadnought | 4:58 |  |
| 3 | The Unkillable Soldier | 4:11 |  |
| 4 | Soldier of Heaven | 3:38 |  |
| 5 | Hellfighters | 3:26 |  |
| 6 | Race to the Sea | 3:47 |  |
| 7 | Lady of the Dark | 3:03 |  |
| 8 | The Valley of Death | 4:13 |  |
| 9 | Christmas Truce | 5:18 |  |
| 10 | Versailles | 4:14 |  |
