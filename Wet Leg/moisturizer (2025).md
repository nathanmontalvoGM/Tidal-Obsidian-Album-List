---
title: "moisturizer"
artist: "Wet Leg"
year: 2025
tidal_id: 438505853
tags:
  - Indierock
  - Indiepop
  - Garagerockrevival
  - Rock
rating:
---

# moisturizer
**Artist:** Wet Leg
**Year:** 2025

![[_covers/Wet Leg - moisturizer.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/438505853
```
^button-pjc4
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Wet%20Leg%20moisturizer
```
^button-hbvq

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
| 1 | CPR | 2:51 |  |
| 2 | liquidize | 2:27 |  |
| 3 | catch these fists | 3:08 |  |
| 4 | davina mccall | 3:47 |  |
| 5 | jennifer’s body | 2:26 |  |
| 6 | mangetout | 3:24 |  |
| 7 | pond song | 2:58 |  |
| 8 | pokemon | 3:26 |  |
| 9 | pillow talk | 2:56 |  |
| 10 | don’t speak | 3:13 |  |
| 11 | 11:21 | 3:46 |  |
| 12 | u and me at home | 4:03 |  |
