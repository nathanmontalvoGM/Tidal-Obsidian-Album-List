---
title: "The Sleeping City"
artist: "An Abstract Illusion"
year: 2025
tidal_id: 466008447
tags:
  - Progressivemetal
  - Mathmetal
  - Melodicdeathmetal
  - Atmosphericmetal
rating:
---

# The Sleeping City
**Artist:** An Abstract Illusion
**Year:** 2025

![[_covers/An Abstract Illusion - The Sleeping City.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/466008447
```
^button-pqlz
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=An%20Abstract%20Illusion%20The%20Sleeping%20City
```
^button-6q8t

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
| 1 | Blackmurmur | 11:00 |  |
| 2 | No Dreams Beyond Empty Horizons | 8:13 |  |
| 3 | Like a Geyser Ever Erupting | 7:58 |  |
| 4 | Frost Flower | 8:14 |  |
| 5 | Emmett | 11:19 |  |
| 6 | Silverfields | 3:46 |  |
| 7 | The Sleeping City | 10:07 |  |
