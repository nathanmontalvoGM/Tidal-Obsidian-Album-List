---
title: "Weatherglow"
artist: "Asian Glow"
year: 2022
tidal_id: 221725190
tags:
  - Emo
  - Indietronica
  - Shoegaze
  - Lofi
rating:
---

# Weatherglow
**Artist:** Asian Glow
**Year:** 2022

![[_covers/Asian Glow - Weatherglow.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/221725190
```
^button-onkb
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Asian%20Glow%20Weatherglow
```
^button-othu

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
| 1 | Melt a Bed | 3:44 |  |
| 2 | Clockwalk Around the Ache | 4:01 |  |
| 3 | Center | 4:42 |  |
| 4 | Late Time Stroll | 4:19 |  |
| 5 | Look Alive, Sunshine | 3:08 |  |
| 6 | Jet | 3:47 |  |
