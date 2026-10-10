---
title: "Victory"
artist: "Madeon"
year: 2026
tidal_id: 534836233
tags: []
rating:
---

# Victory
**Artist:** Madeon
**Year:** 2026

![[_covers/Madeon - Victory.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/534836233
```
^button-dg0a
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Madeon%20Victory
```
^button-xztr

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
| 1 | Hi! | 2:22 |  |
| 2 | Car Crash Baby | 3:17 |  |
| 3 | Super Platinum | 2:32 |  |
| 4 | Dancing on Your Grave | 3:59 |  |
| 5 | Somebody Else | 3:13 |  |
| 6 | Fire Away | 3:27 |  |
| 7 | Chaos Magic | 3:17 |  |
| 8 | Enjoy | 3:01 |  |
| 9 | Red Jacket | 2:58 |  |
| 10 | Lonely Space Age | 3:50 |  |
