---
title: "Double Infinity"
artist: "Big Thief"
year: 2025
tidal_id: 454086302
tags:
  - Indierock
  - Rock
  - Psychedelicrock
  - Folkrock
rating:
---

# Double Infinity
**Artist:** Big Thief
**Year:** 2025

![[_covers/Big Thief - Double Infinity.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/454086302
```
^button-za6o
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Big%20Thief%20Double%20Infinity
```
^button-tlef

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
| 1 | Incomprehensible | 3:54 |  |
| 2 | Words | 3:47 |  |
| 3 | Los Angeles | 3:57 |  |
| 4 | All Night All Day | 4:48 |  |
| 5 | Double Infinity | 4:12 |  |
| 6 | No Fear | 6:58 |  |
| 7 | Grandmother | 6:00 |  |
| 8 | Happy With You | 4:26 |  |
| 9 | How Could I Have Known | 4:50 |  |
