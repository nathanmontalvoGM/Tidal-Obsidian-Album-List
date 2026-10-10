---
title: "Super Snõõper"
artist: "Snõõper"
year: 2023
tidal_id: 475814696
tags:
  - Postpunk
  - GaragePunk
  - Punk
  - Punkrock
rating:
---

# Super Snõõper
**Artist:** Snõõper
**Year:** 2023

![[_covers/Snõõper - Super Snõõper.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/475814696
```
^button-tpy8
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Sn%C3%B5%C3%B5per%20Super%20Sn%C3%B5%C3%B5per
```
^button-uorx

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
| 1 | Stretching | 1:08 |  |
| 2 | Bed Bugs | 0:34 |  |
| 3 | Pod | 1:41 |  |
| 4 | Fitness | 1:55 |  |
| 5 | Powerball | 1:03 |  |
| 6 | Xerox | 1:09 |  |
| 7 | Fruit Fly | 0:55 |  |
| 8 | Inventory | 0:49 |  |
| 9 | Defect | 1:38 |  |
| 10 | Town Topic | 1:33 |  |
| 11 | Music for Spies | 1:33 |  |
| 12 | Microbe | 1:59 |  |
| 13 | Unable | 1:32 |  |
| 14 | Running | 5:22 |  |
