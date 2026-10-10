---
title: "The Saberlight Chronicles"
artist: "Fellowship"
year: 2022
tidal_id: 332852788
tags:
  - Powermetal
  - Symphonicmetal
rating:
---

# The Saberlight Chronicles
**Artist:** Fellowship
**Year:** 2022

![[_covers/Fellowship - The Saberlight Chronicles.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/332852788
```
^button-jpyv
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Fellowship%20The%20Saberlight%20Chronicles
```
^button-2cr7

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
| 1 | Until the Fires Die | 5:14 |  |
| 2 | Atlas | 4:54 |  |
| 3 | Glory Days | 4:53 |  |
| 4 | Oak and Ash | 4:52 |  |
| 5 | Hearts Upon the Hill | 4:25 |  |
| 6 | Scars and Shrapnel Wounds | 3:55 |  |
| 7 | The Hours of Wintertime | 5:44 |  |
| 8 | Glint | 5:10 |  |
| 9 | The Saint Beyond the River | 4:06 |  |
| 10 | Silhouette | 4:25 |  |
| 11 | Still Enough | 5:39 |  |
| 12 | Avalon | 9:08 |  |
