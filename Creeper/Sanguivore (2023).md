---
title: "Sanguivore"
artist: "Creeper"
year: 2023
tidal_id: 320529126
tags:
  - Conceptalbum
  - Steinmanesque
  - 35
  - Bestof2022
rating:
---

# Sanguivore
**Artist:** Creeper
**Year:** 2023

![[_covers/Creeper - Sanguivore.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/320529126
```
^button-ns7m
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Creeper%20Sanguivore
```
^button-g4to

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
| 1 | Further Than Forever | 9:12 |  |
| 2 | Cry to Heaven | 4:27 |  |
| 3 | Sacred Blasphemy | 2:53 |  |
| 4 | The Ballad of Spook & Mercy | 4:39 |  |
| 5 | Lovers Led Astray | 4:40 |  |
| 6 | Teenage Sacrifice | 4:17 |  |
| 7 | Chapel Gates | 2:23 |  |
| 8 | The Abyss | 0:42 |  |
| 9 | Black Heaven | 4:15 |  |
| 10 | More Than Death | 4:38 |  |
