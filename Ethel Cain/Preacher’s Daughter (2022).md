---
title: "Preacher’s Daughter"
artist: "Ethel Cain"
year: 2022
tidal_id: 243731232
tags:
  - Slowcore
  - DreamPop
  - Americana
  - Singersongwriter
rating:
---

# Preacher’s Daughter
**Artist:** Ethel Cain
**Year:** 2022

![[_covers/Ethel Cain - Preacher’s Daughter.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/243731232
```
^button-1485
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Ethel%20Cain%20Preacher%E2%80%99s%20Daughter
```
^button-govh

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
| 1 | Family Tree (intro) | 3:42 |  |
| 2 | American Teenager | 4:18 |  |
| 3 | A House in Nebraska | 7:47 |  |
| 4 | Western Nights | 6:05 |  |
| 5 | Family Tree | 7:11 |  |
| 6 | Hard Times | 5:03 |  |
| 7 | Thoroughfare | 9:28 |  |
| 8 | Gibson Girl | 5:42 |  |
| 9 | Ptolemaea | 6:24 |  |
| 10 | August Underground | 3:41 |  |
| 11 | Televangelism | 3:04 |  |
| 12 | Sun Bleached Flies | 7:36 |  |
| 13 | Strangers | 5:44 |  |
