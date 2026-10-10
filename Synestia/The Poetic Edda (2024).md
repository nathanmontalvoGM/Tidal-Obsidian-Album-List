---
title: "The Poetic Edda"
artist: "Synestia"
year: 2024
tidal_id: 360034668
tags:
  - Deathcore
  - Neoclassicaldjent
  - Symphonicdeathcore
  - Mathmetal
rating:
---

# The Poetic Edda
**Artist:** Synestia
**Year:** 2024

![[_covers/Synestia - The Poetic Edda.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/360034668
```
^button-tq5k
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Synestia%20The%20Poetic%20Edda
```
^button-mvtw

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
| 1 | Death Empress |  |  |
| 2 | I, The Devourer | 4:57 |  |
| 3 | The Poetic Edda | 6:05 |  |
| 4 | Winter |  |  |
