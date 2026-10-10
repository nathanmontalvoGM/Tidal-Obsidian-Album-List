---
title: "Empty Hands"
artist: "Poppy"
year: 2026
tidal_id: 492022483
tags:
  - Alternativemetal
  - Emo
  - Alternativerock
  - Metalcore
rating:
---

# Empty Hands
**Artist:** Poppy
**Year:** 2026

![[_covers/Poppy - Empty Hands.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/492022483
```
^button-l512
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Poppy%20Empty%20Hands
```
^button-nyfq

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
| 1 | Public Domain | 4:00 |  |
| 2 | Bruised Sky | 3:40 |  |
| 3 | Guardian | 3:14 |  |
| 4 | Constantly Nowhere | 0:28 |  |
| 5 | Unravel | 2:55 |  |
| 6 | Dying to Forget | 3:33 |  |
| 7 | Time Will Tell | 3:27 |  |
| 8 | Eat the Hate | 1:50 |  |
| 9 | The Wait | 3:46 |  |
| 10 | If We’re Following the Light | 4:06 |  |
| 11 | Blink | 0:44 |  |
| 12 | Ribs | 3:39 |  |
| 13 | Empty Hands | 3:09 |  |
