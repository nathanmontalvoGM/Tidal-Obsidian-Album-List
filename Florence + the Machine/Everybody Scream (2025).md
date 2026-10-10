---
title: "Everybody Scream"
artist: "Florence + the Machine"
year: 2025
tidal_id: 469785152
tags:
  - Folkrock
  - ArtRock
  - ArtPop
  - Alternativerock
rating:
---

# Everybody Scream
**Artist:** Florence + the Machine
**Year:** 2025

![[_covers/Florence + the Machine - Everybody Scream.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/469785152
```
^button-p7az
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Florence%20%2B%20the%20Machine%20Everybody%20Scream
```
^button-meph

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
| 1 | Everybody Scream | 4:04 |  |
