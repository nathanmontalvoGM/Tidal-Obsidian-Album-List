---
title: Dereliction
artist: Larcɇnia Roɇ
year: 2024
tidal_id: 359953981
tags:
  - Deathcore
rating:
---

# Dereliction
**Artist:** Larcɇnia Roɇ
**Year:** 2024

![[_covers/Larcɇnia Roɇ - Dereliction.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/359953981
```
^button-xxms
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Larc%C9%87nia%20Ro%C9%87%20Dereliction
```
^button-39bd

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
| 1 | Smile | 4:02 |  |
| 2 | Unhinged | 3:49 |  |
| 3 | Precursor | 2:36 |  |
| 4 | Nose Tork | 4:54 |  |
| 5 | Alienation | 5:48 |  |
| 6 | Onlooker | 2:54 |  |
| 7 | Slippy Slide | 4:07 |  |
