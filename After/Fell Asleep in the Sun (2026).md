---
title: "Fell Asleep in the Sun"
artist: "After"
year: 2026
tidal_id: 561288351
tags: []
rating:
---

# Fell Asleep in the Sun
**Artist:** After
**Year:** 2026

![[_covers/After - Fell Asleep in the Sun.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/561288351
```
^button-l8tt
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=After%20Fell%20Asleep%20in%20the%20Sun
```
^button-dz2i

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
| 1 | Take Me to Sunrise | 3:14 |  |
| 2 | Promise (When You Go) | 3:06 |  |
| 3 | Metal | 3:18 |  |
| 4 | Breathe Your Air | 3:16 |  |
| 5 | Fitfully | 3:01 |  |
| 6 | Do or Die | 2:21 |  |
| 7 | Blow Out the Candle | 3:43 |  |
| 8 | Secret Love Song | 1:34 |  |
| 9 | Open Water | 3:20 |  |
| 10 | Blind | 3:09 |  |
| 11 | Snowburn | 3:38 |  |
| 12 | If You Don’t Know by Now | 3:55 |  |
| 13 | Fell Asleep in the Sun | 3:51 |  |
