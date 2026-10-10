---
title: "From Hell With Love"
artist: "Beast In Black"
year: 2019
tidal_id: 99855943
tags:
  - Powermetal
  - Heavymetal
  - Numetal
  - Motorheadcover
rating:
---

# From Hell With Love
**Artist:** Beast In Black
**Year:** 2019

![[_covers/Beast In Black - From Hell With Love.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/99855943
```
^button-2swx
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Beast%20In%20Black%20From%20Hell%20With%20Love
```
^button-gsmu

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
| 1 | Cry Out for a Hero | 3:27 |  |
| 2 | From Hell With Love | 3:55 |  |
| 3 | Sweet True Lies | 3:26 |  |
| 4 | Repentless | 4:02 |  |
| 5 | Die by the Blade | 3:14 |  |
| 6 | Oceandeep | 5:46 |  |
| 7 | Unlimited Sin | 3:34 |  |
| 8 | True Believer | 3:28 |  |
| 9 | This Is War | 3:39 |  |
| 10 | Heart of Steel | 4:22 |  |
| 11 | No Surrender | 4:15 |  |
| 12 | Killed by Death | 3:52 |  |
| 13 | No Easy Way Out | 4:05 |  |
