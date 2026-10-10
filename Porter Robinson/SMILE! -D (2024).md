---
title: SMILE! :D
artist: Porter Robinson
year: 2024
tidal_id: 376814627
tags:
  - Favorite
  - Electropop
  - Poprock
  - Indietronica
  - Indierock
rating:
---

# SMILE! :D
**Artist:** Porter Robinson
**Year:** 2024

![[_covers/Porter Robinson - SMILE! -D.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/376814627
```
^button-62fj
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Porter%20Robinson%20SMILE%21%20%3AD
```
^button-rz9e

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
| 1 | Knock Yourself Out XD | 2:48 |  |
| 2 | Cheerleader | 3:57 |  |
| 3 | Russian Roulette | 6:28 |  |
| 4 | Perfect Pinterest Garden | 2:28 |  |
| 5 | Year of the Cup | 4:22 |  |
| 6 | Kitsune Maison Freestyle | 3:53 |  |
| 7 | Easier to Love You | 4:10 |  |
| 8 | Mona Lisa | 3:45 |  |
| 9 | Is There Really No Happiness? | 3:19 |  |
| 10 | Everything to Me (outro fade) | 4:46 |  |
