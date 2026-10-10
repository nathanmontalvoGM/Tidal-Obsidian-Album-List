---
title: "Director's Cuts"
artist: "To The Grave"
year: 2023
tidal_id: 253985929
tags:
  - Deathcore
  - Album2023
rating:
---

# Director's Cuts
**Artist:** To The Grave
**Year:** 2023

![[_covers/To The Grave - Director's Cuts.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/253985929
```
^button-efwn
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=To%20The%20Grave%20Director%27s%20Cuts
```
^button-x3ru

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
| 1 | Warning Shot | 1:44 |  |
| 2 | Red Dot Sight | 3:26 |  |
| 3 | Full Sequence | 3:35 |  |
| 4 | B.D.T.S | 3:17 |  |
| 5 | Protest and Sever | 4:25 |  |
| 6 | Manhunt | 3:38 |  |
| 7 | Found Footage | 3:43 |  |
| 8 | Axe of Kindness | 4:08 |  |
| 9 | Reversing the Bear Trap | 3:25 |  |
| 10 | Cut Off the Head | 3:30 |  |
| 11 | Die, Rise | 8:29 |  |
