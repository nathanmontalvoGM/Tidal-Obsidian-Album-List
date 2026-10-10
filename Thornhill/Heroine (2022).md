---
title: "Heroine"
artist: "Thornhill"
year: 2022
tidal_id: 379540602
tags:
  - Alternativemetal
  - Shoegaze
  - Alternativerock
  - Metalcore
rating:
---

# Heroine
**Artist:** Thornhill
**Year:** 2022

![[_covers/Thornhill - Heroine.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/379540602
```
^button-yjbw
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Thornhill%20Heroine
```
^button-wq0x

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
| 1 | The Hellfire Club | 5:06 |  |
| 2 | Leather Wings | 3:21 |  |
| 3 | Blue Velvet | 4:50 |  |
| 4 | Arkangel | 4:10 |  |
| 5 | Valentine | 3:13 |  |
| 6 | Casanova | 3:58 |  |
| 7 | Something Terrible Came with the Rain | 2:30 |  |
| 8 | Hollywood | 5:09 |  |
| 9 | Raw | 3:42 |  |
| 10 | Varsity Hearts | 4:59 |  |
| 11 | Heroine | 4:59 |  |
