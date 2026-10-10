---
title: "Houdini"
artist: "Melvins"
year: 1993
tidal_id: 4073695
tags:
  - Sludgemetal
  - Alternativerock
  - Grunge
rating:
---

# Houdini
**Artist:** Melvins
**Year:** 1993

![[_covers/Melvins - Houdini.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/4073695
```
^button-actj
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Melvins%20Houdini
```
^button-5c2f

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
| 1 | Hooch | 2:51 |  |
| 2 | Night Goat | 4:41 |  |
| 3 | Lizzy | 4:43 |  |
| 4 | Going Blind | 4:32 |  |
| 5 | Honey Bucket | 3:01 |  |
| 6 | Hag Me | 7:06 |  |
| 7 | Set Me Straight | 2:25 |  |
| 8 | Sky Pup | 3:50 |  |
| 9 | Joan of Arc | 3:36 |  |
| 10 | Teet | 2:52 |  |
| 11 | Copache | 2:07 |  |
| 12 | Pearl Bomb | 2:45 |  |
| 13 | Spread Eagle Beagle | 10:14 |  |
| 14 | Rocket Reducer No. 62 (Rama Lama Fa Fa Fa) | 3:32 |  |
