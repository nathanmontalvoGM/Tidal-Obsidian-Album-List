---
title: "Amongst The Low & Empty"
artist: "Signs of the Swarm"
year: 2023
tidal_id: 293059599
tags:
  - Brutaldeathcore
  - Deathcore
rating:
---

# Amongst The Low & Empty
**Artist:** Signs of the Swarm
**Year:** 2023

![[_covers/Signs of the Swarm - Amongst The Low & Empty.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/293059599
```
^button-b87y
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Signs%20of%20the%20Swarm%20Amongst%20The%20Low%20%26%20Empty
```
^button-5kdh

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
| 1 | Amongst the Low & Empty | 4:01 |  |
| 2 | Tower of Torsos | 3:29 |  |
| 3 | Pray for Death | 3:38 |  |
| 4 | Borrowed Time | 2:57 |  |
| 5 | Between Fire & Stone | 3:59 |  |
| 6 | Shackles Like Talons | 4:34 |  |
| 7 | DREAMKILLER | 4:11 |  |
| 8 | The Witch Beckons | 3:02 |  |
| 9 | Echelon | 3:45 |  |
| 10 | Faces Without Names | 4:27 |  |
| 11 | Malady | 4:03 |  |
