---
title: "Negative Spaces"
artist: "Poppy"
year: 2024
tidal_id: 383686884
tags:
  - Alternativemetal
  - Metalcore
  - Numetal
  - Alternativerock
rating:
---

# Negative Spaces
**Artist:** Poppy
**Year:** 2024

![[_covers/Poppy - Negative Spaces.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/383686884
```
^button-wwhi
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Poppy%20Negative%20Spaces
```
^button-3vgg

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
| 1 | have you had enough? | 3:38 |  |
| 2 | the cost of giving up | 3:18 |  |
| 3 | they’re all around us | 3:25 |  |
| 4 | yesterday | 0:48 |  |
| 5 | crystallized | 3:07 |  |
| 6 | vital | 3:20 |  |
| 7 | push go | 3:33 |  |
| 8 | nothing | 3:04 |  |
| 9 | the center’s falling out | 2:25 |  |
| 10 | hey there | 1:29 |  |
| 11 | negative spaces | 2:55 |  |
| 12 | surviving on defiance | 3:28 |  |
| 13 | new way out | 3:23 |  |
| 14 | tomorrow | 0:52 |  |
| 15 | halo | 3:41 |  |
