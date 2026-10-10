---
title: "The Money Store"
artist: "Death Grips"
year: 2012
tidal_id: 14558039
tags:
  - Hiphop
  - ExperimentalHipHop
  - IndustrialHipHop
  - Experimentalrock
rating:
---

# The Money Store
**Artist:** Death Grips
**Year:** 2012

![[_covers/Death Grips - The Money Store.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/14558039
```
^button-s00m
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Death%20Grips%20The%20Money%20Store
```
^button-pqfj

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
| 1 | Get Got | 2:51 |  |
| 2 | The Fever (Aye Aye) | 3:07 |  |
| 3 | Lost Boys | 3:06 |  |
| 4 | Blackjack | 2:22 |  |
| 5 | I’ve Seen Footage | 3:22 |  |
