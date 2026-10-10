---
title: Premonitions
artist: Synestia
year: 2025
tidal_id: 455850009
tags:
  - Deathcore
  - Symphonicmetal
rating:
---

# Premonitions
**Artist:** Synestia
**Year:** 2025

![[_covers/Synestia - Premonitions.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/455850009
```
^button-35p0
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Synestia%20Premonitions
```
^button-tk9o

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
| 1 | The Wretched King and His Hollow Throne | 3:55 |  |
| 2 | Dies Irae | 4:44 |  |
| 3 | The Mourning Star | 4:18 |  |
| 4 | Premonitions | 5:57 |  |
