---
title: "Oxidized"
artist: "Frontierer"
year: 2021
tidal_id: 193635707
tags:
  - Noise
  - Glitch
  - Mathcore
  - Hardcore
rating:
---

# Oxidized
**Artist:** Frontierer
**Year:** 2021

![[_covers/Frontierer - Oxidized.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/193635707
```
^button-13ui
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Frontierer%20Oxidized
```
^button-cz79

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
| 1 | Heirloom | 3:18 |  |
| 2 | Corrosive Wash | 3:27 |  |
| 3 | Opaque Horizon | 2:58 |  |
| 4 | Death/ | 2:25 |  |
| 5 | Disintegrative | 3:32 |  |
| 6 | This Magnetic Drift | 4:27 |  |
| 7 | LK WX | 2:32 |  |
| 8 | Southern Hemorrhage | 2:45 |  |
| 9 | SVVANS | 2:01 |  |
| 10 | Stereopticon | 3:20 |  |
| 11 | Removal of the Copper Iris and the Lightning Pill | 2:38 |  |
| 12 | Motherboard | 2:20 |  |
| 13 | Daydark | 4:12 |  |
| 14 | Glacial Plasma | 3:23 |  |
| 15 | The Damage and the Sift | 3:21 |  |
| 16 | /Hope | 2:51 |  |
