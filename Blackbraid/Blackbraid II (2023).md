---
title: "Blackbraid II"
artist: "Blackbraid"
year: 2023
tidal_id: 290666834
tags:
  - Blackmetal
  - Melodicblackmetal
  - Atmosphericmetal
  - 2020s
rating:
---

# Blackbraid II
**Artist:** Blackbraid
**Year:** 2023

![[_covers/Blackbraid - Blackbraid II.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/290666834
```
^button-f9uf
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Blackbraid%20Blackbraid%20II
```
^button-p66y

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
| 1 | Autumnal Hearts Ablaze | 2:10 |  |
| 2 | The Spirit Returns | 4:37 |  |
| 3 | The Wolf That Guides the Hunters Hand | 7:34 |  |
| 4 | Spells of Moon and Earth | 2:24 |  |
| 5 | Moss Covered Bones on the Altar of the Moon | 13:30 |  |
| 6 | A Song of Death on Winds of Dawn | 11:04 |  |
| 7 | Celestial Passage | 2:24 |  |
| 8 | Twilight Hymn of Ancient Blood | 6:59 |  |
| 9 | Sadness and the Passage of Time and Memory | 7:02 |  |
| 10 | A Fine Day to Die | 8:15 |  |
