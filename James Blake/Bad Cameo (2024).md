---
title: "Bad Cameo"
artist: "James Blake"
year: 2024
tidal_id: 370627605
tags:
  - Ambient
  - Neopsychedelia
  - ArtPop
  - ExperimentalHipHop
rating:
---

# Bad Cameo
**Artist:** James Blake
**Year:** 2024

![[_covers/James Blake - Bad Cameo.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/370627605
```
^button-ogg7
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=James%20Blake%20Bad%20Cameo
```
^button-soiu

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
| 1 | Save the Savior | 4:05 |  |
| 2 | In Grey | 6:10 |  |
| 3 | Midnight | 4:58 |  |
| 4 | Woo | 2:49 |  |
| 5 | Bad Cameo | 3:51 |  |
| 6 | Missing Man | 3:56 |  |
| 7 | Twice | 4:56 |  |
| 8 | Transport Me | 4:56 |  |
| 9 | Run Away From the Rabbit | 3:47 |  |
| 10 | Red Carpet | 4:08 |  |
