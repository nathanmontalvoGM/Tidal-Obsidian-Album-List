---
title: "Phantom Island"
artist: "King Gizzard & The Lizard Wizard"
year: 2025
tidal_id: 440456313
tags:
  - BluesRock
  - SymphonicProg
  - Psychedelicrock
  - Poprock
rating:
---

# Phantom Island
**Artist:** King Gizzard & The Lizard Wizard
**Year:** 2025

![[_covers/King Gizzard & The Lizard Wizard - Phantom Island.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/440456313
```
^button-zhns
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=King%20Gizzard%20%26%20The%20Lizard%20Wizard%20Phantom%20Island
```
^button-uibs

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
| 1 | Phantom Island | 5:14 |  |
| 2 | Deadstick | 3:33 |  |
| 3 | Lonely Cosmos | 5:35 |  |
| 4 | Eternal Return | 4:34 |  |
| 5 | Panpsych | 4:02 |  |
| 6 | Spacesick | 4:50 |  |
| 7 | Aerodynamic | 4:46 |  |
| 8 | Sea of Doubt | 4:24 |  |
| 9 | Silent Spirit | 4:28 |  |
| 10 | Grow Wings and Fly | 5:08 |  |
