---
title: "Eye of Water"
artist: "TIDELESS"
year: 2023
tidal_id: 303637097
tags: []
rating:
---

# Eye of Water
**Artist:** TIDELESS
**Year:** 2023

![[_covers/TIDELESS - Eye of Water.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/303637097
```
^button-z60x
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=TIDELESS%20Eye%20of%20Water
```
^button-768l

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
| 1 | Drowning (19° 40′ 49″ N, 99° 0′ 36″ W) | 6:40 |  |
| 2 | Fields at Dawn | 14:54 |  |
| 3 | Oblations for the Sun | 18:52 |  |
| 4 | Laurel of Victory | 10:35 |  |
| 5 | Lush.Serene.Dissolved | 24:17 |  |
| 6 | Sea of Tears | 8:01 |  |
