---
title: "The Crux"
artist: "Djo"
year: 2025
tidal_id: 412355330
tags:
  - Rock
  - Softrock
  - Indie
  - Indiepop
rating:
---

# The Crux
**Artist:** Djo
**Year:** 2025

![[_covers/Djo - The Crux.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/412355330
```
^button-l0oy
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Djo%20The%20Crux
```
^button-uixn

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
| 1 | Lonesome Is a State of Mind | 4:19 |  |
| 2 | Basic Being Basic | 2:38 |  |
| 3 | Link | 3:15 |  |
| 4 | Potion | 2:47 |  |
| 5 | Delete Ya | 3:23 |  |
| 6 | Egg | 4:35 |  |
| 7 | Fly | 5:25 |  |
| 8 | Charlie’s Garden | 3:25 |  |
| 9 | Gap Tooth Smile | 2:58 |  |
| 10 | Golden Line | 3:22 |  |
| 11 | Back on You | 5:23 |  |
| 12 | Crux | 3:43 |  |
