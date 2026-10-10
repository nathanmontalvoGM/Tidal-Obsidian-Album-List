---
title: "Eternal"
artist: "An Autumn for Crippled Children"
year: 2016
tidal_id: 257981657
tags:
  - Blackgaze
  - Blackmetal
  - Postmetal
  - Atmosphericmetal
rating:
---

# Eternal
**Artist:** An Autumn for Crippled Children
**Year:** 2016

![[_covers/An Autumn for Crippled Children - Eternal.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/257981657
```
^button-qxn0
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=An%20Autumn%20for%20Crippled%20Children%20Eternal
```
^button-5gsn

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
| 1 | Eternal Youth | 4:28 |  |
| 2 | I Will Never Let You Die | 4:12 |  |
| 3 | On Fire | 4:20 |  |
| 4 | Farewell | 3:59 |  |
| 5 | This Small Space You Occupied Is So Empty Now | 4:52 |  |
| 6 | You Have Been in the Shadows for So Long | 5:03 |  |
| 7 | Days of Sleep | 4:54 |  |
| 8 | Swallowed by Night's Despair | 3:26 |  |
| 9 | Cloud Mood | 4:30 |  |
| 10 | Matters of the Heart | 4:51 |  |
