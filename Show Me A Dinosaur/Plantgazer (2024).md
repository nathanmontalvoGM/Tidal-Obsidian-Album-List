---
title: "Plantgazer"
artist: "Show Me A Dinosaur"
year: 2024
tidal_id: 160326205
tags:
  - Blackgaze
  - Postrock
  - Rock
rating:
---

# Plantgazer
**Artist:** Show Me A Dinosaur
**Year:** 2024

![[_covers/Show Me A Dinosaur - Plantgazer.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/160326205
```
^button-3lpz
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Show%20Me%20A%20Dinosaur%20Plantgazer
```
^button-w5ce

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
| 1 | Sunflower | 5:28 |  |
| 2 | Marsh | 5:34 |  |
| 3 | Red River | 9:37 |  |
| 4 | Selva | 6:46 |  |
| 5 | Unsaid I | 5:48 |  |
| 6 | Hum | 6:07 |  |
| 7 | Unsaid II | 4:58 |  |
