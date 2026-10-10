---
title: "The Spiritual Sound"
artist: "Agriculture"
year: 2025
tidal_id: 443831341
tags:
  - Blackmetal
  - Postmetal
  - Depressiveblackmetal
  - Blackgaze
rating:
---

# The Spiritual Sound
**Artist:** Agriculture
**Year:** 2025

![[_covers/Agriculture - The Spiritual Sound.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/443831341
```
^button-bm86
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Agriculture%20The%20Spiritual%20Sound
```
^button-cfhu

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
| 1 | My Garden | 5:12 |  |
| 2 | Flea | 3:55 |  |
| 3 | Micah (5:15am) | 4:21 |  |
| 4 | The Weight | 5:43 |  |
| 5 | Serenity | 3:07 |  |
| 6 | The Spiritual Sound | 0:28 |  |
| 7 | Dan’s Love Song | 4:51 |  |
| 8 | Bodhidharma | 6:23 |  |
| 9 | Hallelujah | 3:30 |  |
| 10 | The Reply | 6:29 |  |
