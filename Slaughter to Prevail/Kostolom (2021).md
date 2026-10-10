---
title: "Kostolom"
artist: "Slaughter to Prevail"
year: 2021
tidal_id: 438800048
tags:
  - Deathcore
  - Numetal
  - Mathmetal
rating:
---

# Kostolom
**Artist:** Slaughter to Prevail
**Year:** 2021

![[_covers/Slaughter to Prevail - Kostolom.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/438800048
```
^button-duc2
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Slaughter%20to%20Prevail%20Kostolom
```
^button-yv3j

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
| 1 | Bonebreaker | 4:25 |  |
| 2 | Demolisher | 3:36 |  |
| 3 | Baba Yaga | 4:15 |  |
| 4 | Made in Russia | 3:55 |  |
| 5 | Zavali Ebalo | 3:57 |  |
| 6 | Agony | 3:51 |  |
| 7 | Your Only | 3:53 |  |
| 8 | I Killed a Man | 4:05 |  |
| 9 | Bratva | 4:50 |  |
| 10 | Ouroboros | 3:51 |  |
| 11 | Head on a Plate | 4:28 |  |
| 12 | Father | 3:56 |  |
