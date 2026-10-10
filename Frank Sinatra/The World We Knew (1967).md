---
title: "The World We Knew"
artist: "Frank Sinatra"
year: 1967
tidal_id: 22629352
tags:
  - Swing
  - Jazz
  - EasyListening
  - FrankSinatra
rating:
---

# The World We Knew
**Artist:** Frank Sinatra
**Year:** 1967

![[_covers/Frank Sinatra - The World We Knew.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/22629352
```
^button-nkj6
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Frank%20Sinatra%20The%20World%20We%20Knew
```
^button-5bg1

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
| 1 | The World We Knew (Over and Over) | 2:47 |  |
| 2 | Somethin’ Stupid | 2:42 |  |
| 3 | This Is My Love | 3:33 |  |
| 4 | Born Free | 2:02 |  |
| 5 | Don't Sleep in the Subway | 2:19 |  |
| 6 | This Town | 3:02 |  |
| 7 | This Is My Song | 2:27 |  |
| 8 | You Are There | 3:28 |  |
| 9 | Drinking Again | 3:10 |  |
| 10 | Some Enchanted Evening | 2:35 |  |
