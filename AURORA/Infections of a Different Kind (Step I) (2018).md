---
title: "Infections of a Different Kind (Step I)"
artist: "AURORA"
year: 2018
tidal_id: 243783626
tags:
  - Indie
  - Pop
  - Electropop
  - ArtPop
rating:
---

# Infections of a Different Kind (Step I)
**Artist:** AURORA
**Year:** 2018

![[_covers/AURORA - Infections of a Different Kind (Step I).jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/243783626
```
^button-k1x6
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=AURORA%20Infections%20of%20a%20Different%20Kind%20%28Step%20I%29
```
^button-u6b5

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
| 1 | Queendom | 3:26 |  |
| 2 | Forgotten Love | 3:28 |  |
| 3 | Gentle Earthquakes | 3:47 |  |
| 4 | All Is Soft Inside | 5:08 |  |
| 5 | It Happened Quiet | 4:09 |  |
| 6 | Churchyard | 3:46 |  |
| 7 | Soft Universe | 3:59 |  |
| 8 | Infections of a Different Kind | 5:26 |  |
