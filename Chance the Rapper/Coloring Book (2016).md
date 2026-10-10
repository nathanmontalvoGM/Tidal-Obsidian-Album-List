---
title: "Coloring Book"
artist: "Chance the Rapper"
year: 2016
tidal_id: 60920015
tags:
  - Rap
  - Hiphop
  - Gospel
  - Conscioushiphop
rating:
---

# Coloring Book
**Artist:** Chance the Rapper
**Year:** 2016

![[_covers/Chance the Rapper - Coloring Book.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/60920015
```
^button-wpbj
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Chance%20the%20Rapper%20Coloring%20Book
```
^button-efh8

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
| 1 | All We Got | 3:24 |  |
| 2 | No Problem | 5:05 |  |
| 3 | Summer Friends | 4:50 |  |
| 4 | D.R.A.M. Sings Special | 1:41 |  |
| 5 | Blessings | 3:42 |  |
| 6 | Same Drugs | 4:18 |  |
| 7 | Mixtape | 4:53 |  |
| 8 | Angels | 3:26 |  |
| 9 | Juke Jam | 3:40 |  |
| 10 | All Night | 2:22 |  |
| 11 | How Great | 5:37 |  |
| 12 | Smoke Break | 3:46 |  |
| 13 | Finish Line / Drown | 6:47 |  |
| 14 | Blessings | 3:50 |  |
