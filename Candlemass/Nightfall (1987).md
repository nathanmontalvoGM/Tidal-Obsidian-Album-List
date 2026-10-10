---
title: "Nightfall"
artist: "Candlemass"
year: 1987
tidal_id: 2596368
tags:
  - Doommetal
  - TraditionalDoomMetal
  - EpicDoomMetal
  - Heavymetal
rating:
---

# Nightfall
**Artist:** Candlemass
**Year:** 1987

![[_covers/Candlemass - Nightfall.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/2596368
```
^button-pknp
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Candlemass%20Nightfall
```
^button-04n2

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
| 1 | Gothic Stone | 0:48 |  |
| 2 | The Well of Souls | 7:27 |  |
| 3 | Codex Gigas | 2:20 |  |
| 4 | At the Gallows End | 5:48 |  |
| 5 | Samarithan | 5:31 |  |
| 6 | Marche Funebre | 2:22 |  |
| 7 | Dark Are the Veils of Death | 7:08 |  |
| 8 | Mourners Lament | 6:10 |  |
| 9 | Bewitched | 6:38 |  |
| 10 | Black Candles | 2:18 |  |
