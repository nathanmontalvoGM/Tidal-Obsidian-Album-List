---
title: "Albion"
artist: "Harp"
year: 2023
tidal_id: 331225974
tags:
  - Singersongwriter
  - Darkfolk
  - Folkrock
  - Indiefolk
rating:
---

# Albion
**Artist:** Harp
**Year:** 2023

![[_covers/Harp - Albion.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/331225974
```
^button-4rii
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Harp%20Albion
```
^button-wjp2

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
| 1 | The Pleasant Grey | 1:49 |  |
| 2 | I Am the Seed | 3:37 |  |
| 3 | A Fountain | 4:09 |  |
| 4 | Daughters of Albion | 3:01 |  |
| 5 | Chrystals | 1:37 |  |
| 6 | Country Cathedral Drive | 5:06 |  |
| 7 | Shining Spires | 3:56 |  |
| 8 | Silver Wings | 3:45 |  |
| 9 | Seven Long Suns | 3:55 |  |
| 10 | Moon | 1:14 |  |
| 11 | Throne of Amber | 4:10 |  |
| 12 | Herstmonceux | 4:04 |  |
