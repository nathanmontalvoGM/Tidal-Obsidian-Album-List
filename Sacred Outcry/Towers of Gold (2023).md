---
title: "Towers of Gold"
artist: "Sacred Outcry"
year: 2023
tidal_id: 294380741
tags:
  - Powermetal
  - Heavymetal
  - Conceptalbum
  - Bestof2022
rating:
---

# Towers of Gold
**Artist:** Sacred Outcry
**Year:** 2023

![[_covers/Sacred Outcry - Towers of Gold.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/294380741
```
^button-xmlv
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Sacred%20Outcry%20Towers%20of%20Gold
```
^button-gt3e

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
| 1 | Through Lands Forgotten | 2:14 |  |
| 2 | The Flame Rekindled | 5:06 |  |
| 3 | The Voyage | 5:11 |  |
| 4 | Ιnto the Storm | 4:41 |  |
| 5 | Symphony of the Night | 5:33 |  |
| 6 | A Midnight Reverie | 1:41 |  |
| 7 | The Sweet Wine of Betrayal | 7:52 |  |
| 8 | The City of Stone | 5:22 |  |
| 9 | Towers of Gold | 14:52 |  |
| 10 | Where Crimson Shadows Dwell | 2:55 |  |
