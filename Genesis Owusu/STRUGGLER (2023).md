---
title: "STRUGGLER"
artist: "Genesis Owusu"
year: 2023
tidal_id: 294399339
tags:
  - Funk
  - Postpunk
  - Neosoul
  - Synthpunk
rating:
---

# STRUGGLER
**Artist:** Genesis Owusu
**Year:** 2023

![[_covers/Genesis Owusu - STRUGGLER.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/294399339
```
^button-kjkd
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Genesis%20Owusu%20STRUGGLER
```
^button-q2l7

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
| 1 | Leaving the Light | 3:10 |  |
| 2 | The Roach | 2:38 |  |
| 3 | The Old Man | 2:24 |  |
| 4 | See Ya There | 4:39 |  |
| 5 | Freak Boy | 2:28 |  |
| 6 | Tied Up! | 3:09 |  |
| 7 | That’s Life (A Swamp) | 5:26 |  |
| 8 | Balthazar | 3:00 |  |
| 9 | Stay Blessed | 2:57 |  |
| 10 | What Comes Will Come | 3:51 |  |
| 11 | Stuck to the Fan | 4:16 |  |
