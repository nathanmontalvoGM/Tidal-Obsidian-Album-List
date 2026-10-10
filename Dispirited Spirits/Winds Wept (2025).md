---
title: "Winds Wept"
artist: "Dispirited Spirits"
year: 2025
tidal_id: 454236304
tags:
  - Artrock
  - Emo
  - Jazzrock
  - Mathrock
rating:
---

# Winds Wept
**Artist:** Dispirited Spirits
**Year:** 2025

![[_covers/Dispirited Spirits - Winds Wept.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/454236304
```
^button-zxim
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Dispirited%20Spirits%20Winds%20Wept
```
^button-jjee

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
| 1 | Forecast (Such a Beautiful Day) | 4:43 |  |
| 2 | Counting Raindrops | 2:45 |  |
| 3 | D.N.R. | 3:47 |  |
| 4 | Kishi Kaisei | 9:51 |  |
| 5 | Irithyll (Count Your Lucky Stars) | 3:05 |  |
| 6 | Powerlines / Powerless | 5:29 |  |
| 7 | For Everest (Winds Wept) | 12:11 |  |
