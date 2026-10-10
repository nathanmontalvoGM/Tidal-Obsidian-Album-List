---
title: "WE WERE JUST HERE"
artist: "Just Mustard"
year: 2025
tidal_id: 442370656
tags:
  - Noise
  - Alternativerock
  - Postrock
  - Postpunk
rating:
---

# WE WERE JUST HERE
**Artist:** Just Mustard
**Year:** 2025

![[_covers/Just Mustard - WE WERE JUST HERE.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/442370656
```
^button-cuxn
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Just%20Mustard%20WE%20WERE%20JUST%20HERE
```
^button-2rlw

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
| 1 | WE WERE JUST HERE | 3:40 |  |
| 2 | POLLYANNA | 4:24 |  |
