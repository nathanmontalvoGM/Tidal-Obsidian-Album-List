---
title: "Lost Weekend"
artist: "Phoebe Bridgers"
year: 2026
tidal_id: 550858406
tags: []
rating:
---

# Lost Weekend
**Artist:** Phoebe Bridgers
**Year:** 2026

![[_covers/Phoebe Bridgers - Lost Weekend.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/550858406
```
^button-xzo9
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Phoebe%20Bridgers%20Lost%20Weekend
```
^button-y4lo

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
| 1-1 | The Outside | 3:57 |  |
| 1-2 | Lost Boys | 4:14 |  |
| 1-3 | Kill Me | 4:41 |  |
| 1-4 | The Governor’s Waltz | 3:27 |  |
| 1-5 | Bobby | 3:59 |  |
| 1-6 | Lost Weekend | 3:38 |  |
| 1-7 | Haunted | 3:34 |  |
| 1-8 | Panorama | 2:46 |  |
| 1-9 | Still Standing | 3:56 |  |
| 1-10 | Liberty Tree | 3:17 |  |
| 2-1 | Never Going Back! | 1:42 |  |
| 2-2 | Other Plans | 2:20 |  |
| 2-3 | Lost Parade | 0:55 |  |
| 2-4 | I Can’t Wait | 3:37 |  |
| 2-5 | As Above | 4:24 |  |
| 2-6 | Lost Weekend (reprise) | 1:59 |  |
