---
title: "HIT ME HARD AND SOFT"
artist: "Billie Eilish"
year: 2024
tidal_id: 363236461
tags:
  - Aoty
  - Pop
  - ArtPop
  - Poprock
rating:
---

# HIT ME HARD AND SOFT
**Artist:** Billie Eilish
**Year:** 2024

![[_covers/Billie Eilish - HIT ME HARD AND SOFT.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/363236461
```
^button-51vv
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Billie%20Eilish%20HIT%20ME%20HARD%20AND%20SOFT
```
^button-glj7

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
| 1 | SKINNY | 3:39 |  |
| 2 | LUNCH | 2:59 |  |
| 3 | CHIHIRO | 5:03 |  |
| 4 | BIRDS OF A FEATHER | 3:30 |  |
| 5 | WILDFLOWER | 4:21 |  |
| 6 | THE GREATEST | 4:53 |  |
| 7 | L’AMOUR DE MA VIE | 5:33 |  |
| 8 | THE DINER | 3:06 |  |
| 9 | BITTERSUITE | 4:58 |  |
| 10 | BLUE | 5:43 |  |
