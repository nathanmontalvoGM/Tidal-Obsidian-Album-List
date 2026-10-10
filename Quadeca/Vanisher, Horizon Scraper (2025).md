---
title: "Vanisher, Horizon Scraper"
artist: "Quadeca"
year: 2025
tidal_id: 450198559
tags:
  - Vinyl
  - ArtPop
  - Folktronica
  - Neopsychedelia
rating:
---

# Vanisher, Horizon Scraper
**Artist:** Quadeca
**Year:** 2025

![[_covers/Quadeca - Vanisher, Horizon Scraper.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/450198559
```
^button-3j8s
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Quadeca%20Vanisher%2C%20Horizon%20Scraper
```
^button-c208

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
| 1 | NO QUESTIONS ASKED | 5:59 |  |
| 2 | WAGING WAR | 5:15 |  |
| 3 | RUIN MY LIFE | 4:41 |  |
| 4 | GODSTAINED | 3:25 |  |
| 5 | AT A TIME LIKE THIS | 4:36 |  |
| 6 | MONDAY | 4:03 |  |
| 7 | DANCING WITHOUT MOVING | 3:19 |  |
| 8 | THAT’S WHY | 4:29 |  |
| 9 | I DREAM ABOUT SINKING | 3:54 |  |
| 10 | NATURAL CAUSES | 3:49 |  |
| 11 | THUNDRRR | 4:40 |  |
| 12 | THE GREAT BAKUNAWA | 5:40 |  |
| 13 | FORGONE | 7:54 |  |
| 14 | CASPER | 7:34 |  |
