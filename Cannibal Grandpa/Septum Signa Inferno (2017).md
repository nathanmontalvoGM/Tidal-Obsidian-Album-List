---
title: "Septum Signa Inferno"
artist: "Cannibal Grandpa"
year: 2017
tidal_id: 78445008
tags:
  - Deathcore
  - Rock
rating:
---

# Septum Signa Inferno
**Artist:** Cannibal Grandpa
**Year:** 2017

![[_covers/Cannibal Grandpa - Septum Signa Inferno.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/78445008
```
^button-mieg
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Cannibal%20Grandpa%20Septum%20Signa%20Inferno
```
^button-8b2y

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
| 1 | Kingdom Under Your Feet | 4:16 |  |
| 2 | Drown In Silver | 2:57 |  |
| 3 | Cerberus | 4:01 |  |
| 4 | The Empire Of The Snake | 3:35 |  |
| 5 | Mandinga | 2:04 |  |
| 6 | Genesis | 3:27 |  |
| 7 | The Crown | 2:52 |  |
| 8 | Septum Signa Inferno | 4:17 |  |
