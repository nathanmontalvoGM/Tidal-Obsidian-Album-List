---
title: "Quest For Fire"
artist: "Skrillex"
year: 2023
tidal_id: 276778735
tags:
  - Dubstep
  - Electronicore
  - UkGarage
  - Edm
rating:
---

# Quest For Fire
**Artist:** Skrillex
**Year:** 2023

![[_covers/Skrillex - Quest For Fire.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/276778735
```
^button-jmsc
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Skrillex%20Quest%20For%20Fire
```
^button-d8br

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
| 1-1 | Leave Me Like This | 3:08 |  |
| 1-2 | Ratata | 2:06 |  |
| 1-3 | Tears | 3:05 |  |
| 1-4 | Rumble | 2:26 |  |
| 1-5 | Butterflies | 3:15 |  |
| 1-6 | Inhale Exhale | 3:25 |  |
| 1-7 | A Street I Know | 3:35 |  |
| 1-8 | Xena | 4:11 |  |
| 2-1 | Too Bizarre (Juked) | 3:28 |  |
| 2-2 | Hydrate | 3:36 |  |
| 2-3 | Warped Tour '05 with Pete Wentz | 0:48 |  |
| 2-4 | Good Space | 2:12 |  |
| 2-5 | Supersonic (My Existence) | 2:45 |  |
| 2-6 | Hazel Theme | 1:51 |  |
| 2-7 | Still Here (With the Ones That I Came With) | 5:03 |  |
