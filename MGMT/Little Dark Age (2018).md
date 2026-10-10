---
title: "Little Dark Age"
artist: "MGMT"
year: 2018
tidal_id: 84192578
tags:
  - Synthpop
  - Neopsychedelia
  - Darkwave
  - Psychedelicpop
rating:
---

# Little Dark Age
**Artist:** MGMT
**Year:** 2018

![[_covers/MGMT - Little Dark Age.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/84192578
```
^button-tjpy
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=MGMT%20Little%20Dark%20Age
```
^button-v0wx

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
| 1 | Little Dark Age | 4:59 |  |
