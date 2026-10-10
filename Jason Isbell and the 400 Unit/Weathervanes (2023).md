---
title: "Weathervanes"
artist: "Jason Isbell and the 400 Unit"
year: 2023
tidal_id: 297862726
tags:
  - Southernrock
  - AltCountry
  - Americana
  - Rootsrock
rating:
---

# Weathervanes
**Artist:** Jason Isbell and the 400 Unit
**Year:** 2023

![[_covers/Jason Isbell and the 400 Unit - Weathervanes.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/297862726
```
^button-plur
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Jason%20Isbell%20and%20the%20400%20Unit%20Weathervanes
```
^button-vla3

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
| 1 | Death Wish | 4:30 |  |
| 2 | King of Oklahoma | 5:02 |  |
| 3 | Strawberry Woman | 4:10 |  |
| 4 | Middle of the Morning | 4:40 |  |
| 5 | Save the World | 5:09 |  |
| 6 | If You Insist | 3:45 |  |
| 7 | Cast Iron Skillet | 3:24 |  |
| 8 | When We Were Close | 3:57 |  |
| 9 | Volunteer | 4:05 |  |
| 10 | Vestavia Hills | 4:31 |  |
| 11 | White Beretta | 3:56 |  |
| 12 | This Ain’t It | 6:14 |  |
| 13 | Miles | 7:07 |  |
