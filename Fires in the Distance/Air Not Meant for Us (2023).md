---
title: "Air Not Meant for Us"
artist: "Fires in the Distance"
year: 2023
tidal_id: 249625968
tags:
  - Numetal
  - Progdeathmetal
  - Melodicdeathmetal
  - Deathdoommetal
rating:
---

# Air Not Meant for Us
**Artist:** Fires in the Distance
**Year:** 2023

![[_covers/Fires in the Distance - Air Not Meant for Us.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/249625968
```
^button-bhr7
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Fires%20in%20the%20Distance%20Air%20Not%20Meant%20for%20Us
```
^button-pihc

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
| 1 | Harbingers | 10:41 |  |
| 2 | Wisdom of the Falling Leaves | 7:34 |  |
| 3 | Crumbling Pillars of a Tranquil Mind | 9:23 |  |
| 4 | Adrift, Beneath the Listless Waves | 6:01 |  |
| 5 | Psalm of the Merciless | 7:05 |  |
| 6 | Idiopathic Despair | 9:03 |  |
