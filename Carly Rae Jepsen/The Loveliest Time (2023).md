---
title: "The Loveliest Time"
artist: "Carly Rae Jepsen"
year: 2023
tidal_id: 306420760
tags:
  - Aoty
  - Pop
  - ContemporaryRnb
  - Electropop
rating:
---

# The Loveliest Time
**Artist:** Carly Rae Jepsen
**Year:** 2023

![[_covers/Carly Rae Jepsen - The Loveliest Time.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/306420760
```
^button-3q89
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Carly%20Rae%20Jepsen%20The%20Loveliest%20Time
```
^button-3z47

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
| 1 | Anything to Be With You | 3:17 |  |
| 2 | Kamikaze | 2:59 |  |
| 3 | After Last Night | 3:28 |  |
| 4 | Aeroplanes | 3:20 |  |
| 5 | Shy Boy | 3:29 |  |
| 6 | Kollage | 4:16 |  |
| 7 | Shadow | 2:49 |  |
| 8 | Psychedelic Switch | 4:32 |  |
| 9 | So Right | 3:36 |  |
| 10 | Come Over | 2:54 |  |
| 11 | Put It to Rest | 3:17 |  |
| 12 | Stadium Love | 2:51 |  |
