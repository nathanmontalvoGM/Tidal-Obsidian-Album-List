---
title: "OK ORCHESTRA"
artist: "AJR"
year: 2021
tidal_id: 490905700
tags:
  - Pop
  - 2020s
  - Indiepop
  - Alternativerock
rating:
---

# OK ORCHESTRA
**Artist:** AJR
**Year:** 2021

![[_covers/AJR - OK ORCHESTRA.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/490905700
```
^button-3fv6
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=AJR%20OK%20ORCHESTRA
```
^button-ei5o

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
| 1 | OK Overture | 4:31 |  |
| 2 | Bummerland | 3:09 |  |
| 3 | 3 O’Clock Things | 3:48 |  |
| 4 | My Play | 3:10 |  |
| 5 | Joe | 3:32 |  |
| 6 | Adventure Is Out There | 3:31 |  |
| 7 | Bang! | 2:50 |  |
| 8 | The Trick | 2:50 |  |
| 9 | Ordinaryish People | 3:39 |  |
| 10 | Humpty Dumpty | 3:37 |  |
| 11 | World’s Smallest Violin | 3:00 |  |
| 12 | Way Less Sad | 3:26 |  |
| 13 | Christmas in June | 4:39 |  |
