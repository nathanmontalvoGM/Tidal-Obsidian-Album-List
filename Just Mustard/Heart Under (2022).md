---
title: "Heart Under"
artist: "Just Mustard"
year: 2022
tidal_id: 403501716
tags:
  - Shoegaze
  - Postpunk
  - Indierock
  - Gothicrock
rating:
---

# Heart Under
**Artist:** Just Mustard
**Year:** 2022

![[_covers/Just Mustard - Heart Under.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/403501716
```
^button-2y3a
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Just%20Mustard%20Heart%20Under
```
^button-10cr

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
| 1 | 23 | 4:53 |  |
| 2 | Still | 4:05 |  |
| 3 | I Am You | 3:50 |  |
| 4 | Seed | 4:48 |  |
| 5 | Blue Chalk | 5:01 |  |
| 6 | Early | 3:49 |  |
| 7 | Sore | 4:24 |  |
| 8 | Mirrors | 4:17 |  |
| 9 | In Shade | 4:38 |  |
| 10 | Rivers | 5:27 |  |
