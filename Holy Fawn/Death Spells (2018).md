---
title: "Death Spells"
artist: "Holy Fawn"
year: 2018
tidal_id: 105498173
tags:
  - Postrock
  - Doommetal
  - Doomgaze
  - Noise
rating:
---

# Death Spells
**Artist:** Holy Fawn
**Year:** 2018

![[_covers/Holy Fawn - Death Spells.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/105498173
```
^button-rk70
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Holy%20Fawn%20Death%20Spells
```
^button-ou6g

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
| 1 | Dark Stone | 6:22 |  |
| 2 | Arrows | 6:40 |  |
| 3 | Drag Me Into the Woods | 6:27 |  |
| 4 | Yawning | 5:35 |  |
| 5 | Seer | 7:51 |  |
| 6 | Two Waves | 3:17 |  |
| 7 | Take Me With You | 7:10 |  |
| 8 | Vespertine | 6:27 |  |
| 9 | Same Blood | 2:48 |  |
| 10 | Sleep Tongue | 8:01 |  |
