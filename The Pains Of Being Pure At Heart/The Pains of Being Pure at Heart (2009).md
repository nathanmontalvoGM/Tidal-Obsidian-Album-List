---
title: "The Pains of Being Pure at Heart"
artist: "The Pains Of Being Pure At Heart"
year: 2009
tidal_id: 111403686
tags:
  - Indierock
  - Pop
  - Rock
rating:
---

# The Pains of Being Pure at Heart
**Artist:** The Pains Of Being Pure At Heart
**Year:** 2009

![[_covers/The Pains Of Being Pure At Heart - The Pains of Being Pure at Heart.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/111403686
```
^button-3t6u
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=The%20Pains%20Of%20Being%20Pure%20At%20Heart%20The%20Pains%20of%20Being%20Pure%20at%20Heart
```
^button-ajau

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
| 1 | Contender | 2:41 |  |
| 2 | Come Saturday | 3:17 |  |
| 3 | Young Adult Friction | 4:08 |  |
| 4 | This Love Is Fucking Right! | 3:16 |  |
| 5 | The Tenure Itch | 3:46 |  |
| 6 | Stay Alive | 4:56 |  |
| 7 | Everything With You | 3:00 |  |
| 8 | A Teenager in Love | 3:24 |  |
| 9 | Hey Paul | 2:04 |  |
| 10 | Gentle Sons | 4:34 |  |
| 11 | The Pains of Being Pure at Heart | 2:56 |  |
| 12 | Ramona | 3:50 |  |
| 13 | Side Ponytail | 2:03 |  |
| 14 | Higher Than the Stars | 3:49 |  |
| 15 | 103 | 2:03 |  |
| 16 | Falling Over | 3:11 |  |
| 17 | Twins | 3:21 |  |
| 18 | Say No to Love | 3:55 |  |
| 19 | Lost Saint | 3:55 |  |
