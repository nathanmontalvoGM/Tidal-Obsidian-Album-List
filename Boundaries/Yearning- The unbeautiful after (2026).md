---
title: "Yearning: The unbeautiful after"
artist: "Boundaries"
year: 2026
tidal_id: 543652451
tags: []
rating:
---

# Yearning: The unbeautiful after
**Artist:** Boundaries
**Year:** 2026

![[_covers/Boundaries - Yearning- The unbeautiful after.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/543652451
```
^button-84eq
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Boundaries%20Yearning%3A%20The%20unbeautiful%20after
```
^button-aamw

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
| 1 | Malconscience | 2:21 |  |
| 2 | Skies cast amber black | 3:01 |  |
| 3 | May this pain never leave | 3:25 |  |
| 4 | Torn wide open | 3:26 |  |
| 5 | Bitter ash, bitter love | 2:51 |  |
| 6 | Unequal whole | 2:55 |  |
| 7 | Death will follow me | 4:03 |  |
| 8 | The leper's bell | 3:44 |  |
| 9 | Crowned and crucified | 3:51 |  |
| 10 | Wasted angel | 2:25 |  |
| 11 | Evidence of extinction | 2:43 |  |
| 12 | Nothing, gathered | 4:27 |  |
| 13 | Only endless | 4:01 |  |
| 14 | Yearning: The unbeautiful after | 3:49 |  |
