---
title: "Purple"
artist: "Baroness"
year: 2015
tidal_id: 68739189
tags:
  - Progressivemetal
  - SludgeMetal
  - Purple
  - Baroness
rating:
---

# Purple
**Artist:** Baroness
**Year:** 2015

![[_covers/Baroness - Purple.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/68739189
```
^button-jc3k
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Baroness%20Purple
```
^button-uo88

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
| 1 | Morningstar | 4:16 |  |
| 2 | Shock Me | 4:17 |  |
| 3 | Try to Disappear | 4:52 |  |
| 4 | Kerosene | 5:10 |  |
| 5 | Fugue | 2:34 |  |
| 6 | Chlorine & Wine | 6:49 |  |
| 7 | The Iron Bell | 4:24 |  |
| 8 | Desperation Burns | 4:14 |  |
| 9 | If I Have to Wake Up (Would You Stop the Rain?) | 5:41 |  |
| 10 | Crossroads of Infinity | 0:16 |  |
