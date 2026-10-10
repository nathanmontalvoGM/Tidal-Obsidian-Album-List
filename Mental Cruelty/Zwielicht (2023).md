---
title: "Zwielicht"
artist: "Mental Cruelty"
year: 2023
tidal_id: 284264964
tags:
  - Symphonicmetal
  - Deathcore
  - Blackeneddeathcore
  - Blackmetal
rating:
---

# Zwielicht
**Artist:** Mental Cruelty
**Year:** 2023

![[_covers/Mental Cruelty - Zwielicht.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/284264964
```
^button-qtxm
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Mental%20Cruelty%20Zwielicht
```
^button-kiv2

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
| 1 | Midtvinter | 1:43 |  |
| 2 | Obsessis a Daemonio | 5:07 |  |
| 3 | Forgotten Kings | 5:57 |  |
| 4 | Pest | 5:52 |  |
| 5 | Nordlys | 5:19 |  |
| 6 | Mortal Shells | 6:11 |  |
| 7 | Zwielicht | 1:33 |  |
| 8 | Symphony of a Dying Star | 4:11 |  |
| 9 | The Arrogance of Agony | 5:22 |  |
| 10 | A Tale of Salt and Light | 7:31 |  |
