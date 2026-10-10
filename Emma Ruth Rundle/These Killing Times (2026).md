---
title: "These Killing Times"
artist: "Emma Ruth Rundle"
year: 2026
tidal_id: 530275562
tags: []
rating:
---

# These Killing Times
**Artist:** Emma Ruth Rundle
**Year:** 2026

![[_covers/Emma Ruth Rundle - These Killing Times.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/530275562
```
^button-dz6o
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Emma%20Ruth%20Rundle%20These%20Killing%20Times
```
^button-3b58

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
| 1 | Powerless | 5:00 |  |
| 2 | God’s Picture | 5:20 |  |
| 3 | Anvil | 5:22 |  |
| 4 | Catherine Wheel | 4:25 |  |
| 5 | Don’t Delay Heaven | 6:20 |  |
| 6 | Enough | 6:29 |  |
| 7 | Human Kindness | 8:24 |  |
| 8 | Oceans of Time | 2:22 |  |
