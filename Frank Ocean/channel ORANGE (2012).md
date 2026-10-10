---
title: "channel ORANGE"
artist: "Frank Ocean"
year: 2012
tidal_id: 35181031
tags:
  - Rnb
  - Soul
  - Neosoul
  - Rb
rating:
---

# channel ORANGE
**Artist:** Frank Ocean
**Year:** 2012

![[_covers/Frank Ocean - channel ORANGE.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/35181031
```
^button-ukjq
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Frank%20Ocean%20channel%20ORANGE
```
^button-g3ds

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
| 1 | Start | 0:45 |  |
| 2 | Thinkin Bout You | 3:20 |  |
| 3 | Fertilizer | 0:39 |  |
| 4 | Sierra Leone | 2:28 |  |
| 5 | Sweet Life | 4:22 |  |
| 6 | Not Just Money | 1:00 |  |
| 7 | Super Rich Kids | 5:04 |  |
| 8 | Pilot Jones | 3:04 |  |
| 9 | Crack Rock | 3:44 |  |
| 10 | Pyramids | 9:53 |  |
| 11 | Lost | 3:54 |  |
| 12 | White | 1:16 |  |
| 13 | Monks | 3:21 |  |
| 14 | Bad Religion | 2:55 |  |
| 15 | Pink Matter | 4:28 |  |
| 16 | Forrest Gump | 3:15 |  |
| 17 | End / Golden Girl | 8:43 |  |
