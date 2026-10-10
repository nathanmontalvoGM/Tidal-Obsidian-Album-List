---
title: "Extreme Power Metal"
artist: "DragonForce"
year: 2019
tidal_id: 113025554
tags:
  - Powermetal
  - Speedmetal
  - Kerrang
  - Heavymetal
rating:
---

# Extreme Power Metal
**Artist:** DragonForce
**Year:** 2019

![[_covers/DragonForce - Extreme Power Metal.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/113025554
```
^button-zqhj
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=DragonForce%20Extreme%20Power%20Metal
```
^button-8if5

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
| 1 | Highway to Oblivion | 6:48 |  |
| 2 | Cosmic Power of the Infinite Shred Machine | 6:36 |  |
| 3 | The Last Dragonborn | 6:12 |  |
| 4 | Heart Demolition | 5:39 |  |
| 5 | Troopers of the Stars | 5:03 |  |
| 6 | Razorblade Meltdown | 4:45 |  |
| 7 | Strangers | 4:29 |  |
| 8 | In a Skyforged Dream | 4:45 |  |
| 9 | Remembrance Day | 5:10 |  |
| 10 | My Heart Will Go On | 3:24 |  |
| 11 | Behind the Mirror of Death | 5:32 |  |
