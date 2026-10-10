---
title: "Worldwide"
artist: "Snõõper"
year: 2025
tidal_id: 445421386
tags:
  - Rock
  - Garagerock
  - GaragePunk
  - Punk
rating:
---

# Worldwide
**Artist:** Snõõper
**Year:** 2025

![[_covers/Snõõper - Worldwide.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/445421386
```
^button-ytzr
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Sn%C3%B5%C3%B5per%20Worldwide
```
^button-b6xm

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
| 1 | Opt Out | 2:04 |  |
| 2 | On Line | 1:13 |  |
| 3 | Company Car | 2:03 |  |
| 4 | Worldwide | 2:34 |  |
| 5 | Guard Dog | 2:48 |  |
| 6 | Hologram | 2:21 |  |
| 7 | Star 6 9 | 3:11 |  |
| 8 | Blockhead | 1:39 |  |
| 9 | Come Together | 1:31 |  |
| 10 | Pom Pom | 2:08 |  |
| 11 | Relay | 2:21 |  |
| 12 | Subdivision | 4:11 |  |
