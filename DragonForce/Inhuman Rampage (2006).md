---
title: "Inhuman Rampage"
artist: "DragonForce"
year: 2006
tidal_id: 34368466
tags:
  - Powermetal
  - Speedmetal
  - Extrememetal
  - Numetal
rating:
---

# Inhuman Rampage
**Artist:** DragonForce
**Year:** 2006

![[_covers/DragonForce - Inhuman Rampage.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/34368466
```
^button-le4i
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=DragonForce%20Inhuman%20Rampage
```
^button-uiyd

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
| 1-1 | Through the Fire and Flames | 7:21 |  |
| 1-2 | Revolution Deathsquad | 7:53 |  |
| 1-3 | Storming the Burning Fields | 5:19 |  |
| 1-4 | Operation Ground and Pound | 7:44 |  |
| 1-5 | Body Breakdown | 6:58 |  |
| 1-6 | Cry for Eternity | 8:12 |  |
| 1-7 | The Flame of Youth | 6:41 |  |
| 1-8 | Trail of Broken Hearts | 5:55 |  |
| 1-9 | Lost Souls in Endless Time | 6:23 |  |
| 2-1 | "Through the Fire and Flames" Music Video |  |  |
| 2-2 | "Operation Ground and Pound" Music Video |  |  |
| 2-3 | Behind-The-Scenes Rocumentary |  |  |
| 2-4 | Bonus Live performance of "My Spirit Will Go On" (from the '06 Metal Hammer Awards) |  |  |
