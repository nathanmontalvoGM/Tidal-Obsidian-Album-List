---
title: "DIRTY BLONDE"
artist: "Bebe Rexha"
year: 2026
tidal_id: 530753897
tags:
  - Dancepop
  - Electropop
rating:
---

# DIRTY BLONDE
**Artist:** Bebe Rexha
**Year:** 2026

![[_covers/Bebe Rexha - DIRTY BLONDE.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/530753897
```
^button-v9l7
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Bebe%20Rexha%20DIRTY%20BLONDE
```
^button-yn8o

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
| 1 | Hysteria | 2:23 |  |
| 2 | Tokyo | 2:00 |  |
| 3 | New Religion | 2:54 |  |
| 4 | $.H.I.T | 2:07 |  |
| 5 | Çike Çike | 2:19 |  |
| 6 | i like you better than me | 2:38 |  |
| 7 | Drink and a Little Love | 2:41 |  |
| 8 | One Day | 3:08 |  |
| 9 | Time | 2:48 |  |
| 10 | The Way I Want You | 2:30 |  |
| 11 | Nobody’s There | 2:00 |  |
| 12 | Nightfalls | 3:24 |  |
| 13 | Sad Girls | 2:49 |  |
