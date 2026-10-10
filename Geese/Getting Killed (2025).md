---
title: "Getting Killed"
artist: "Geese"
year: 2025
tidal_id: 440082667
tags:
  - Indierock
  - ArtRock
  - Psychedelicrock
  - Krautrock
rating:
---

# Getting Killed
**Artist:** Geese
**Year:** 2025

![[_covers/Geese - Getting Killed.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/440082667
```
^button-ao4e
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Geese%20Getting%20Killed
```
^button-e7gq

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
| 1 | Trinidad | 3:44 |  |
| 2 | Cobra | 3:05 |  |
| 3 | Husbands | 4:08 |  |
| 4 | Getting Killed | 4:44 |  |
| 5 | Islands of Men | 5:54 |  |
| 6 | 100 Horses | 3:46 |  |
| 7 | Half Real | 3:22 |  |
| 8 | Au pays du cocaine | 3:30 |  |
| 9 | Bow Down | 3:28 |  |
| 10 | Taxes | 3:17 |  |
| 11 | Long Island City Here I Come | 6:37 |  |
