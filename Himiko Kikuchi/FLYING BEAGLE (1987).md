---
title: "FLYING BEAGLE"
artist: "Himiko Kikuchi"
year: 1987
tidal_id: 389704246
tags:
  - Jazz
  - JazzFusion
  - Funk
  - Fusion
rating:
---

# FLYING BEAGLE
**Artist:** Himiko Kikuchi
**Year:** 1987

![[_covers/Himiko Kikuchi - FLYING BEAGLE.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/389704246
```
^button-5xec
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Himiko%20Kikuchi%20FLYING%20BEAGLE
```
^button-kthv

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
| 1 | Look Your Back! | 4:58 |  |
| 2 | A Seagull & Clouds | 4:55 |  |
| 3 | Flying Beagle | 6:30 |  |
| 4 | Fluffy | 4:57 |  |
| 5 | Sand Storm | 5:39 |  |
| 6 | Baby Talk | 5:36 |  |
| 7 | The Second Summer | 6:12 |  |
| 8 | Ducky Ducky | 5:04 |  |
