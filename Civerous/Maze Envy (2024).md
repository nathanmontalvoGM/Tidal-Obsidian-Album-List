---
title: "Maze Envy"
artist: "Civerous"
year: 2024
tidal_id: 342231800
tags:
  - Doommetal
  - Mathmetal
  - Deathdoommetal
rating:
---

# Maze Envy
**Artist:** Civerous
**Year:** 2024

![[_covers/Civerous - Maze Envy.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/342231800
```
^button-y3lv
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Civerous%20Maze%20Envy
```
^button-u30z

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
| 1 | The Azure Eye | 2:01 |  |
| 2 | Shrouded in Crystals | 8:25 |  |
| 3 | Endless Symmetry | 2:27 |  |
| 4 | Labyrinth Charm | 4:40 |  |
| 5 | Levitation Tomb | 5:17 |  |
| 6 | Maze Envy | 9:23 |  |
| 7 | Geryon (The Plummet) | 9:54 |  |
