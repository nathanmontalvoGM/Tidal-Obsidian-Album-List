---
title: Nurture
artist: Porter Robinson
year: 2021
tidal_id: 181171322
tags:
  - Favorite
  - Electropop
  - Electronicore
  - Wsum917fmmadison
  - TheMethod
rating:
---

# Nurture
**Artist:** Porter Robinson
**Year:** 2021

![[_covers/Porter Robinson - Nurture.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/181171322
```
^button-kysv
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Porter%20Robinson%20Nurture
```
^button-mu0t

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
| 1 | Lifelike | 1:34 |  |
| 2 | Look at the Sky | 5:09 |  |
| 3 | Get Your Wish | 3:38 |  |
| 4 | Wind Tempos | 6:04 |  |
| 5 | Musician | 3:58 |  |
| 6 | do-re-mi-fa-so-la-ti-do | 3:34 |  |
| 7 | Mother | 3:46 |  |
| 8 | dullscythe | 4:00 |  |
| 9 | Sweet Time | 4:11 |  |
| 10 | Mirror | 5:06 |  |
| 11 | Something Comforting | 4:41 |  |
| 12 | Blossom | 3:46 |  |
| 13 | Unfold | 4:45 |  |
| 14 | Trying to Feel Alive | 4:39 |  |
| 15 | fullmoon lullaby | 4:02 |  |
