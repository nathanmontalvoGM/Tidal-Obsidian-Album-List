---
title: "The Dark Pool"
artist: "Thornhill"
year: 2019
tidal_id: 379465533
tags:
  - Metalcore
  - Alternativemetal
  - Interlude
  - Perfection
rating:
---

# The Dark Pool
**Artist:** Thornhill
**Year:** 2019

![[_covers/Thornhill - The Dark Pool.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/379465533
```
^button-704z
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Thornhill%20The%20Dark%20Pool
```
^button-2fm3

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
| 1 | Views From the Sun | 4:08 |  |
| 2 | Nurture | 3:39 |  |
| 3 | The Haze | 4:11 |  |
| 4 | Red Summer | 4:24 |  |
| 5 | In My Skin | 4:06 |  |
| 6 | All the Light We Don’t See | 1:54 |  |
| 7 | Lily & the Moon | 4:01 |  |
| 8 | Coven | 3:37 |  |
| 9 | Human | 4:27 |  |
| 10 | Netherplace | 2:58 |  |
| 11 | Where We Go When We Die | 4:56 |  |
