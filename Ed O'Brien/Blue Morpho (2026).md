---
title: "Blue Morpho"
artist: "Ed O'Brien"
year: 2026
tidal_id: 495187955
tags: []
rating:
---

# Blue Morpho
**Artist:** Ed O'Brien
**Year:** 2026

![[_covers/Ed O'Brien - Blue Morpho.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/495187955
```
^button-0fut
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Ed%20O%27Brien%20Blue%20Morpho
```
^button-5ztl

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
| 1 | Blue Morpho | 6:18 |  |
