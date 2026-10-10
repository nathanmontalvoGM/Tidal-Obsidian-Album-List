---
title: "Dedicated Side B"
artist: "Carly Rae Jepsen"
year: 2020
tidal_id: 141509574
tags:
  - Pop
  - Synthpop
  - Electropop
  - Dancepop
rating:
---

# Dedicated Side B
**Artist:** Carly Rae Jepsen
**Year:** 2020

![[_covers/Carly Rae Jepsen - Dedicated Side B.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/141509574
```
^button-r7n2
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Carly%20Rae%20Jepsen%20Dedicated%20Side%20B
```
^button-ikjt

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
| 1 | This Love Isn’t Crazy | 3:53 |  |
| 2 | Window | 3:18 |  |
| 3 | Felt This Way | 3:37 |  |
| 4 | Stay Away | 3:37 |  |
| 5 | This Is What They Say | 3:34 |  |
| 6 | Heartbeat | 4:12 |  |
| 7 | Summer Love | 3:15 |  |
| 8 | Fake Mona Lisa | 2:12 |  |
| 9 | Let’s Sort the Whole Thing Out | 3:53 |  |
| 10 | Comeback | 3:43 |  |
| 11 | Solo | 3:16 |  |
| 12 | Now I Don’t Hate California After All | 4:53 |  |
| 13 | Let’s Be Friends | 3:11 |  |
| 14 | Always On My Mind | 3:15 |  |
