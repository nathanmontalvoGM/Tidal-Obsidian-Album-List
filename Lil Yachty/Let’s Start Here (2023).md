---
title: "Let’s Start Here."
artist: "Lil Yachty"
year: 2023
tidal_id: 273619903
tags:
  - Psychedelicrock
  - Neopsychedelia
  - Psychedelicpop
  - Spacerock
rating:
---

# Let’s Start Here.
**Artist:** Lil Yachty
**Year:** 2023

![[_covers/Lil Yachty - Let’s Start Here.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/273619903
```
^button-50ka
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Lil%20Yachty%20Let%E2%80%99s%20Start%20Here.
```
^button-282e

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
| 1 | the BLACK seminole. | 6:52 |  |
| 2 | the ride- | 3:11 |  |
| 3 | running out of time | 4:29 |  |
| 4 | pRETTy | 2:42 |  |
| 5 | :(failure(: | 2:47 |  |
| 6 | THE zone~ | 4:10 |  |
| 7 | WE SAW THE SUN! | 5:31 |  |
| 8 | drive ME crazy! | 3:50 |  |
| 9 | IVE OFFICIALLY LOST ViSiON!!!! | 5:22 |  |
| 10 | sAy sOMETHINg | 3:33 |  |
| 11 | paint THE sky | 3:05 |  |
| 12 | sHouLd i B? | 2:49 |  |
| 13 | The Alchemist. | 2:57 |  |
| 14 | REACH THE SUNSHINE. | 5:58 |  |
