---
title: "Moonglow"
artist: "Avantasia"
year: 2019
tidal_id: 99893966
tags:
  - Powermetal
  - Symphonicmetal
  - Metalopera
  - MelodicMetalcore
rating:
---

# Moonglow
**Artist:** Avantasia
**Year:** 2019

![[_covers/Avantasia - Moonglow.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/99893966
```
^button-epv7
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Avantasia%20Moonglow
```
^button-qf5h

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
| 1 | Ghost in the Moon | 9:52 |  |
| 2 | Book of Shallows | 5:00 |  |
| 3 | Moonglow | 3:56 |  |
| 4 | The Raven Child | 11:15 |  |
| 5 | Starlight | 3:39 |  |
| 6 | Invincible | 3:07 |  |
| 7 | Alchemy | 7:28 |  |
| 8 | The Piper at the Gates of Dawn | 7:21 |  |
| 9 | Lavender | 4:31 |  |
| 10 | Requiem for a Dream | 6:09 |  |
| 11 | Maniac | 4:32 |  |
| 12 | Heart | 3:49 |  |
