---
title: "My Ghosts Go Ghost"
artist: "By Storm"
year: 2026
tidal_id: 490209783
tags:
  - Glitchpop
  - Electronicore
  - Folktronica
  - Illbient
rating:
---

# My Ghosts Go Ghost
**Artist:** By Storm
**Year:** 2026

![[_covers/By Storm - My Ghosts Go Ghost.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/490209783
```
^button-onhq
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=By%20Storm%20My%20Ghosts%20Go%20Ghost
```
^button-ufgt

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
| 1 | Can I Have You for Myself? | 5:21 |  |
| 2 | Dead Weight | 4:28 |  |
| 3 | Grapefruit | 4:20 |  |
| 4 | In My Town | 7:02 |  |
| 5 | Zig Zag | 6:56 |  |
| 6 | Best Interest | 4:28 |  |
| 7 | Double Trio 2 | 5:10 |  |
| 8 | And I Dance | 4:19 |  |
| 9 | GGG | 4:02 |  |
