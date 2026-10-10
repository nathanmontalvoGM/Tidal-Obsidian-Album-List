---
title: "Cannibal"
artist: "Bury Tomorrow"
year: 2020
tidal_id: 146940121
tags:
  - Metalcore
  - Numetal
  - Eargasm
  - MelodicMetalcore
rating:
---

# Cannibal
**Artist:** Bury Tomorrow
**Year:** 2020

![[_covers/Bury Tomorrow - Cannibal.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/146940121
```
^button-b3du
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Bury%20Tomorrow%20Cannibal
```
^button-2xrv

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
| 1 | Choke | 3:47 |  |
| 2 | Cannibal | 4:16 |  |
| 3 | The Grey (VIXI) | 3:59 |  |
| 4 | Imposter | 3:27 |  |
| 5 | Better Below | 3:12 |  |
| 6 | The Agonist | 4:02 |  |
| 7 | Quake | 4:25 |  |
| 8 | Gods & Machines | 4:05 |  |
| 9 | Voice & Truth | 3:06 |  |
| 10 | Cold Sleep | 3:39 |  |
| 11 | Dark, Infinite | 4:01 |  |
