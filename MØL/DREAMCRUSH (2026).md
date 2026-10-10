---
title: "DREAMCRUSH"
artist: "MØL"
year: 2026
tidal_id: 490065965
tags:
  - Shoegaze
  - Bestof2022
  - Blackgaze
rating:
---

# DREAMCRUSH
**Artist:** MØL
**Year:** 2026

![[_covers/MØL - DREAMCRUSH.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/490065965
```
^button-o8ti
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=M%C3%98L%20DREAMCRUSH
```
^button-vx0y

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
| 1 | DREAM | 3:13 |  |
| 2 | Små forlis | 3:45 |  |
| 3 | Young | 4:18 |  |
| 4 | Hud | 4:46 |  |
| 5 | Garland | 3:47 |  |
| 6 | Favour | 4:33 |  |
| 7 | A Former Blueprint | 3:21 |  |
| 8 | ∞ | 0:48 |  |
| 9 | Dissonance | 4:03 |  |
| 10 | Mimic | 4:03 |  |
| 11 | CRUSH | 5:47 |  |
