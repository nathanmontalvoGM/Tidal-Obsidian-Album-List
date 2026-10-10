---
title: "Bright Future"
artist: "Adrianne Lenker"
year: 2024
tidal_id: 348182611
tags:
  - Singer-Songwriter
  - ContemporaryFolk
  - Americana
  - Folk
rating:
---

# Bright Future
**Artist:** Adrianne Lenker
**Year:** 2024

![[_covers/Adrianne Lenker - Bright Future.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/348182611
```
^button-98v3
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Adrianne%20Lenker%20Bright%20Future
```
^button-ui5e

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
| 1 | real house | 5:58 |  |
| 2 | sadness as a gift | 4:19 |  |
| 3 | fool | 2:54 |  |
| 4 | no machine | 3:00 |  |
| 5 | free treasure | 3:35 |  |
| 6 | vampire empire | 3:55 |  |
| 7 | evol | 4:14 |  |
| 8 | candleflame | 2:34 |  |
| 9 | already lost | 3:27 |  |
| 10 | cell phone says | 2:38 |  |
| 11 | donut seam | 2:25 |  |
| 12 | ruined | 4:32 |  |
