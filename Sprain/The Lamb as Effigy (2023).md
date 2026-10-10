---
title: "The Lamb as Effigy"
artist: "Sprain"
year: 2023
tidal_id: 298402972
tags:
  - Experimentalrock
  - Noiserock
  - Postrock
  - Drone
rating:
---

# The Lamb as Effigy
**Artist:** Sprain
**Year:** 2023

![[_covers/Sprain - The Lamb as Effigy.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/298402972
```
^button-er8j
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Sprain%20The%20Lamb%20as%20Effigy
```
^button-w82r

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
| 1 | Man Proposes, God Disposes | 7:09 |  |
| 2 | Reiterations | 6:42 |  |
| 3 | Privilege of Being | 5:28 |  |
| 4 | Margin for Error | 24:36 |  |
| 5 | The Commercial Nude | 10:54 |  |
| 6 | The Reclining Nude | 12:56 |  |
| 7 | We Think So Ill of You | 4:15 |  |
| 8 | God, or Whatever You Call It | 24:38 |  |
