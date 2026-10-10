---
title: The Wicked Rule The Night
artist: Avantasia
year: 2022
tidal_id: 227167252
tags:
  - Powermetal
  - RockOpera
  - Symphonicdeathcore
rating:
---

# The Wicked Rule The Night
**Artist:** Avantasia
**Year:** 2022

![[_covers/Avantasia - The Wicked Rule The Night.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/227167252
```
^button-7b6i
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Avantasia%20The%20Wicked%20Rule%20The%20Night
```
^button-541m

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
| 1 | The Wicked Rule the Night | 4:24 |  |
