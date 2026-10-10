---
title: "Descent"
artist: "Immolation"
year: 2026
tidal_id: 514122912
tags:
  - 14Wochen
  - OffizielleCharts
  - Plattentestsde
rating:
---

# Descent
**Artist:** Immolation
**Year:** 2026

![[_covers/Immolation - Descent.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/514122912
```
^button-1aiv
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Immolation%20Descent
```
^button-cw5n

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
| 1 | These Vengeful Winds | 4:04 |  |
| 2 | The Ephemeral Curse | 3:57 |  |
| 3 | God’s Last Breath | 4:22 |  |
| 4 | Adversary | 3:17 |  |
| 5 | Attrition | 4:44 |  |
| 6 | Bend Towards the Dark | 3:56 |  |
| 7 | Host | 4:12 |  |
| 8 | False Ascent | 3:49 |  |
| 9 | Banished | 3:17 |  |
| 10 | Descent | 5:57 |  |
