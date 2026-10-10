---
title: "Soft Spot"
artist: "Honningbarna"
year: 2025
tidal_id: 411499794
tags:
  - DancePunk
  - Posthardcore
  - Noiserock
  - Synthpunk
rating:
---

# Soft Spot
**Artist:** Honningbarna
**Year:** 2025

![[_covers/Honningbarna - Soft Spot.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/411499794
```
^button-b9gf
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Honningbarna%20Soft%20Spot
```
^button-j8qr

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
| 1 | Alt går over, noe varer | 3:30 |  |
| 2 | Schäfer | 2:20 |  |
| 3 | Amor fati | 3:22 |  |
| 4 | MP5 | 2:45 |  |
| 5 | Festen som aldri stopper | 3:20 |  |
| 6 | God gutt | 3:28 |  |
| 7 | Hvilke splinter | 2:42 |  |
| 8 | Av liv treffer | 0:48 |  |
| 9 | King Spud | 3:05 |  |
| 10 | Rød bic | 2:51 |  |
| 11 | Heute ist mein tag | 3:03 |  |
| 12 | Ditt hjertes Hizbollah | 3:47 |  |
| 13 | Ultraøyer | 4:19 |  |
