---
title: "The Hives Forever Forever The Hives"
artist: "The Hives"
year: 2025
tidal_id: 456037754
tags:
  - Garagerock
  - Indierock
  - Sweden
  - Garagerockrevival
rating:
---

# The Hives Forever Forever The Hives
**Artist:** The Hives
**Year:** 2025

![[_covers/The Hives - The Hives Forever Forever The Hives.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/456037754
```
^button-zam0
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=The%20Hives%20The%20Hives%20Forever%20Forever%20The%20Hives
```
^button-ezqg

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
| 1 | The Hives Forever Forever the Hives | 3:03 |  |
| 2 | Legalize Living | 3:24 |  |
| 3 | Paint a Picture | 2:48 |  |
| 4 | Enough Is Enough | 2:49 |  |
