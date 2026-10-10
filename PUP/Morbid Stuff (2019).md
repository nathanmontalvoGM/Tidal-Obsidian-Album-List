---
title: "Morbid Stuff"
artist: "PUP"
year: 2019
tidal_id: 104818954
tags:
  - PopPunk
  - Vinyl
  - Powerpop
  - Indierock
rating:
---

# Morbid Stuff
**Artist:** PUP
**Year:** 2019

![[_covers/PUP - Morbid Stuff.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/104818954
```
^button-vron
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=PUP%20Morbid%20Stuff
```
^button-iehe

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
| 1 | Morbid Stuff | 2:44 |  |
| 2 | Kids | 3:30 |  |
| 3 | Free At Last | 2:34 |  |
| 4 | See You At Your Funeral | 3:40 |  |
| 5 | Scorpion Hill | 5:08 |  |
| 6 | Closure | 3:08 |  |
| 7 | Bloody Mary, Kate and Ashley | 2:44 |  |
| 8 | Sibling Rivalry | 3:27 |  |
| 9 | Full Blown Meltdown | 2:32 |  |
| 10 | Bare Hands | 3:35 |  |
| 11 | City | 3:51 |  |
