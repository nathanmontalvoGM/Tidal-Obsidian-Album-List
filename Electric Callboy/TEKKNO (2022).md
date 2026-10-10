---
title: "TEKKNO"
artist: "Electric Callboy"
year: 2022
tidal_id: 224324546
tags:
  - Metalcore
  - Electronicore
  - Trancecore
  - Edm
rating:
---

# TEKKNO
**Artist:** Electric Callboy
**Year:** 2022

![[_covers/Electric Callboy - TEKKNO.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/224324546
```
^button-xnz3
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Electric%20Callboy%20TEKKNO
```
^button-dukb

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
| 1 | Pump It | 2:52 |  |
| 2 | We Got the Moves | 3:26 |  |
| 3 | Fuckboi | 2:44 |  |
| 4 | Spaceman | 3:10 |  |
| 5 | Mindreader | 3:45 |  |
| 6 | Arrow of Love | 3:43 |  |
| 7 | Parasite | 3:03 |  |
| 8 | Tekkno Train | 2:58 |  |
| 9 | Hurrikan | 1:39 |  |
| 10 | Neon | 3:12 |  |
| 11 | Pump It (live) | 3:00 |  |
| 12 | Hate/Love (live) | 3:12 |  |
| 13 | Spaceman (live) | 3:13 |  |
| 14 | We Got the Moves (live) | 3:51 |  |
| 15 | Hypa Hypa (live) | 3:44 |  |
