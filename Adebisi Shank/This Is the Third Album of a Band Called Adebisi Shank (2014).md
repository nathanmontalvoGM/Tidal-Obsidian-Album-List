---
title: "This Is the Third Album of a Band Called Adebisi Shank"
artist: "Adebisi Shank"
year: 2014
tidal_id: 430140479
tags:
  - Bestof2019
  - Myrainynightsintokyo
  - Personalfavourites
  - Mathrock
rating:
---

# This Is the Third Album of a Band Called Adebisi Shank
**Artist:** Adebisi Shank
**Year:** 2014

![[_covers/Adebisi Shank - This Is the Third Album of a Band Called Adebisi Shank.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/430140479
```
^button-kdwj
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Adebisi%20Shank%20This%20Is%20the%20Third%20Album%20of%20a%20Band%20Called%20Adebisi%20Shank
```
^button-3ibj

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
| 1 | World in Harmony | 5:11 |  |
| 2 | Big Unit | 4:35 |  |
| 3 | Turnaround | 3:16 |  |
| 4 | Mazel Tov | 3:49 |  |
| 5 | Thundertruth | 2:37 |  |
| 6 | Sensation | 5:14 |  |
| 7 | Chaos Emeralds | 3:41 |  |
| 8 | Voodoo Vision | 6:00 |  |
| 9 | (Trio Always) | 1:05 |  |
