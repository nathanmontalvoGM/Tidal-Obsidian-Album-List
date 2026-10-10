---
title: "Lotus"
artist: "Little Simz"
year: 2025
tidal_id: 439599724
tags:
  - Jazzrap
  - Rap
  - Neosoul
  - Hiphop
rating:
---

# Lotus
**Artist:** Little Simz
**Year:** 2025

![[_covers/Little Simz - Lotus.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/439599724
```
^button-fqew
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Little%20Simz%20Lotus
```
^button-nrmt

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
| 1 | Thief | 4:00 |  |
| 2 | Flood | 2:47 |  |
| 3 | Young | 2:50 |  |
| 4 | Only | 3:35 |  |
| 5 | Free | 3:35 |  |
| 6 | Peace | 4:27 |  |
| 7 | Hollow | 2:54 |  |
| 8 | Lion | 2:57 |  |
| 9 | Enough | 3:02 |  |
| 10 | Blood | 4:28 |  |
| 11 | Lotus | 6:35 |  |
| 12 | Lonely | 4:25 |  |
| 13 | Blue | 4:14 |  |
