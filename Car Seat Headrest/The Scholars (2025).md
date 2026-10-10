---
title: "The Scholars"
artist: "Car Seat Headrest"
year: 2025
tidal_id: 429237324
tags:
  - RockOpera
  - Furry
  - Progressivepop
  - Indierock
rating:
---

# The Scholars
**Artist:** Car Seat Headrest
**Year:** 2025

![[_covers/Car Seat Headrest - The Scholars.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/429237324
```
^button-t8h8
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Car%20Seat%20Headrest%20The%20Scholars
```
^button-q0n2

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
| 1 | CCF (I’m Gonna Stay with You) | 8:12 |  |
| 2 | Devereaux | 4:31 |  |
| 3 | Lady Gay Approximately | 3:48 |  |
| 4 | The Catastrophe (Good Luck with That, Man) | 5:28 |  |
| 5 | Equals | 4:12 |  |
| 6 | Gethsemane | 10:52 |  |
| 7 | Reality | 11:14 |  |
| 8 | Planet Desperation | 18:52 |  |
| 9 | True/False Lover | 3:29 |  |
