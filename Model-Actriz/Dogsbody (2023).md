---
title: "Dogsbody"
artist: "Model/Actriz"
year: 2023
tidal_id: 452396523
tags:
  - Noiserock
  - DancePunk
  - Industrialrock
  - Rock
rating:
---

# Dogsbody
**Artist:** Model/Actriz
**Year:** 2023

![[_covers/Model-Actriz - Dogsbody.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/452396523
```
^button-6o5c
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Model/Actriz%20Dogsbody
```
^button-1zrk

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
| 1 | Donkey Show | 3:10 |  |
| 2 | Mosquito | 3:12 |  |
| 3 | Crossing Guard | 4:44 |  |
| 4 | Slate | 3:23 |  |
| 5 | Divers | 4:00 |  |
| 6 | Amaranth | 3:37 |  |
| 7 | Pure Mode | 3:07 |  |
| 8 | Maria | 3:26 |  |
| 9 | Sleepless | 5:49 |  |
| 10 | Sun In | 3:24 |  |
