---
title: "Idols"
artist: "Yungblud"
year: 2025
tidal_id: 441807306
tags:
  - Rock
  - Alternativerock
  - Bitpop
  - Hardrock
rating:
---

# Idols
**Artist:** Yungblud
**Year:** 2025

![[_covers/Yungblud - Idols.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/441807306
```
^button-1qrv
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Yungblud%20Idols
```
^button-53e1

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
| 1 | Hello Heaven, Hello | 9:06 |  |
| 2 | Idols Pt. 1 | 3:35 |  |
| 3 | Lovesick Lullaby | 2:55 |  |
| 4 | Zombie | 4:06 |  |
| 5 | The Greatest Parade | 3:55 |  |
| 6 | Change | 3:28 |  |
| 7 | Monday Murder | 2:54 |  |
| 8 | Ghosts | 6:26 |  |
| 9 | Fire | 2:32 |  |
| 10 | War | 3:50 |  |
| 11 | Idols Pt. II | 1:41 |  |
| 12 | Supermoon | 3:12 |  |
