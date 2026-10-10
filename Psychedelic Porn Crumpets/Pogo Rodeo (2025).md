---
title: "Pogo Rodeo"
artist: "Psychedelic Porn Crumpets"
year: 2025
tidal_id: 464145390
tags:
  - Rock
  - Stonerrock
  - Psychedelicrock
  - GaragePunk
rating:
---

# Pogo Rodeo
**Artist:** Psychedelic Porn Crumpets
**Year:** 2025

![[_covers/Psychedelic Porn Crumpets - Pogo Rodeo.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/464145390
```
^button-y3bf
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Psychedelic%20Porn%20Crumpets%20Pogo%20Rodeo
```
^button-at7s

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
| 1 | Salsa Verde | 3:24 |  |
| 2 | Born in the A.D's | 4:33 |  |
| 3 | Manny's Ready to Roll | 3:41 |  |
| 4 | The Real Contra Band | 3:09 |  |
| 5 | Japan | 4:22 |  |
| 6 | Unconventional Daze | 3:26 |  |
| 7 | Texas Rangers | 3:41 |  |
| 8 | Looniversal | 3:01 |  |
| 9 | Watermelon | 4:09 |  |
| 10 | Bowling With Tim | 3:53 |  |
| 11 | Heading to Fringe | 4:47 |  |
