---
title: "Rift in Reality"
artist: "Labyrinthus Stellarum"
year: 2025
tidal_id: 422525287
tags:
  - Atmosphericmetal
  - Cybermetal
rating:
---

# Rift in Reality
**Artist:** Labyrinthus Stellarum
**Year:** 2025

![[_covers/Labyrinthus Stellarum - Rift in Reality.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/422525287
```
^button-arbg
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Labyrinthus%20Stellarum%20Rift%20in%20Reality
```
^button-oam4

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
| 1 | Voyagers | 3:55 |  |
| 2 | Ravenous Planet | 5:12 |  |
| 3 | Take Us Home | 4:35 |  |
| 4 | Rift in Reality | 3:46 |  |
| 5 | Lost in the Void | 7:28 |  |
| 6 | Cosmic Plague | 3:41 |  |
| 7 | Liftoff | 5:29 |  |
| 8 | Nirlakh | 3:12 |  |
