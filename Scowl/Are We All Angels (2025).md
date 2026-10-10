---
title: "Are We All Angels"
artist: "Scowl"
year: 2025
tidal_id: 406144346
tags:
  - Grunge
  - Punkrock
  - Postpunk
  - HardcorePunk
rating:
---

# Are We All Angels
**Artist:** Scowl
**Year:** 2025

![[_covers/Scowl - Are We All Angels.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/406144346
```
^button-o9py
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Scowl%20Are%20We%20All%20Angels
```
^button-un7h

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
| 1 | Special | 2:57 |  |
| 2 | B.A.B.E. | 2:33 |  |
| 3 | Fantasy | 3:29 |  |
| 4 | Not Hell, Not Heaven | 3:01 |  |
| 5 | Tonight (I’m Afraid) | 3:25 |  |
| 6 | Fleshed Out | 2:22 |  |
| 7 | Let You Down | 3:16 |  |
| 8 | Cellophane | 2:23 |  |
| 9 | Suffer the Fool (How High Are You?) | 3:15 |  |
| 10 | Haunted | 3:16 |  |
| 11 | Are We All Angels | 2:48 |  |
