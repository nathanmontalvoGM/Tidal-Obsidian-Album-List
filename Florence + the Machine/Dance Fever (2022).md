---
title: "Dance Fever"
artist: "Florence + the Machine"
year: 2022
tidal_id: 228279663
tags:
  - Indiepop
  - BaroquePop
  - Alternativerock
  - ArtPop
rating:
---

# Dance Fever
**Artist:** Florence + the Machine
**Year:** 2022

![[_covers/Florence + the Machine - Dance Fever.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/228279663
```
^button-4wfl
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Florence%20%2B%20the%20Machine%20Dance%20Fever
```
^button-v0pc

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
| 1 | King | 4:40 |  |
| 2 | Free | 3:54 |  |
| 3 | Choreomania | 3:33 |  |
| 4 | Back in Town | 3:55 |  |
| 5 | Girls Against God | 4:40 |  |
| 6 | Dream Girl Evil | 3:47 |  |
| 7 | Prayer Factory | 1:13 |  |
| 8 | Cassandra | 4:17 |  |
| 9 | Heaven Is Here | 1:51 |  |
| 10 | Daffodil | 3:34 |  |
| 11 | My Love | 3:51 |  |
| 12 | Restraint | 0:47 |  |
| 13 | The Bomb | 2:44 |  |
| 14 | Morning Elvis | 4:22 |  |
