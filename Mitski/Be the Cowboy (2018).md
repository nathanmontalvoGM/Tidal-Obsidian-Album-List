---
title: "Be the Cowboy"
artist: "Mitski"
year: 2018
tidal_id: 91826107
tags:
  - ArtPop
  - Indierock
  - Indiepop
  - ArtRock
rating:
---

# Be the Cowboy
**Artist:** Mitski
**Year:** 2018

![[_covers/Mitski - Be the Cowboy.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/91826107
```
^button-6dz9
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Mitski%20Be%20the%20Cowboy
```
^button-jcqx

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
| 1 | Geyser | 2:23 |  |
| 2 | Why Didn’t You Stop Me? | 2:21 |  |
| 3 | Old Friend | 1:52 |  |
| 4 | A Pearl | 2:36 |  |
| 5 | Lonesome Love | 1:50 |  |
| 6 | Remember My Name | 2:15 |  |
| 7 | Me and My Husband | 2:17 |  |
| 8 | Come Into the Water | 1:32 |  |
| 9 | Nobody | 3:13 |  |
| 10 | Pink in the Night | 2:16 |  |
| 11 | A Horse Named Cold Air | 2:03 |  |
| 12 | Washing Machine Heart | 2:08 |  |
| 13 | Blue Light | 1:43 |  |
| 14 | Two Slow Dancers | 3:59 |  |
