---
title: "The Redshift Blues"
artist: "Dispirited Spirits"
year: 2023
tidal_id: 266331961
tags:
  - Progressivepop
  - Emo
  - Postrock
  - ArtRock
rating:
---

# The Redshift Blues
**Artist:** Dispirited Spirits
**Year:** 2023

![[_covers/Dispirited Spirits - The Redshift Blues.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/266331961
```
^button-5qyj
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Dispirited%20Spirits%20The%20Redshift%20Blues
```
^button-n6rc

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
| 1 | Ships Sailing Space | 5:20 |  |
| 2 | Nine Clouds | 3:54 |  |
| 3 | Former Living Thing | 2:47 |  |
| 4 | Bring Down the Sky | 8:10 |  |
| 5 | Saturnine Saturn Dreams | 7:14 |  |
| 6 | Methanol Fire | 4:49 |  |
| 7 | Redshift Blues | 10:32 |  |
