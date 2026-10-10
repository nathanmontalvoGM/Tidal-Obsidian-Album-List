---
title: "I Love My Computer"
artist: "Ninajirachi"
year: 2025
tidal_id: 446039372
tags:
  - ElectroHouse
  - Electropop
  - Electronicore
  - Dance
rating:
---

# I Love My Computer
**Artist:** Ninajirachi
**Year:** 2025

![[_covers/Ninajirachi - I Love My Computer.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/446039372
```
^button-didi
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Ninajirachi%20I%20Love%20My%20Computer
```
^button-s1t6

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
| 1 | London Song | 3:15 |  |
| 2 | iPod Touch | 3:16 |  |
| 3 | Fuck My Computer | 3:10 |  |
| 4 | CSIRAC | 3:21 |  |
| 5 | Delete | 3:51 |  |
| 6 | ฅ^•ﻌ•^ฅ | 1:06 |  |
| 7 | All I Am | 3:02 |  |
| 8 | Infohazard | 4:29 |  |
| 9 | Battery Death | 3:18 |  |
| 10 | Sing Good | 2:40 |  |
| 11 | It's You | 2:49 |  |
| 12 | All At Once | 5:27 |  |
