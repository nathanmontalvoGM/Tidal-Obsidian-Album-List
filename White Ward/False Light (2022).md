---
title: "False Light"
artist: "White Ward"
year: 2022
tidal_id: 216462544
tags:
  - Bestof2022
  - Jazz
  - Progressivemetal
  - Blackmetal
rating:
---

# False Light
**Artist:** White Ward
**Year:** 2022

![[_covers/White Ward - False Light.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/216462544
```
^button-wjg7
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=White%20Ward%20False%20Light
```
^button-hahu

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
| 1 | Leviathan | 13:17 |  |
| 2 | Salt Paradise | 5:21 |  |
| 3 | Phoenix | 10:49 |  |
| 4 | Silence Circles | 9:13 |  |
| 5 | Echoes in Eternity | 3:29 |  |
| 6 | Cronus | 6:20 |  |
| 7 | False Light | 14:43 |  |
| 8 | Downfall | 3:15 |  |
