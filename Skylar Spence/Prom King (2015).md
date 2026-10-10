---
title: "Prom King"
artist: "Skylar Spence"
year: 2015
tidal_id: 195419786
tags:
  - Poptron
  - Disco
  - FutureFunk
  - Vaporwave
rating:
---

# Prom King
**Artist:** Skylar Spence
**Year:** 2015

![[_covers/Skylar Spence - Prom King.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/195419786
```
^button-6rb2
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Skylar%20Spence%20Prom%20King
```
^button-o8ja

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
| 1 | Intro | 2:11 |  |
| 2 | Can't You See | 4:06 |  |
| 3 | Prom King | 4:14 |  |
| 4 | I Can't Be Your Superman | 4:20 |  |
| 5 | Ridiculous! | 3:34 |  |
| 6 | Fall Harder | 4:46 |  |
| 7 | Bounce Is Back | 3:30 |  |
| 8 | Affairs | 4:21 |  |
| 9 | All I Want | 3:00 |  |
| 10 | Cash Wednesday | 2:32 |  |
| 11 | Fiona Coyne | 4:09 |  |
