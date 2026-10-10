---
title: Under the Veil of Madness
artist: ASCENSION
year: 2023
tidal_id: 271324328
tags:
  - Powermetal
rating:
---

# Under the Veil of Madness
**Artist:** ASCENSION
**Year:** 2023

![[_covers/ASCENSION - Under the Veil of Madness.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/271324328
```
^button-giy2
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=ASCENSION%20Under%20the%20Veil%20of%20Madness
```
^button-k32k

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
| 1 | Sayonara | 6:21 |  |
| 2 | Megalomaniac | 3:58 |  |
| 3 | Defiance | 4:59 |  |
| 4 | Monsters | 7:15 |  |
| 5 | Set You Free | 5:35 |  |
| 6 | Last Winter's Night | 9:08 |  |
| 7 | Under the Veil of Madness | 8:45 |  |
| 8 | Power of a Thousand Suns | 3:04 |  |
| 9 | Pages of Gold | 6:19 |  |
