---
title: "Pirouette"
artist: "Model/Actriz"
year: 2025
tidal_id: 414848562
tags:
  - DancePunk
  - Industrialrock
  - Ebm
  - Rock
rating:
---

# Pirouette
**Artist:** Model/Actriz
**Year:** 2025

![[_covers/Model-Actriz - Pirouette.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/414848562
```
^button-49np
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Model/Actriz%20Pirouette
```
^button-ycjz

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
| 1 | Vespers | 3:26 |  |
| 2 | Cinderella | 4:34 |  |
| 3 | Poppy | 3:37 |  |
| 4 | Diva | 4:16 |  |
| 5 | Headlights | 1:33 |  |
| 6 | Acid Rain | 5:24 |  |
| 7 | Departures | 4:31 |  |
| 8 | Audience | 2:55 |  |
| 9 | Ring Road | 2:03 |  |
| 10 | Doves | 4:11 |  |
| 11 | Baton | 4:16 |  |
