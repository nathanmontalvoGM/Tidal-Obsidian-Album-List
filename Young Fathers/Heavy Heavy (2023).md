---
title: "Heavy Heavy"
artist: "Young Fathers"
year: 2023
tidal_id: 272941544
tags:
  - ArtPop
  - Ninjatune
  - 2023albums
  - Rock
rating:
---

# Heavy Heavy
**Artist:** Young Fathers
**Year:** 2023

![[_covers/Young Fathers - Heavy Heavy.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/272941544
```
^button-6fa9
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Young%20Fathers%20Heavy%20Heavy
```
^button-rk39

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
| 1 | Rice | 2:40 |  |
| 2 | I Saw | 3:27 |  |
| 3 | Drum | 3:38 |  |
| 4 | Tell Somebody | 3:10 |  |
| 5 | Geronimo | 3:33 |  |
| 6 | Shoot Me Down | 3:28 |  |
| 7 | Ululation | 2:53 |  |
| 8 | Sink or Swim | 3:04 |  |
| 9 | Holy Moly | 3:29 |  |
| 10 | Be Your Lady | 3:23 |  |
| 11 | I Saw (instrumental) | 3:31 |  |
| 12 | Tell Somebody (instrumental) | 3:13 |  |
| 13 | Geronimo (instrumental) | 3:33 |  |
| 14 | Be Your Lady (instrumental) | 3:14 |  |
