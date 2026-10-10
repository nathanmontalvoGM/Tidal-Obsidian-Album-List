---
title: "Bronco"
artist: "Orville Peck"
year: 2022
tidal_id: 223676616
tags:
  - Country
  - Guitar
  - Americana
  - Contemporarycountry
rating:
---

# Bronco
**Artist:** Orville Peck
**Year:** 2022

![[_covers/Orville Peck - Bronco.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/223676616
```
^button-m96h
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Orville%20Peck%20Bronco
```
^button-eq23

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
| 1 | Daytona Sand | 3:15 |  |
| 2 | The Curse of the Blackened Eye | 4:10 |  |
| 3 | Outta Time | 4:19 |  |
| 4 | Lafayette | 3:02 |  |
| 5 | C’mon Baby, Cry | 3:31 |  |
| 6 | Iris Rose | 2:49 |  |
| 7 | Kalahari Down | 4:50 |  |
| 8 | Bronco | 3:29 |  |
| 9 | Trample Out the Days | 3:48 |  |
| 10 | Blush | 3:37 |  |
| 11 | Hexie Mountains | 3:12 |  |
| 12 | Let Me Drown | 3:20 |  |
| 13 | Any Turn | 2:16 |  |
| 14 | City of Gold | 4:04 |  |
| 15 | All I Can Say | 3:56 |  |
