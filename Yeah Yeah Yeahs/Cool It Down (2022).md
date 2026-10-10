---
title: "Cool It Down"
artist: "Yeah Yeah Yeahs"
year: 2022
tidal_id: 228045954
tags:
  - ArtRock
  - Punk
  - Synthpop
  - Alternativerock
rating:
---

# Cool It Down
**Artist:** Yeah Yeah Yeahs
**Year:** 2022

![[_covers/Yeah Yeah Yeahs - Cool It Down.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/228045954
```
^button-oqyy
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Yeah%20Yeah%20Yeahs%20Cool%20It%20Down
```
^button-hbq3

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
| 1 | Spitting Off the Edge of the World | 4:17 |  |
| 2 | Lovebomb | 5:06 |  |
| 3 | Wolf | 4:13 |  |
| 4 | Fleez | 3:58 |  |
| 5 | Burning | 4:05 |  |
| 6 | Blacktop | 4:23 |  |
| 7 | Different Today | 4:27 |  |
| 8 | Mars | 1:55 |  |
