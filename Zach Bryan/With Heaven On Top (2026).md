---
title: "With Heaven On Top"
artist: "Zach Bryan"
year: 2026
tidal_id: 487981161
tags:
  - Country
  - Americana
  - Countryfolk
  - Countryrock
rating:
---

# With Heaven On Top
**Artist:** Zach Bryan
**Year:** 2026

![[_covers/Zach Bryan - With Heaven On Top.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/487981161
```
^button-7l9d
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Zach%20Bryan%20With%20Heaven%20On%20Top
```
^button-v93i

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
| 1 | Down, Down, Stream | 1:59 |  |
| 2 | Runny Eggs | 3:52 |  |
| 3 | Appetite | 3:05 |  |
| 4 | DeAnn’s Denim | 2:41 |  |
| 5 | Say Why | 2:23 |  |
| 6 | Drowning | 3:05 |  |
| 7 | Santa Fe | 2:54 |  |
| 8 | Skin | 2:55 |  |
| 9 | Dry Deserts | 2:31 |  |
| 10 | Bad News | 3:16 |  |
| 11 | South and Pine | 3:21 |  |
| 12 | Cannonball | 3:57 |  |
| 13 | Slicked Back | 3:51 |  |
| 14 | Anyways | 3:23 |  |
| 15 | If They Come Lookin’ | 2:27 |  |
| 16 | Rivers and Creeks | 3:35 |  |
| 17 | Plastic Cigarette | 3:05 |  |
| 18 | You Can Still Come Home | 3:41 |  |
| 19 | Aeroplane | 2:20 |  |
| 20 | Always Willin’ | 4:05 |  |
| 21 | Miles | 3:30 |  |
| 22 | All Good Things Past | 4:02 |  |
| 23 | Camper | 2:15 |  |
| 24 | Sundown Girls | 2:02 |  |
| 25 | With Heaven On Top | 3:53 |  |
