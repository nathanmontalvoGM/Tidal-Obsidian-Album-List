---
title: "Lonely At The Top"
artist: "Joey Bada$$"
year: 2025
tidal_id: 456515507
tags:
  - Boombap
  - Hardcorehiphop
  - Hiphop
  - Jazzrap
rating:
---

# Lonely At The Top
**Artist:** Joey Bada$$
**Year:** 2025

![[_covers/Joey Bada$$ - Lonely At The Top.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/456515507
```
^button-nq7v
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Joey%20Bada%24%24%20Lonely%20At%20The%20Top
```
^button-wnqv

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
| 1 | DARK AURA | 2:53 |  |
| 2 | SWANK WHITE | 4:18 |  |
| 3 | SUPAFLEE | 3:12 |  |
| 4 | HIGHROLLER | 3:27 |  |
| 5 | READY TO LOVE | 3:00 |  |
| 6 | BK’S FINEST | 4:34 |  |
| 7 | UNDERWATER | 4:12 |  |
| 8 | 3 FEET AWAY | 3:58 |  |
| 9 | SPEEDIN’ THROUGH THE RAIN | 3:14 |  |
| 10 | STILL | 3:26 |  |
| 11 | LONELY AT THE TOP | 3:17 |  |
