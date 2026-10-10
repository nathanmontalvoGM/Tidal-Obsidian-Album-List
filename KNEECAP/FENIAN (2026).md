---
title: "FENIAN"
artist: "KNEECAP"
year: 2026
tidal_id: 519187418
tags:
  - Hiphop
  - Hardcorehiphop
rating:
---

# FENIAN
**Artist:** KNEECAP
**Year:** 2026

![[_covers/KNEECAP - FENIAN.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/519187418
```
^button-flkd
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=KNEECAP%20FENIAN
```
^button-uuqy

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
| 1 | Éire go Deo | 2:19 |  |
| 2 | Smugglers & Scholars | 3:11 |  |
| 3 | Carnival | 2:52 |  |
| 4 | Palestine | 2:36 |  |
| 5 | Liars Tale | 3:17 |  |
| 6 | FENIAN | 3:14 |  |
| 7 | Big Bad Mo | 3:44 |  |
| 8 | Headcase | 2:40 |  |
| 9 | An Ra | 3:40 |  |
| 10 | Cold at the Top | 3:20 |  |
| 11 | Occupied 6 | 2:04 |  |
| 12 | Gael Phonics | 2:34 |  |
| 13 | Cocaine Hill | 3:27 |  |
| 14 | Irish Goodbye | 3:34 |  |
