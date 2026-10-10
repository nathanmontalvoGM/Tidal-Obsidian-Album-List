---
title: "Wake Up The Wicked"
artist: "Powerwolf"
year: 2024
tidal_id: 376214735
tags:
  - Powermetal
  - Heavymetal
  - Lautrezension
  - Numetal
rating:
---

# Wake Up The Wicked
**Artist:** Powerwolf
**Year:** 2024

![[_covers/Powerwolf - Wake Up The Wicked.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/376214735
```
^button-cxgw
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Powerwolf%20Wake%20Up%20The%20Wicked
```
^button-j08i

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
| 1 | Bless ’em With the Blade | 2:48 |  |
| 2 | Sinners of the Seven Seas | 3:01 |  |
| 3 | Kyrie Klitorem | 3:04 |  |
| 4 | Heretic Hunters | 3:27 |  |
| 5 | 1589 | 4:05 |  |
| 6 | Viva Vulgata | 3:08 |  |
| 7 | Wake Up the Wicked | 3:39 |  |
| 8 | Joan of Arc | 3:21 |  |
| 9 | Thunderpriest | 3:22 |  |
| 10 | We Don’t Wanna Be No Saints | 3:16 |  |
| 11 | Vargamor | 3:57 |  |
