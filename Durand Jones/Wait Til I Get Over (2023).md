---
title: "Wait Til I Get Over"
artist: "Durand Jones"
year: 2023
tidal_id: 273584760
tags:
  - Soul
  - Neosoul
  - Funk
rating:
---

# Wait Til I Get Over
**Artist:** Durand Jones
**Year:** 2023

![[_covers/Durand Jones - Wait Til I Get Over.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/273584760
```
^button-i9g2
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Durand%20Jones%20Wait%20Til%20I%20Get%20Over
```
^button-bslo

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
| 1 | Gerri Marie | 2:45 |  |
| 2 | The Place You’d Most Want to Live (interlude) | 1:09 |  |
| 3 | Lord Have Mercy | 4:01 |  |
| 4 | Sadie | 2:56 |  |
| 5 | I Want You | 4:04 |  |
| 6 | Wait Til I Get Over | 3:01 |  |
| 7 | That Feeling | 4:22 |  |
| 8 | See It Through (interlude) | 1:24 |  |
| 9 | See It Through | 3:24 |  |
| 10 | Someday We’ll All Be Free | 4:03 |  |
| 11 | Letter to My 17 Year Old Self | 5:47 |  |
| 12 | Secrets | 4:11 |  |
