---
title: "A Funeral In Purgatory"
artist: "Blind Equation"
year: 2025
tidal_id: 421066136
tags:
  - Blackmetal
  - Metalcore
  - Cybergrind
  - Electronicore
rating:
---

# A Funeral In Purgatory
**Artist:** Blind Equation
**Year:** 2025

![[_covers/Blind Equation - A Funeral In Purgatory.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/421066136
```
^button-zgv2
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Blind%20Equation%20A%20Funeral%20In%20Purgatory
```
^button-w1in

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
| 1 | This Eternal Curse | 2:46 |  |
| 2 | Nothing | 2:41 |  |
| 3 | it feels like the end | 2:23 |  |
| 4 | A Funeral… | 4:14 |  |
| 5 | +‧+ ̊ ཐི⋆✟⋆ཋྀ ̊+‧+ | 0:58 |  |
| 6 | …in purgatory | 1:30 |  |
| 7 | Flashback | 2:26 |  |
| 8 | mourn | 3:16 |  |
| 9 | Relinquished Dreams | 3:03 |  |
| 10 | still | 2:51 |  |
| 11 | Incomplete | 6:07 |  |
