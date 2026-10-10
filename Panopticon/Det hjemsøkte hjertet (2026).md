---
title: "Det hjemsøkte hjertet"
artist: "Panopticon"
year: 2026
tidal_id: 501418812
tags: []
rating:
---

# Det hjemsøkte hjertet
**Artist:** Panopticon
**Year:** 2026

![[_covers/Panopticon - Det hjemsøkte hjertet.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/501418812
```
^button-65qm
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Panopticon%20Det%20hjems%C3%B8kte%20hjertet
```
^button-21pq

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
| 1 | Woodland Caribou | 12:10 |  |
| 2 | The Great Silence, Extinct | 8:54 |  |
| 3 | Blood and Fur Upon the Melting Snow | 12:14 |  |
| 4 | The White Cedars | 8:30 |  |
| 5 | A Culture of Wilderness | 9:04 |  |
| 6 | Lyset | 1:43 |  |
| 7 | Ghost Eyes in the Fire Light | 13:50 |  |
