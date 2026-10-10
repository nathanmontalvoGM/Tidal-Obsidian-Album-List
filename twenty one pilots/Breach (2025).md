---
title: Breach
artist: twenty one pilots
year: 2025
tidal_id: 459844445
tags:
  - Favorite
  - Alternativerock
  - Rock
  - Pop
  - Breakbeat
rating:
---

# Breach
**Artist:** twenty one pilots
**Year:** 2025

![[_covers/twenty one pilots - Breach.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/459844445
```
^button-zkk6
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=twenty%20one%20pilots%20Breach
```
^button-5n89

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
| 1 | City Walls | 5:22 |  |
| 2 | RAWFEAR | 3:22 |  |
| 3 | Drum Show | 3:23 |  |
| 4 | Garbage | 3:16 |  |
| 5 | The Contract | 3:48 |  |
| 6 | Downstairs | 5:26 |  |
| 7 | Robot Voices | 3:57 |  |
| 8 | Center Mass | 3:48 |  |
| 9 | Cottonwood | 3:08 |  |
| 10 | One Way | 2:43 |  |
| 11 | Days Lie Dormant | 3:26 |  |
| 12 | Tally | 3:32 |  |
| 13 | Intentions | 2:15 |  |
