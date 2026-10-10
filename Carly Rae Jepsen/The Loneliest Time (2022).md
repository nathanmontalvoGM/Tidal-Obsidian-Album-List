---
title: The Loneliest Time
artist: Carly Rae Jepsen
year: 2022
tidal_id: 255225490
tags:
  - Favorite
  - Pop
  - Dancepop
  - Disco
  - Electropop
rating:
---

# The Loneliest Time
**Artist:** Carly Rae Jepsen
**Year:** 2022

![[_covers/Carly Rae Jepsen - The Loneliest Time.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/255225490
```
^button-adh1
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Carly%20Rae%20Jepsen%20The%20Loneliest%20Time
```
^button-7iph

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
| 1 | Surrender My Heart | 2:48 |  |
| 2 | Joshua Tree | 2:29 |  |
| 3 | Talking to Yourself | 2:53 |  |
| 4 | Far Away | 2:59 |  |
| 5 | Sideways | 2:16 |  |
| 6 | Beach House | 2:29 |  |
| 7 | Bends | 3:15 |  |
| 8 | Western Wind | 3:45 |  |
| 9 | So Nice | 3:39 |  |
| 10 | Bad Thing Twice | 3:13 |  |
| 11 | Shooting Star | 3:19 |  |
| 12 | Go Find Yourself or Whatever | 4:44 |  |
| 13 | The Loneliest Time | 4:36 |  |
| 14 | Keep Away | 4:02 |  |
