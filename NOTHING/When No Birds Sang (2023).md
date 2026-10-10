---
title: "When No Birds Sang"
artist: "NOTHING"
year: 2023
tidal_id: 316979894
tags:
  - Sludge
  - Metalcore
  - Grindcore
  - Shoegaze
rating:
---

# When No Birds Sang
**Artist:** NOTHING
**Year:** 2023

![[_covers/NOTHING - When No Birds Sang.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/316979894
```
^button-7lds
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=NOTHING%20When%20No%20Birds%20Sang
```
^button-3dzj

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
| 1 | Rose Tinted World | 8:11 |  |
| 2 | Like Stars in the Firmament | 5:24 |  |
| 3 | Forever Well | 4:07 |  |
| 4 | Wild Blue | 4:32 |  |
| 5 | When No Birds Sang | 5:48 |  |
| 6 | Spend the Grace | 5:47 |  |
