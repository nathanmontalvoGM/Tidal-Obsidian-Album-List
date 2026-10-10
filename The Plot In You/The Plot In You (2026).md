---
title: "The Plot In You"
artist: "The Plot In You"
year: 2026
tidal_id: 539685518
tags: []
rating:
---

# The Plot In You
**Artist:** The Plot In You
**Year:** 2026

![[_covers/The Plot In You - The Plot In You.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/539685518
```
^button-b5zt
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=The%20Plot%20In%20You%20The%20Plot%20In%20You
```
^button-4ka3

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
| 1 | Divide | 3:28 |  |
| 2 | Left Behind | 3:26 |  |
| 3 | Forgotten | 2:55 |  |
| 4 | Closure | 3:13 |  |
| 5 | Don’t Look Away | 3:13 |  |
| 6 | All That I Can Give | 3:18 |  |
| 7 | Been Here Before | 4:27 |  |
| 8 | Pretend | 3:05 |  |
| 9 | Spare Me | 3:37 |  |
| 10 | Silence | 3:11 |  |
| 11 | You Get One | 3:00 |  |
| 12 | Carved | 3:18 |  |
