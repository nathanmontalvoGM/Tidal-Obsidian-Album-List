---
title: "Watching from a Distance"
artist: "Warning"
year: 2008
tidal_id: 449897084
tags:
  - Doommetal
  - Rock
rating:
---

# Watching from a Distance
**Artist:** Warning
**Year:** 2008

![[_covers/Warning - Watching from a Distance.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/449897084
```
^button-ddgp
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Warning%20Watching%20from%20a%20Distance
```
^button-ushz

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
| 1-1 | Watching From a Distance | 12:06 |  |
| 1-2 | Footprints | 7:31 |  |
| 2-1 | Bridges | 11:30 |  |
| 2-2 | Faces | 8:31 |  |
| 2-3 | Echoes | 10:16 |  |
