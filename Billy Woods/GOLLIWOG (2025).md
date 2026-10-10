---
title: "GOLLIWOG"
artist: "Billy Woods"
year: 2025
tidal_id: 414584891
tags:
  - AbstractHipHop
  - ExperimentalHipHop
  - Horrorcore
  - Jazzrap
rating:
---

# GOLLIWOG
**Artist:** Billy Woods
**Year:** 2025

![[_covers/Billy Woods - GOLLIWOG.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/414584891
```
^button-7kbr
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Billy%20Woods%20GOLLIWOG
```
^button-yzea

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
| 1 | Jumpscare | 3:16 |  |
| 2 | STAR87 | 2:37 |  |
| 3 | Misery | 2:12 |  |
| 4 | BLK XMAS | 3:10 |  |
| 5 | Waterproof Mascara | 2:53 |  |
| 6 | Counterclockwise | 2:10 |  |
| 7 | Corinthians | 3:22 |  |
| 8 | Pitchforks & Halos | 2:21 |  |
| 9 | All These Worlds Are Yours | 2:43 |  |
| 10 | Maquiladoras | 3:07 |  |
| 11 | A Doll Fulla Pins | 3:30 |  |
| 12 | Golgotha | 3:01 |  |
| 13 | Cold Sweat | 2:23 |  |
| 14 | BLK ZMBY | 2:13 |  |
| 15 | Make No Mistake | 2:31 |  |
| 16 | Born Alone | 2:56 |  |
| 17 | Lead Paint Test | 4:25 |  |
| 18 | Dislocated | 5:42 |  |
| 19 | Zaire (Andrew Broder mix) | 3:40 |  |
