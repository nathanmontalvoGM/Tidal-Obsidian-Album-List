---
title: "For the first time"
artist: "Black Country, New Road"
year: 2021
tidal_id: 160225315
tags:
  - Postpunk
  - Experimentalrock
  - Postrock
  - Crankwave
rating:
---

# For the first time
**Artist:** Black Country, New Road
**Year:** 2021

![[_covers/Black Country, New Road - For the first time.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/160225315
```
^button-i42c
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Black%20Country%2C%20New%20Road%20For%20the%20first%20time
```
^button-vhbx

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
| 1 | Instrumental | 5:27 |  |
| 2 | Athens, France | 6:22 |  |
| 3 | Science Fair | 6:20 |  |
| 4 | Sunglasses | 9:50 |  |
| 5 | Track X | 4:44 |  |
| 6 | Opus | 8:01 |  |
