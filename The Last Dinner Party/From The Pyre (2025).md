---
title: "From The Pyre"
artist: "The Last Dinner Party"
year: 2025
tidal_id: 466009252
tags:
  - Poprock
  - Glamrock
  - Indierock
  - Progressivepop
rating:
---

# From The Pyre
**Artist:** The Last Dinner Party
**Year:** 2025

![[_covers/The Last Dinner Party - From The Pyre.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/466009252
```
^button-uo1u
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=The%20Last%20Dinner%20Party%20From%20The%20Pyre
```
^button-ecap

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
| 1 | Agnus Dei | 5:33 |  |
| 2 | Count the Ways | 3:59 |  |
| 3 | Second Best | 3:31 |  |
| 4 | This is the Killer Speaking | 4:54 |  |
| 5 | Rifle | 4:32 |  |
| 6 | Woman is a Tree | 3:58 |  |
| 7 | I Hold Your Anger | 4:21 |  |
| 8 | Sail Away | 3:59 |  |
| 9 | The Scythe | 4:45 |  |
| 10 | Inferno | 3:29 |  |
