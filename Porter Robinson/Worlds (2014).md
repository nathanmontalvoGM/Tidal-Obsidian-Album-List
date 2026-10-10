---
title: "Worlds"
artist: "Porter Robinson"
year: 2014
tidal_id: 32571279
tags:
  - Vocaloid
  - Electronicore
  - Chillout
  - Edm
rating:
---

# Worlds
**Artist:** Porter Robinson
**Year:** 2014

![[_covers/Porter Robinson - Worlds.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/32571279
```
^button-srqk
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Porter%20Robinson%20Worlds
```
^button-vwcm

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
| 1 | Divinity | 6:08 |  |
| 2 | Sad Machine | 5:50 |  |
| 3 | Years of War | 3:56 |  |
| 4 | Flicker | 4:39 |  |
| 5 | Fresh Static Snow | 5:58 |  |
| 6 | Polygon Dust | 3:29 |  |
| 7 | Hear the Bells | 4:46 |  |
| 8 | Natural Light | 2:21 |  |
| 9 | Lionhearted | 4:26 |  |
| 10 | Sea of Voices | 4:58 |  |
| 11 | Fellow Feeling | 5:50 |  |
| 12 | Goodbye To a World | 5:28 |  |
