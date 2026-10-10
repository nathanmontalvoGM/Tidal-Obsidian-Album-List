---
title: "The Ballad of Darren"
artist: "Blur"
year: 2023
tidal_id: 304357042
tags:
  - ArtRock
  - Indiepop
  - Indierock
  - BaroquePop
rating:
---

# The Ballad of Darren
**Artist:** Blur
**Year:** 2023

![[_covers/Blur - The Ballad of Darren.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/304357042
```
^button-igmx
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Blur%20The%20Ballad%20of%20Darren
```
^button-5ehu

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
| 1 | The Ballad | 3:37 |  |
| 2 | St. Charles Square | 3:55 |  |
| 3 | Barbaric | 4:08 |  |
| 4 | Russian Strings | 3:37 |  |
| 5 | The Everglades (For Leonard) | 2:56 |  |
| 6 | The Narcissist | 4:05 |  |
| 7 | Goodbye Albert | 4:16 |  |
| 8 | Far Away Island | 2:57 |  |
| 9 | Avalon | 3:05 |  |
| 10 | The Heights | 3:23 |  |
| 11 | The Rabbi | 2:43 |  |
| 12 | The Swan | 3:45 |  |
| 13 | Sticks and Stones | 3:23 |  |
