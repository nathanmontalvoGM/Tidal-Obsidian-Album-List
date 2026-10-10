---
title: "private music"
artist: "Deftones"
year: 2025
tidal_id: 455128514
tags:
  - Alternativemetal
  - Bestof2022
  - Shoegaze
  - Posthardcore
rating:
---

# private music
**Artist:** Deftones
**Year:** 2025

![[_covers/Deftones - private music.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/455128514
```
^button-9xrs
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Deftones%20private%20music
```
^button-axjc

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
| 1 | my mind is a mountain | 2:50 |  |
| 2 | locked club | 2:52 |  |
| 3 | ecdysis | 3:28 |  |
| 4 | infinite source | 3:32 |  |
| 5 | souvenir | 6:10 |  |
| 6 | cXz | 3:12 |  |
| 7 | i think about you all the time | 4:08 |  |
| 8 | milk of the madonna | 4:08 |  |
| 9 | cut hands | 3:01 |  |
| 10 | ~metal dream | 3:02 |  |
| 11 | departing the body | 5:59 |  |
