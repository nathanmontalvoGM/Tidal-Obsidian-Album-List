---
title: "Evil Empire"
artist: "Rage Against The Machine"
year: 1996
tidal_id: 5120094
tags:
  - Rock
  - Alternativerock
  - Rapcore
  - Political
rating:
---

# Evil Empire
**Artist:** Rage Against The Machine
**Year:** 1996

![[_covers/Rage Against The Machine - Evil Empire.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/5120094
```
^button-ep8u
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Rage%20Against%20The%20Machine%20Evil%20Empire
```
^button-2ndr

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
| 1 | People of the Sun | 2:30 |  |
| 2 | Bulls on Parade | 3:49 |  |
| 3 | Vietnow | 4:37 |  |
| 4 | Revolver | 5:27 |  |
| 5 | Snakecharmer | 3:55 |  |
| 6 | Tire Me | 2:57 |  |
| 7 | Down Rodeo | 5:20 |  |
| 8 | Without a Face | 3:36 |  |
| 9 | Wind Below | 5:50 |  |
| 10 | Roll Right | 4:20 |  |
| 11 | Year of tha Boomerang | 3:59 |  |
