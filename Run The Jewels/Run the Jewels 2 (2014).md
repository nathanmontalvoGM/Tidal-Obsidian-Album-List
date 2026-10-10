---
title: "Run the Jewels 2"
artist: "Run The Jewels"
year: 2014
tidal_id: 185863813
tags:
  - Hiphop
  - Loud
  - Spoken
  - Upbeat
rating:
---

# Run the Jewels 2
**Artist:** Run The Jewels
**Year:** 2014

![[_covers/Run The Jewels - Run the Jewels 2.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/185863813
```
^button-but0
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Run%20The%20Jewels%20Run%20the%20Jewels%202
```
^button-hyjr

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
| 1 | Jeopardy | 3:21 |  |
| 2 | Oh My Darling Don't Cry | 3:24 |  |
| 3 | Blockbuster Night, Pt. 1 | 2:32 |  |
| 4 | Close Your Eyes (and Count to Fuck) | 3:54 |  |
| 5 | All My Life | 3:07 |  |
| 6 | Lie, Cheat, Steal | 3:28 |  |
| 7 | Early | 3:44 |  |
| 8 | All Due Respect | 2:47 |  |
| 9 | Love Again (Akinyele Back) | 3:45 |  |
| 10 | Crown | 3:45 |  |
| 11 | Angel Duster | 5:09 |  |
| 12 | Blockbuster Night, Pt. 2 | 2:39 |  |
