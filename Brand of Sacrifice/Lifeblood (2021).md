---
title: "Lifeblood"
artist: "Brand of Sacrifice"
year: 2021
tidal_id: 161511706
tags:
  - Deathcore
  - Numetal
  - Technicaldeathcore
  - Brutaldeathcore
rating:
---

# Lifeblood
**Artist:** Brand of Sacrifice
**Year:** 2021

![[_covers/Brand of Sacrifice - Lifeblood.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/161511706
```
^button-itaw
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Brand%20of%20Sacrifice%20Lifeblood
```
^button-4cnt

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
| 1 | Dawn | 1:53 |  |
| 2 | Demon King | 3:55 |  |
| 3 | Animal | 4:05 |  |
| 4 | Altered Eyes | 3:54 |  |
| 5 | Prophecy of the Falcon | 2:57 |  |
| 6 | Perfect World | 1:28 |  |
| 7 | Mortal Vessel | 4:17 |  |
| 8 | Foe of the Inhuman | 4:05 |  |
| 9 | Vengeance | 4:28 |  |
| 10 | Ruin | 3:43 |  |
| 11 | Corridor of Dreams | 2:07 |  |
| 12 | Lifeblood | 4:17 |  |
