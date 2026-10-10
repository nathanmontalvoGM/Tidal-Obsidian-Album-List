---
title: "A Mind Waiting To Die"
artist: "Graphic Nature"
year: 2023
tidal_id: 252238521
tags:
  - Metalcore
  - Alternativemetal
  - Numetal
rating:
---

# A Mind Waiting To Die
**Artist:** Graphic Nature
**Year:** 2023

![[_covers/Graphic Nature - A Mind Waiting To Die.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/252238521
```
^button-5po6
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Graphic%20Nature%20A%20Mind%20Waiting%20To%20Die
```
^button-spp4

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
| 1 | 404 | 0:43 |  |
| 2 | Sour | 2:32 |  |
| 3 | Into the Dark | 2:48 |  |
| 4 | Killing Floor | 2:54 |  |
| 5 | Sleepless | 2:22 |  |
| 6 | White Noise | 3:20 |  |
| 7 | 90 | 0:56 |  |
| 8 | Bad Blood | 2:53 |  |
| 9 | Twisted Fear | 3:04 |  |
| 10 | Headstone | 3:37 |  |
| 11 | Death Wish | 2:32 |  |
| 12 | A Twin | 2:33 |  |
| 13 | The Downpour | 4:17 |  |
