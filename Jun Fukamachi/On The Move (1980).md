---
title: "On The Move"
artist: "Jun Fukamachi"
year: 1980
tidal_id: 164097659
tags:
  - Jazz
  - Fusion
  - Instrumental
  - Japan
rating:
---

# On The Move
**Artist:** Jun Fukamachi
**Year:** 1980

![[_covers/Jun Fukamachi - On The Move.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/164097659
```
^button-nk5q
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Jun%20Fukamachi%20On%20The%20Move
```
^button-625s

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
| 1 | On The Move | 5:48 |  |
| 2 | You're Sorry | 6:28 |  |
| 3 | Letter To N.Y. | 4:56 |  |
| 4 | Departure In The Dark | 6:01 |  |
| 5 | Dance Of Paranoia | 4:46 |  |
| 6 | When I Got Your Wave "Pathetique" | 7:08 |  |
| 7 | Early Evening Lullaby | 6:55 |  |
| 8 | Departure In The Dark - Again | 3:58 |  |
