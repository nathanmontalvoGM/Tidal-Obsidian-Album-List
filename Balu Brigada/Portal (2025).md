---
title: "Portal"
artist: "Balu Brigada"
year: 2025
tidal_id: 439745413
tags:
  - Indiepop
  - Indierock
  - Alternativedance
  - Altpop
rating:
---

# Portal
**Artist:** Balu Brigada
**Year:** 2025

![[_covers/Balu Brigada - Portal.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/439745413
```
^button-q9r9
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Balu%20Brigada%20Portal
```
^button-tv14

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
| 1 | The Portal | 1:00 |  |
| 2 | So Cold | 3:21 |  |
| 3 | Golden Gate Girl | 3:17 |  |
| 4 | Sideways | 3:07 |  |
| 5 | Birthday Interlude | 1:17 |  |
| 6 | Backseat | 6:23 |  |
| 7 | Politix | 4:32 |  |
| 8 | The Question | 3:16 |  |
| 9 | 4:25 | 4:37 |  |
| 10 | Isolation | 4:01 |  |
| 11 | What Do We Ever Really Know? | 3:53 |  |
| 12 | Butterfly Boy | 5:02 |  |
