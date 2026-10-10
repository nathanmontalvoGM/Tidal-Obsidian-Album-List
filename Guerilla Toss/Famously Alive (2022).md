---
title: "Famously Alive"
artist: "Guerilla Toss"
year: 2022
tidal_id: 217835547
tags:
  - Synthpop
  - NoisePop
  - Zolo
  - Synthpunk
rating:
---

# Famously Alive
**Artist:** Guerilla Toss
**Year:** 2022

![[_covers/Guerilla Toss - Famously Alive.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/217835547
```
^button-rz3o
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Guerilla%20Toss%20Famously%20Alive
```
^button-50mb

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
| 1 | Cannibal Capital | 4:24 |  |
| 2 | Famously Alive | 2:05 |  |
| 3 | Live Exponential | 2:35 |  |
| 4 | Mermaid Airplane | 2:59 |  |
| 5 | Wild Fantasy | 4:29 |  |
| 6 | Pyramid Humm | 3:57 |  |
| 7 | Excitable Girls | 2:39 |  |
| 8 | I Got Spirit | 3:05 |  |
| 9 | Happy Me | 4:08 |  |
| 10 | Heathen in Me | 3:13 |  |
