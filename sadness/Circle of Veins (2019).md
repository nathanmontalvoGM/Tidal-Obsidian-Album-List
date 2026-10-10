---
title: "Circle of Veins"
artist: "sadness"
year: 2019
tidal_id: 118097242
tags:
  - Blackgaze
  - Atmosphericmetal
  - Depressiveblackmetal
  - Rock
rating:
---

# Circle of Veins
**Artist:** sadness
**Year:** 2019

![[_covers/sadness - Circle of Veins.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/118097242
```
^button-h83t
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=sadness%20Circle%20of%20Veins
```
^button-wnhf

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
| 1 | Eye of Prima | 8:42 |  |
| 2 | Cerrien | 9:05 |  |
| 3 | Lana | 7:22 |  |
| 4 | The Spring Sun on Summer Rain | 4:40 |  |
| 5 | Eye of Prima (alternate version) | 7:41 |  |
| 6 | I Follow Rivers | 25:42 |  |
