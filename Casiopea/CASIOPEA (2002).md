---
title: "CASIOPEA"
artist: "Casiopea"
year: 2002
tidal_id: 157658550
tags:
  - JazzFusion
  - Jazz
  - Japanese
  - Instrumental
rating:
---

# CASIOPEA
**Artist:** Casiopea
**Year:** 2002

![[_covers/Casiopea - CASIOPEA.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/157658550
```
^button-9zcn
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Casiopea%20CASIOPEA
```
^button-y4cr

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
| 1 | Time Limit | 3:07 |  |
| 2 | Tears of the Star | 4:32 |  |
| 3 | Space Road | 5:14 |  |
| 4 | Midnight Rendezvous | 5:23 |  |
| 5 | Far Away | 3:57 |  |
| 6 | Swallow | 4:26 |  |
| 7 | Dream Hill | 5:39 |  |
| 8 | Black Joke | 4:16 |  |
