---
title: "INSIDE"
artist: "Bo Burnham"
year: 2021
tidal_id: 189591372
tags:
  - Comedy
  - Netflix
  - Nota10
  - Pop
rating:
---

# INSIDE
**Artist:** Bo Burnham
**Year:** 2021

![[_covers/Bo Burnham - INSIDE.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/189591372
```
^button-wmkq
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Bo%20Burnham%20INSIDE
```
^button-m55b

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
| 1 | Content | 1:36 |  |
| 2 | Comedy | 5:19 |  |
| 3 | Facetime With My Mom (Tonight) | 2:20 |  |
| 4 | How the World Works | 4:15 |  |
| 5 | White Woman’s Instagram | 4:00 |  |
| 6 | Unpaid Intern | 0:34 |  |
| 7 | Bezos I | 0:58 |  |
| 8 | Sexting | 3:21 |  |
| 9 | Look Who’s Inside Again | 1:23 |  |
| 10 | Problematic | 3:13 |  |
| 11 | 30 | 2:34 |  |
| 12 | Don’t Wanna Know | 1:05 |  |
| 13 | Shit | 1:18 |  |
| 14 | All Time Low | 0:54 |  |
| 15 | Welcome to the Internet | 4:36 |  |
| 16 | Bezos II | 0:45 |  |
| 17 | That Funny Feeling | 5:01 |  |
| 18 | All Eyes on Me | 5:02 |  |
| 19 | Goodbye | 4:09 |  |
| 20 | Any Day Now | 0:57 |  |
