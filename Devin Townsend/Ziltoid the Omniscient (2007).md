---
title: "Ziltoid the Omniscient"
artist: "Devin Townsend"
year: 2007
tidal_id: 51971817
tags:
  - Progressivemetal
  - Coffeemetal
  - Numetal
  - Rock
rating:
---

# Ziltoid the Omniscient
**Artist:** Devin Townsend
**Year:** 2007

![[_covers/Devin Townsend - Ziltoid the Omniscient.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/51971817
```
^button-j3xi
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Devin%20Townsend%20Ziltoid%20the%20Omniscient
```
^button-d8l4

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
| 1-1 | ZTO | 1:17 |  |
| 1-2 | By Your Command | 8:10 |  |
| 1-3 | Ziltoidia Attaxx!!! | 3:43 |  |
| 1-4 | Solar Winds | 9:47 |  |
| 1-5 | Hyperdrive | 3:48 |  |
| 1-6 | N9 | 5:31 |  |
| 1-7 | Planet Smasher | 5:45 |  |
| 1-8 | Omnidimensional Creator | 0:48 |  |
| 1-9 | Color Your World | 9:45 |  |
| 1-10 | The Greys | 4:15 |  |
| 1-11 | Tall Latte | 1:03 |  |
| 2-1 | Messages From Ziltoid | 7:34 |  |
| 2-2 | Travelling Salesman | 2:14 |  |
| 2-3 | Another Road | 4:31 |  |
