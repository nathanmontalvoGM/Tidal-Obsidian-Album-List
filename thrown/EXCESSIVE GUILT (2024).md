---
title: "EXCESSIVE GUILT"
artist: "thrown"
year: 2024
tidal_id: 363349693
tags:
  - Numetal
rating:
---

# EXCESSIVE GUILT
**Artist:** thrown
**Year:** 2024

![[_covers/thrown - EXCESSIVE GUILT.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/363349693
```
^button-8zl8
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=thrown%20EXCESSIVE%20GUILT
```
^button-5woa

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
| 1 | guilt | 2:36 |  |
| 2 | backfire | 2:00 |  |
| 3 | on the verge | 2:14 |  |
| 4 | bitter friend | 1:54 |  |
| 5 | nights | 2:02 |  |
| 6 | look at me | 1:30 |  |
| 7 | dislike | 2:03 |  |
| 8 | ignored | 1:00 |  |
| 9 | bloodsucker | 1:59 |  |
| 10 | vent | 1:30 |  |
| 11 | so done | 2:00 |  |
