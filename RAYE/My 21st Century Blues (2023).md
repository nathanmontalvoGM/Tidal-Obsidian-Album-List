---
title: "My 21st Century Blues"
artist: "RAYE"
year: 2023
tidal_id: 270052032
tags:
  - Pop
  - Poprap
  - Blues
  - House
rating:
---

# My 21st Century Blues
**Artist:** RAYE
**Year:** 2023

![[_covers/RAYE - My 21st Century Blues.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/270052032
```
^button-yqf2
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=RAYE%20My%2021st%20Century%20Blues
```
^button-ctg9

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
| 1 | Introduction. | 0:57 |  |
| 2 | Oscar Winning Tears. | 3:03 |  |
| 3 | Hard Out Here. | 3:10 |  |
| 4 | Black Mascara. | 3:59 |  |
| 5 | Escapism. | 4:32 |  |
| 6 | Mary Jane. | 3:52 |  |
| 7 | The Thrill Is Gone. | 3:19 |  |
| 8 | Ice Cream Man. | 4:08 |  |
| 9 | Flip a Switch. | 3:21 |  |
| 10 | Body Dysmorphia. | 2:33 |  |
| 11 | Environmental Anxiety. | 3:14 |  |
| 12 | Five Star Hotels. | 3:24 |  |
| 13 | Worth It. | 4:06 |  |
| 14 | Buss It Down. | 2:37 |  |
| 15 | Fin. | 0:31 |  |
