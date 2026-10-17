---
title: "Live at Carnegie Hall"
artist: "Cameron Winter"
year: 2026
tidal_id: 552484488
tags: []
rating:
---

# Live at Carnegie Hall
**Artist:** Cameron Winter
**Year:** 2026

![[_covers/Cameron Winter - Live at Carnegie Hall.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/552484488
```
^button-ze1f
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Cameron%20Winter%20Live%20at%20Carnegie%20Hall
```
^button-wj8s

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
| 1 | It All Fell in the River | 4:30 |  |
| 2 | Try as I May | 5:35 |  |
| 3 | Emperor XIII in Shades | 4:18 |  |
| 4 | The Rolling Stones | 4:25 |  |
| 5 | Love Takes Miles | 4:13 |  |
| 6 | Drinking Age | 5:10 |  |
| 7 | Cancer of the Skull | 7:03 |  |
| 8 | If You Turn Back Now | 5:37 |  |
| 9 | Nina + Field of Cops | 6:37 |  |
| 10 | $0 | 8:42 |  |
| 11 | Take It With You | 6:17 |  |
| 12 | Vines | 4:38 |  |
