---
title: "Bioluminescence"
artist: "Dawn of Ouroboros"
year: 2025
tidal_id: 389002094
tags:
  - Blackmetal
  - Melodicdeathmetal
  - Progressivemetal
rating:
---

# Bioluminescence
**Artist:** Dawn of Ouroboros
**Year:** 2025

![[_covers/Dawn of Ouroboros - Bioluminescence.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/389002094
```
^button-g3z2
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Dawn%20of%20Ouroboros%20Bioluminescence
```
^button-v7um

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
| 1 | Bioluminescence | 5:07 |  |
| 2 | Nebulae | 4:47 |  |
| 3 | Slipping Burgundy | 7:38 |  |
| 4 | Poseidon's Hymn | 4:33 |  |
| 5 | Dueling Sunsets | 5:43 |  |
| 6 | Static Repetition | 5:29 |  |
| 7 | Fragile Tranquility | 6:43 |  |
| 8 | Mournful Ambience | 3:11 |  |
