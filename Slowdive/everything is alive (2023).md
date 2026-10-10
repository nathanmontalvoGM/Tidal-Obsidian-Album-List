---
title: "everything is alive"
artist: "Slowdive"
year: 2023
tidal_id: 295476130
tags:
  - DreamPop
  - Shoegaze
  - Ambient
  - Indierock
rating:
---

# everything is alive
**Artist:** Slowdive
**Year:** 2023

![[_covers/Slowdive - everything is alive.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/295476130
```
^button-chou
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Slowdive%20everything%20is%20alive
```
^button-htdx

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
| 1 | shanty | 5:47 |  |
| 2 | prayer remembered | 4:46 |  |
| 3 | alife | 4:33 |  |
| 4 | andalucia plays | 6:41 |  |
| 5 | kisses | 3:57 |  |
| 6 | skin in the game | 3:52 |  |
| 7 | chained to a cloud | 6:51 |  |
| 8 | the slab | 5:10 |  |
