---
title: "Elegy"
artist: "Shadow of Intent"
year: 2022
tidal_id: 197837547
tags:
  - Deathcore
  - Symphonicmetal
  - Symphonicmelodicdeath
  - Numetal
rating:
---

# Elegy
**Artist:** Shadow of Intent
**Year:** 2022

![[_covers/Shadow of Intent - Elegy.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/197837547
```
^button-5fb2
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Shadow%20of%20Intent%20Elegy
```
^button-776h

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
| 1 | Farewell | 4:56 |  |
| 2 | Saurian King | 5:24 |  |
| 3 | The Coming Fire | 4:09 |  |
| 4 | Of Fury | 4:48 |  |
| 5 | Intensified Genocide | 4:01 |  |
| 6 | Life of Exile | 4:53 |  |
| 7 | Where Millions Have Come to Die | 4:23 |  |
| 8 | From Ruin… We Rise | 4:51 |  |
| 9 | Blood in the Sands of Time | 5:22 |  |
| 10 | Reconquest | 4:51 |  |
| 11 | Elegy I: Adapt | 2:29 |  |
| 12 | Elegy II: Devise | 4:26 |  |
| 13 | Elegy III: Overcome | 6:01 |  |
