---
title: All The Devils Are Here
artist: Mugshot
year: 2025
tidal_id: 424725089
tags:
  - Metalcore
  - BeatdownHardcore
rating:
---

# All The Devils Are Here
**Artist:** Mugshot
**Year:** 2025

![[_covers/Mugshot - All The Devils Are Here.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/424725089
```
^button-fezh
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Mugshot%20All%20The%20Devils%20Are%20Here
```
^button-n4m6

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
| 1 | Die in Fear | 1:30 |  |
| 2 | Afore a Waking Nightmare | 1:38 |  |
| 3 | Shame | 2:05 |  |
| 4 | Vale of Tears | 2:01 |  |
| 5 | Skin the Rabbit | 1:56 |  |
| 6 | I Will Be Here Forever | 3:02 |  |
| 7 | Flesh of My Body | 0:39 |  |
| 8 | Baptized in Concrete | 3:06 |  |
| 9 | Where Your Sins Will Lie | 2:09 |  |
| 10 | All the Devils Are Here | 2:34 |  |
| 11 | Me & You | 2:30 |  |
| 12 | Next to Your Idols | 2:24 |  |
