---
title: "Bonito Generation"
artist: "Kero Kero Bonito"
year: 2016
tidal_id: 245928025
tags:
  - Electropop
  - Synthpop
  - Pop
  - Bitpop
rating:
---

# Bonito Generation
**Artist:** Kero Kero Bonito
**Year:** 2016

![[_covers/Kero Kero Bonito - Bonito Generation.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/245928025
```
^button-v8f6
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Kero%20Kero%20Bonito%20Bonito%20Generation
```
^button-ogo9

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
| 1 | Waking Up | 2:57 |  |
| 2 | Heard a Song | 3:19 |  |
| 3 | Graduation | 3:19 |  |
| 4 | Fish Bowl | 1:45 |  |
| 5 | Big City | 2:52 |  |
| 6 | Break | 3:16 |  |
| 7 | Lipslap | 3:39 |  |
| 8 | Try Me | 3:29 |  |
| 9 | Paintbrush | 0:57 |  |
| 10 | Trampoline | 4:03 |  |
| 11 | Picture This | 3:24 |  |
| 12 | Hey Parents | 3:22 |  |
| 13 | Forever Summer Holiday | 3:36 |  |
| 14 | Picture This (Felicita remix) | 3:00 |  |
| 15 | Fish Bowl (Frankie Cosmos remix) | 1:44 |  |
| 16 | Heard a Song (CFCF remix) | 4:05 |  |
| 17 | Trampoline (Saint Etienne remix) | 3:48 |  |
| 18 | Lipslap (Makeness remix) | 3:58 |  |
| 19 | Break (Jonah Baseball remix) | 2:25 |  |
