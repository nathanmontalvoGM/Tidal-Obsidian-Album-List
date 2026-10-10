---
title: "Time Heals Everything"
artist: "Blu"
year: 2026
tidal_id: 505811027
tags:
  - Hiphop
rating:
---

# Time Heals Everything
**Artist:** Blu
**Year:** 2026

![[_covers/Blu - Time Heals Everything.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/505811027
```
^button-gdlz
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Blu%20Time%20Heals%20Everything
```
^button-d3jl

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
| 1 | Soul Unusual | 4:32 |  |
| 2 | Shoe Laces | 4:39 |  |
| 3 | Crumbs | 3:39 |  |
| 4 | The Bag | 4:19 |  |
| 5 | Hard Times | 5:32 |  |
| 6 | I Don't Rhyme | 6:16 |  |
| 7 | Lazy Afternoon | 4:41 |  |
| 8 | In my Window | 4:16 |  |
| 9 | T.S.O.D. | 4:26 |  |
| 10 | Time Heals Everything | 6:30 |  |
