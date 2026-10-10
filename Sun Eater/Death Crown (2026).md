---
title: "Death Crown"
artist: "Sun Eater"
year: 2026
tidal_id: 495964280
tags: []
rating:
---

# Death Crown
**Artist:** Sun Eater
**Year:** 2026

![[_covers/Sun Eater - Death Crown.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/495964280
```
^button-9cnx
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Sun%20Eater%20Death%20Crown
```
^button-6deq

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
| 1 | Death Crown | 3:35 |  |
| 2 | Wounds | 3:47 |  |
