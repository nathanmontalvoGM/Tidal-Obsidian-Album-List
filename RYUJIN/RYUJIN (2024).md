---
title: "RYUJIN"
artist: "RYUJIN"
year: 2024
tidal_id: 314612550
tags:
  - Melodicdeathmetal
rating:
---

# RYUJIN
**Artist:** RYUJIN
**Year:** 2024

![[_covers/RYUJIN - RYUJIN.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/314612550
```
^button-927x
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=RYUJIN%20RYUJIN
```
^button-0lwb

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
| 1 | Hajimari | 0:40 |  |
| 2 | Gekokujo | 4:47 |  |
| 3 | Dragon, Fly Free | 4:22 |  |
| 4 | Raijin & Fujin | 6:09 |  |
| 5 | The Rainbow Song | 4:01 |  |
| 6 | Kunnecup | 5:35 |  |
| 7 | Scream of the Dragon | 3:56 |  |
| 8 | Gekirin | 4:04 |  |
| 9 | Saigo No Hoshi | 5:20 |  |
| 10 | Ryujin | 7:39 |  |
| 11 | Saigo No Hoshi (single edit) | 5:24 |  |
| 12 | Everytime I Die | 3:59 |  |
