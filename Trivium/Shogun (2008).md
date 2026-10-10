---
title: "Shogun"
artist: "Trivium"
year: 2008
tidal_id: 1969292
tags:
  - Heavymetal
  - Melodicmetalcore
  - Metalcore
  - Thrashmetal
rating:
---

# Shogun
**Artist:** Trivium
**Year:** 2008

![[_covers/Trivium - Shogun.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/1969292
```
^button-g5qu
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Trivium%20Shogun
```
^button-zvoy

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
| 1 | Kirisute Gomen | 6:27 |  |
| 2 | Torn Between Scylla and Charybdis | 6:49 |  |
| 3 | Down From the Sky | 5:34 |  |
| 4 | Into the Mouth of Hell We March | 5:52 |  |
| 5 | Throes of Perdition | 5:54 |  |
| 6 | Insurrection | 4:57 |  |
| 7 | The Calamity | 4:58 |  |
| 8 | He Who Spawned the Furies | 4:07 |  |
| 9 | Of Prometheus and the Crucifix | 4:40 |  |
| 10 | Like Callisto to a Star in Heaven | 5:25 |  |
| 11 | Shogun | 11:57 |  |
| 12 | Iron Maiden | 3:43 |  |
