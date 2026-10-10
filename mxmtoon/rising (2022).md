---
title: "rising"
artist: "mxmtoon"
year: 2022
tidal_id: 246281740
tags:
  - Pop
  - Indiepop
rating:
---

# rising
**Artist:** mxmtoon
**Year:** 2022

![[_covers/mxmtoon - rising.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/246281740
```
^button-mpnb
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=mxmtoon%20rising
```
^button-avw8

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
| 1 | mona lisa | 3:10 |  |
| 2 | learn to love you | 2:12 |  |
| 3 | victim of nostalgia | 2:36 |  |
| 4 | sad disco | 3:03 |  |
| 5 | frown | 2:19 |  |
| 6 | florida | 2:47 |  |
| 7 | scales | 2:39 |  |
| 8 | growing pains | 2:42 |  |
| 9 | dizzy | 2:54 |  |
| 10 | haze | 3:11 |  |
| 11 | dance (end of the world) | 2:38 |  |
| 12 | coming of age | 2:38 |  |
