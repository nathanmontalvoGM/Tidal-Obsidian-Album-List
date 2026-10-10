---
title: "Harbour Century"
artist: "Eunuchs"
year: 2024
tidal_id: 350119011
tags:
  - ArtRock
  - SymphonicProg
  - Jazzrock
  - AvantProg
rating:
---

# Harbour Century
**Artist:** Eunuchs
**Year:** 2024

![[_covers/Eunuchs - Harbour Century.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/350119011
```
^button-7dsv
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Eunuchs%20Harbour%20Century
```
^button-lubo

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
| 1 | Magic Death Sea Nemesis | 6:07 |  |
| 2 | Pat a Dragon | 4:20 |  |
| 3 | Estuary of Dreams | 4:29 |  |
| 4 | Siren | 4:48 |  |
| 5 | Magnificent Stallion | 3:38 |  |
| 6 | Gnome and Fortune | 6:04 |  |
| 7 | Bird Angel Dynasty | 5:22 |  |
| 8 | Hierophant | 3:28 |  |
| 9 | Heroin King | 17:35 |  |
