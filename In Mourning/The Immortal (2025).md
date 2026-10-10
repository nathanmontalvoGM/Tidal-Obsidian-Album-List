---
title: "The Immortal"
artist: "In Mourning"
year: 2025
tidal_id: 431695685
tags:
  - Melodicdeathmetal
  - Progressivemetal
  - Numetal
  - Progressivepop
rating:
---

# The Immortal
**Artist:** In Mourning
**Year:** 2025

![[_covers/In Mourning - The Immortal.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/431695685
```
^button-ae9v
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=In%20Mourning%20The%20Immortal
```
^button-9jo2

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
| 1 | The Immortal | 1:07 |  |
| 2 | Silver Crescent | 5:28 |  |
| 3 | Song of the Cranes | 6:07 |  |
| 4 | As Long as the Twilight Stays | 7:16 |  |
| 5 | The Sojourner | 5:05 |  |
| 6 | Moonless Sky | 3:01 |  |
| 7 | Staghorn | 5:43 |  |
| 8 | North Star | 5:15 |  |
| 9 | The Hounding | 8:10 |  |
