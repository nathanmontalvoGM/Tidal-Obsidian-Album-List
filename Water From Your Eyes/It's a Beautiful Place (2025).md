---
title: "It's a Beautiful Place"
artist: "Water From Your Eyes"
year: 2025
tidal_id: 451341791
tags:
  - Rock
  - Indierock
  - Experimentalrock
  - Punk
rating:
---

# It's a Beautiful Place
**Artist:** Water From Your Eyes
**Year:** 2025

![[_covers/Water From Your Eyes - It's a Beautiful Place.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/451341791
```
^button-see0
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Water%20From%20Your%20Eyes%20It%27s%20a%20Beautiful%20Place
```
^button-ierj

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
| 1 | One Small Step | 0:26 |  |
| 2 | Life Signs | 4:32 |  |
| 3 | Nights in Armor | 3:09 |  |
| 4 | Born 2 | 4:24 |  |
| 5 | You Don't Believe in God? | 1:25 |  |
| 6 | Spaceship | 4:49 |  |
| 7 | Playing Classics | 5:53 |  |
| 8 | It's a Beautiful Place | 0:50 |  |
| 9 | Blood on the Dollar | 2:40 |  |
| 10 | For Mankind | 0:59 |  |
