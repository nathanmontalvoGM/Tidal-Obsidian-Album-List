---
title: "Wishbone"
artist: "Conan Gray"
year: 2025
tidal_id: 452880357
tags:
  - Singersongwriter
  - Indiepop
  - Poprock
  - Chamberpop
rating:
---

# Wishbone
**Artist:** Conan Gray
**Year:** 2025

![[_covers/Conan Gray - Wishbone.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/452880357
```
^button-6747
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Conan%20Gray%20Wishbone
```
^button-m7xb

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
| 1 | Actor | 3:44 |  |
| 2 | This Song | 3:34 |  |
| 3 | Vodka Cranberry | 4:05 |  |
| 4 | Romeo | 3:32 |  |
| 5 | My World | 3:44 |  |
| 6 | Class Clown | 3:17 |  |
| 7 | Nauseous | 3:43 |  |
| 8 | Caramel | 3:54 |  |
| 9 | Connell | 3:32 |  |
| 10 | Sunset Tower | 3:18 |  |
| 11 | Eleven Eleven | 3:29 |  |
| 12 | Care | 3:28 |  |
