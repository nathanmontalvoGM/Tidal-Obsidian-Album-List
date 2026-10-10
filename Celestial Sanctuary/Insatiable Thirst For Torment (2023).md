---
title: Insatiable Thirst For Torment
artist: Celestial Sanctuary
year: 2023
tidal_id: 297487451
tags:
  - DeathMetal
rating:
---

# Insatiable Thirst For Torment
**Artist:** Celestial Sanctuary
**Year:** 2023

![[_covers/Celestial Sanctuary - Insatiable Thirst For Torment.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/297487451
```
^button-dbji
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Celestial%20Sanctuary%20Insatiable%20Thirst%20For%20Torment
```
^button-spz6

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
| 1 | Trapped Within the Rank Membrane | 6:26 |  |
| 2 | Glutted With Chunder | 4:21 |  |
| 3 | Swivel Eyed and Gurning in the Shadows | 5:27 |  |
| 4 | Meandering Stream of Foul Fluid | 4:31 |  |
| 5 | Biomineralization (Cell Death) | 5:49 |  |
| 6 | The Lurid Glow of a Dead, Burning Body | 4:04 |  |
| 7 | Unquenchable Thirst… | 6:04 |  |
| 8 | Gutted With a Blunt Blade | 3:41 |  |
