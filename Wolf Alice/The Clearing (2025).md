---
title: "The Clearing"
artist: "Wolf Alice"
year: 2025
tidal_id: 452964378
tags:
  - Indierock
  - Softrock
  - BaroquePop
  - Poprock
rating:
---

# The Clearing
**Artist:** Wolf Alice
**Year:** 2025

![[_covers/Wolf Alice - The Clearing.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/452964378
```
^button-ao1k
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Wolf%20Alice%20The%20Clearing
```
^button-ls2u

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
| 1 | Thorns | 3:14 |  |
| 2 | Bloom Baby Bloom | 3:47 |  |
| 3 | Just Two Girls | 3:49 |  |
| 4 | Leaning Against the Wall | 4:11 |  |
| 5 | Passenger Seat | 2:52 |  |
| 6 | Play It Out | 4:11 |  |
| 7 | Bread Butter Tea Sugar | 3:28 |  |
| 8 | Safe in the World | 3:31 |  |
| 9 | Midnight Song | 2:50 |  |
| 10 | White Horses | 4:29 |  |
| 11 | The Sofa | 4:26 |  |
