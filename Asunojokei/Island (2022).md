---
title: "Island"
artist: "Asunojokei"
year: 2022
tidal_id: 246452123
tags:
  - Posthardcore
  - Blackgaze
  - Rock
  - Atmosphericmetal
rating:
---

# Island
**Artist:** Asunojokei
**Year:** 2022

![[_covers/Asunojokei - Island.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/246452123
```
^button-6z0w
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Asunojokei%20Island
```
^button-7ngs

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
| 1 | Heavenward | 4:37 |  |
| 2 | Chimera | 5:43 |  |
| 3 | Gaze | 1:42 |  |
| 4 | Footprints | 6:18 |  |
| 5 | Diva Under the Blue Sky | 4:52 |  |
| 6 | Beautiful Name | 3:30 |  |
| 7 | The Forgotten Ones | 5:00 |  |
| 8 | The Sweet Smile of Vortex | 7:49 |  |
| 9 | Tidal Lullaby | 2:15 |  |
| 10 | From the Bottom of the Biotope | 4:34 |  |
| 11 | Thunder | 5:57 |  |
