---
title: "Twin Plagues"
artist: "Wednesday"
year: 2021
tidal_id: 233502396
tags:
  - Indierock
  - Indiepop
  - Wsum917fmmadison
  - Neckofthewoods
rating:
---

# Twin Plagues
**Artist:** Wednesday
**Year:** 2021

![[_covers/Wednesday - Twin Plagues.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/233502396
```
^button-2pq0
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Wednesday%20Twin%20Plagues
```
^button-31d9

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
| 1 | Twin Plagues | 4:08 |  |
| 2 | Handsome Man | 2:28 |  |
| 3 | The Burned Down Dairy Queen | 3:08 |  |
| 4 | Cliff | 2:40 |  |
| 5 | How Can You Live If You Can't Love How Can You If You Do | 3:02 |  |
| 6 | Cody's Only | 2:31 |  |
| 7 | Toothache | 2:39 |  |
| 8 | Birthday Song | 3:16 |  |
| 9 | One More Last One | 3:19 |  |
| 10 | Three Sisters | 2:16 |  |
| 11 | Gary's | 2:11 |  |
| 12 | Ghost of a Dog | 2:24 |  |
