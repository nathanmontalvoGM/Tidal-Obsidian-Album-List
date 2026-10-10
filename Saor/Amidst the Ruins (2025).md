---
title: "Amidst the Ruins"
artist: "Saor"
year: 2025
tidal_id: 393763788
tags:
  - Atmosphericmetal
  - PaganBlackMetal
rating:
---

# Amidst the Ruins
**Artist:** Saor
**Year:** 2025

![[_covers/Saor - Amidst the Ruins.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/393763788
```
^button-qe07
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Saor%20Amidst%20the%20Ruins
```
^button-shww

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
| 1 | Amidst the Ruins | 12:40 |  |
| 2 | Echoes of the Ancient Land | 11:41 |  |
| 3 | Glen of Sorrow | 12:04 |  |
| 4 | The Sylvan Embrace | 8:18 |  |
| 5 | Rebirth | 14:09 |  |
