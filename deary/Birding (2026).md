---
title: "Birding"
artist: "deary"
year: 2026
tidal_id: 480062390
tags:
  - Dreampop
  - Rock
  - Shoegaze
rating:
---

# Birding
**Artist:** deary
**Year:** 2026

![[_covers/deary - Birding.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/480062390
```
^button-unfx
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=deary%20Birding
```
^button-6fyi

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
| 1 | Smile | 5:09 |  |
| 2 | Seabird | 4:38 |  |
| 3 | Baby's Breath | 3:55 |  |
| 4 | Gypsophila | 2:17 |  |
| 5 | Blue Ribbon | 3:46 |  |
| 6 | Garden of Eden | 2:34 |  |
| 7 | Alma | 3:40 |  |
| 8 | No Sweeter Feeling | 3:08 |  |
| 9 | Terra Fable | 4:15 |  |
| 10 | Alfie | 7:30 |  |
| 11 | Birding | 2:19 |  |
