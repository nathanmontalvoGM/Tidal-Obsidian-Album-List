---
title: "Moonlover"
artist: "Ghost Bath"
year: 2016
tidal_id: 107100531
tags:
  - Blackgaze
  - Blackmetal
  - Atmosphericmetal
  - Depressiveblackmetal
rating:
---

# Moonlover
**Artist:** Ghost Bath
**Year:** 2016

![[_covers/Ghost Bath - Moonlover.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/107100531
```
^button-ech8
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Ghost%20Bath%20Moonlover
```
^button-duoq

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
| 1 | The Sleeping Fields | 1:27 |  |
| 2 | Golden Number | 9:08 |  |
| 3 | Happyhouse | 8:44 |  |
| 4 | Beneath the Shade Tree | 4:47 |  |
| 5 | The Silver Flower, Part 1 | 4:03 |  |
| 6 | The Silver Flower, Part 2 | 7:32 |  |
| 7 | Death and the Maiden | 6:25 |  |
| 8 | Ascension | 7:26 |  |
