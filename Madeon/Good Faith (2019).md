---
title: "Good Faith"
artist: "Madeon"
year: 2019
tidal_id: 122276416
tags:
  - Electronicore
  - Electropop
  - Pop
  - Synthpop
rating:
---

# Good Faith
**Artist:** Madeon
**Year:** 2019

![[_covers/Madeon - Good Faith.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/122276416
```
^button-6unn
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Madeon%20Good%20Faith
```
^button-r69f

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
| 1 | Dream Dream Dream | 3:55 |  |
| 2 | All My Friends | 3:25 |  |
| 3 | Be Fine | 3:29 |  |
| 4 | Nirvana | 2:32 |  |
| 5 | Mania | 2:33 |  |
| 6 | Miracle | 4:10 |  |
| 7 | No Fear No More | 3:15 |  |
| 8 | Hold Me Just Because | 3:06 |  |
| 9 | Heavy With Hoping | 4:01 |  |
| 10 | Borealis | 4:46 |  |
