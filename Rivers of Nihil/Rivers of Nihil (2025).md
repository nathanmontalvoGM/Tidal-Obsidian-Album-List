---
title: "Rivers of Nihil"
artist: "Rivers of Nihil"
year: 2025
tidal_id: 405710169
tags:
  - Progressivemetal
  - Mathmetal
  - Deathcore
  - Numetal
rating:
---

# Rivers of Nihil
**Artist:** Rivers of Nihil
**Year:** 2025

![[_covers/Rivers of Nihil - Rivers of Nihil.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/405710169
```
^button-efhf
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Rivers%20of%20Nihil%20Rivers%20of%20Nihil
```
^button-7n0o

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
| 1 | The Sub‐Orbital Blues | 4:18 |  |
| 2 | Dustman | 4:33 |  |
| 3 | Criminals | 4:32 |  |
| 4 | Despair Church | 6:30 |  |
| 5 | Water & Time | 5:24 |  |
| 6 | House of Light | 5:49 |  |
| 7 | Evidence | 4:22 |  |
| 8 | American Death | 5:23 |  |
| 9 | The Logical End | 6:07 |  |
| 10 | Rivers of Nihil | 3:16 |  |
