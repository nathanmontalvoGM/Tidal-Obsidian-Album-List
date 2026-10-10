---
title: "Where we've been, Where we go from here"
artist: "Friko"
year: 2024
tidal_id: 322984947
tags:
  - Indierock
  - Chamberpop
  - NoisePop
  - Midwestemo
rating:
---

# Where we've been, Where we go from here
**Artist:** Friko
**Year:** 2024

![[_covers/Friko - Where we've been, Where we go from here.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/322984947
```
^button-p15a
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Friko%20Where%20we%27ve%20been%2C%20Where%20we%20go%20from%20here
```
^button-mhn8

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
| 1 | Where We’ve Been | 5:15 |  |
| 2 | Crimson to Chrome | 3:28 |  |
| 3 | Crashing Through | 3:43 |  |
| 4 | For Ella | 4:03 |  |
| 5 | Chemical | 3:22 |  |
| 6 | Statues | 3:54 |  |
| 7 | Until I’m With You Again | 3:33 |  |
| 8 | Get Numb to It! | 4:52 |  |
| 9 | Cardinal | 3:54 |  |
