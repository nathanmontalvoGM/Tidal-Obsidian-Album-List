---
title: "The Chosen"
artist: "Enterprise Earth"
year: 2022
tidal_id: 333882773
tags:
  - Mathmetal
  - Deathcore
  - Numetal
  - Metalcore
rating:
---

# The Chosen
**Artist:** Enterprise Earth
**Year:** 2022

![[_covers/Enterprise Earth - The Chosen.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/333882773
```
^button-bntk
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Enterprise%20Earth%20The%20Chosen
```
^button-wy6i

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
| 1 | Where Dreams Are Broken | 5:21 |  |
| 2 | Reanimate // Disintegrate | 6:11 |  |
| 3 | Unleash Hell | 6:05 |  |
| 4 | I Have to Escape | 3:35 |  |
| 5 | The Tower | 1:18 |  |
| 6 | They Have No Honor | 4:21 |  |
| 7 | Overpass | 7:47 |  |
| 8 | You Couldn’t Save Me | 5:57 |  |
| 9 | Unhallowed Path | 1:29 |  |
| 10 | Legends Never Die | 4:29 |  |
| 11 | My Blood, Their Satiation | 5:43 |  |
| 12 | Skeleton Key | 4:02 |  |
| 13 | The Chosen | 8:34 |  |
| 14 | Atlas | 2:53 |  |
