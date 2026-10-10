---
title: "Crazymad, For Me"
artist: "CMAT"
year: 2023
tidal_id: 295886015
tags:
  - AltCountry
  - Singersongwriter
  - Indiepop
  - Poprock
rating:
---

# Crazymad, For Me
**Artist:** CMAT
**Year:** 2023

![[_covers/CMAT - Crazymad, For Me.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/295886015
```
^button-33nt
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=CMAT%20Crazymad%2C%20For%20Me
```
^button-doiw

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
| 1 | California | 4:05 |  |
| 2 | Phone Me | 3:24 |  |
| 3 | Vincent Kompany | 3:01 |  |
| 4 | Such a Miranda | 2:35 |  |
| 5 | Rent | 4:42 |  |
| 6 | Where Are Your Kids Tonight? | 5:26 |  |
| 7 | Can’t Make Up My Mind | 4:24 |  |
| 8 | Whatever’s Inconvenient | 4:28 |  |
| 9 | I… Hate Who I Am When I'm Horny | 5:13 |  |
| 10 | Torn Apart | 3:20 |  |
| 11 | Stay for Something | 3:36 |  |
| 12 | Have Fun! | 4:30 |  |
