---
title: "Zach Bryan"
artist: "Zach Bryan"
year: 2023
tidal_id: 311604336
tags:
  - Country
  - Americana
  - Countryrock
  - Alternativecountry
rating:
---

# Zach Bryan
**Artist:** Zach Bryan
**Year:** 2023

![[_covers/Zach Bryan - Zach Bryan.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/311604336
```
^button-b19h
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Zach%20Bryan%20Zach%20Bryan
```
^button-ss24

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
| 1 | Fear & Fridays (poem) | 1:47 |  |
| 2 | Overtime | 3:10 |  |
| 3 | Summertime’s Close | 3:06 |  |
| 4 | East Side of Sorrow | 3:29 |  |
| 5 | Hey Driver | 3:47 |  |
| 6 | Fear and Fridays | 2:51 |  |
| 7 | Ticking | 4:02 |  |
| 8 | Holy Roller | 3:36 |  |
| 9 | Jake’s Piano / Long Island | 5:19 |  |
| 10 | El Dorado | 3:02 |  |
| 11 | I Remember Everything | 3:47 |  |
| 12 | Tourniquet | 3:09 |  |
| 13 | Spotless | 2:49 |  |
| 14 | Tradesman | 3:07 |  |
| 15 | Smaller Acts | 3:07 |  |
| 16 | Oklahoman Son | 4:09 |  |
