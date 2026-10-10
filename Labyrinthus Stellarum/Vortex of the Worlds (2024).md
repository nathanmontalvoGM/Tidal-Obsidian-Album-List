---
title: "Vortex of the Worlds"
artist: "Labyrinthus Stellarum"
year: 2024
tidal_id: 348113874
tags:
  - Atmosphericmetal
  - Spaceambient
  - Blackmetal
  - CyberMetal
rating:
---

# Vortex of the Worlds
**Artist:** Labyrinthus Stellarum
**Year:** 2024

![[_covers/Labyrinthus Stellarum - Vortex of the Worlds.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/348113874
```
^button-kkph
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Labyrinthus%20Stellarum%20Vortex%20of%20the%20Worlds
```
^button-91qp

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
| 1 | Transcendence | 6:39 |  |
| 2 | Downfall | 6:31 |  |
| 3 | Interstellar Wandering | 4:55 |  |
| 4 | From the Nothingness | 5:11 |  |
| 5 | The Light of Dying Worlds | 7:54 |  |
| 6 | Vortex of the Worlds | 5:54 |  |
