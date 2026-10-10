---
title: "Flesh Stays Together"
artist: "Dying Wish"
year: 2025
tidal_id: 460069364
tags:
  - Metalcore
  - Hardcore
  - Alternativemetal
  - HardcorePunk
rating:
---

# Flesh Stays Together
**Artist:** Dying Wish
**Year:** 2025

![[_covers/Dying Wish - Flesh Stays Together.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/460069364
```
^button-io31
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Dying%20Wish%20Flesh%20Stays%20Together
```
^button-jz5r

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
| 1 | I Don’t Belong Anywhere | 4:04 |  |
| 2 | A Curse Upon Iron | 3:55 |  |
| 3 | I’ll Know You’re Not Around | 3:43 |  |
| 4 | Revenge in Carnage | 2:27 |  |
| 5 | Nothing Like You | 4:14 |  |
| 6 | Surrender Everything | 2:57 |  |
| 7 | Moments I Regret | 3:43 |  |
| 8 | Empty the Chamber | 2:47 |  |
| 9 | Heaven Departs | 4:03 |  |
| 10 | Flesh Stays Together | 4:02 |  |
