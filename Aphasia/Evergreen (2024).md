---
title: Evergreen
artist: Aphasia
year: 2024
tidal_id: 359542499
tags:
  - Metalcore
rating:
---

# Evergreen
**Artist:** Aphasia
**Year:** 2024

![[_covers/Aphasia - Evergreen.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/359542499
```
^button-vrjt
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Aphasia%20Evergreen
```
^button-ptk5

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
| 1 | Evergreen | 3:31 |  |
| 2 | In Death | 3:36 |  |
| 3 | Buying Time | 3:22 |  |
