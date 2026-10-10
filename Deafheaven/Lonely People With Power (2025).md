---
title: "Lonely People With Power"
artist: "Deafheaven"
year: 2025
tidal_id: 415466666
tags:
  - Blackgaze
  - Blackmetal
  - Postmetal
  - Bestof2022
rating:
---

# Lonely People With Power
**Artist:** Deafheaven
**Year:** 2025

![[_covers/Deafheaven - Lonely People With Power.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/415466666
```
^button-c2f0
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Deafheaven%20Lonely%20People%20With%20Power
```
^button-8t96

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
| 1-1 | Incidental I | 0:56 |  |
| 1-2 | Doberman | 6:34 |  |
| 1-3 | Magnolia | 4:14 |  |
| 1-4 | The Garden Route | 5:48 |  |
| 1-5 | Heathen | 5:02 |  |
| 1-6 | Amethyst | 8:14 |  |
| 2-1 | Incidental II | 4:20 |  |
| 2-2 | Revelator | 6:24 |  |
| 2-3 | Body Behavior | 5:23 |  |
| 2-4 | Incidental III | 2:08 |  |
| 2-5 | Winona | 7:28 |  |
| 2-6 | The Marvelous Orange Tree | 5:37 |  |
