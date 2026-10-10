---
title: "Vector"
artist: "Haken"
year: 2018
tidal_id: 94071070
tags:
  - Progressivemetal
  - Djent
  - Progressivepop
  - Prog
rating:
---

# Vector
**Artist:** Haken
**Year:** 2018

![[_covers/Haken - Vector.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/94071070
```
^button-wk66
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Haken%20Vector
```
^button-7how

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
| 1-1 | Clear | 1:50 |  |
| 1-2 | The Good Doctor | 3:56 |  |
| 1-3 | Puzzle Box | 7:43 |  |
| 1-4 | Veil | 12:35 |  |
| 1-5 | Nil by Mouth | 6:51 |  |
| 2-1 | Host | 6:45 |  |
| 2-2 | A Cell Divides | 6:04 |  |
| 3-1 | Clear | 1:50 |  |
| 3-2 | The Good Doctor | 3:56 |  |
| 3-3 | Puzzle Box | 7:43 |  |
| 3-4 | Veil | 12:35 |  |
| 3-5 | Nil by Mouth | 6:51 |  |
| 3-6 | Host | 6:45 |  |
| 3-7 | A Cell Divides | 6:04 |  |
