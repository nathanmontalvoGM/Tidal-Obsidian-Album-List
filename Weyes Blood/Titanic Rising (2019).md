---
title: "Titanic Rising"
artist: "Weyes Blood"
year: 2019
tidal_id: 105356343
tags:
  - Wsum917fmmadison
  - BaroquePop
  - ArtPop
  - Softrock
rating:
---

# Titanic Rising
**Artist:** Weyes Blood
**Year:** 2019

![[_covers/Weyes Blood - Titanic Rising.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/105356343
```
^button-okb7
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Weyes%20Blood%20Titanic%20Rising
```
^button-5qsv

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
| 1 | A Lot’s Gonna Change | 4:21 |  |
| 2 | Andromeda | 4:40 |  |
| 3 | Everyday | 5:07 |  |
| 4 | Something to Believe | 4:45 |  |
| 5 | Titanic Rising | 1:36 |  |
| 6 | Movies | 5:53 |  |
| 7 | Mirror Forever | 5:05 |  |
| 8 | Wild Time | 6:09 |  |
| 9 | Picture Me Better | 3:41 |  |
| 10 | Nearer to Thee | 1:05 |  |
