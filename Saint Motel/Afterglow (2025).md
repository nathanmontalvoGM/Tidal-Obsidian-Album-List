---
title: Afterglow
artist: Saint Motel
year: 2025
tidal_id: 460006293
tags:
  - Poprock
  - Chamberpop
  - Indiepop
  - Indierock
rating:
---

# Afterglow
**Artist:** Saint Motel
**Year:** 2025

![[_covers/Saint Motel - Afterglow.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/460006293
```
^button-e28k
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Saint%20Motel%20Afterglow
```
^button-e5le

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
| 1 | Room With a View (For the End of the World) | 4:34 |  |
| 2 | Wait & See | 4:34 |  |
| 3 | Hold My Breath | 3:14 |  |
| 4 | Peace n Love n Anarchy | 3:18 |  |
| 5 | Let Me Down Gently | 3:54 |  |
| 6 | Can I Paint You | 3:25 |  |
| 7 | Free Refills | 2:56 |  |
| 8 | Divine | 2:49 |  |
| 9 | Where the Sunset Goes | 3:44 |  |
| 10 | Up & Away We Go | 3:00 |  |
