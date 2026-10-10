---
title: "Epicus Doomicus Metallicus"
artist: "Candlemass"
year: 1986
tidal_id: 68660554
tags:
  - Doommetal
  - TraditionalDoomMetal
  - EpicDoomMetal
  - Heavymetal
rating:
---

# Epicus Doomicus Metallicus
**Artist:** Candlemass
**Year:** 1986

![[_covers/Candlemass - Epicus Doomicus Metallicus.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/68660554
```
^button-syny
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Candlemass%20Epicus%20Doomicus%20Metallicus
```
^button-9wwp

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
| 1-1 | Solitude | 5:37 |  |
| 1-2 | Demons Gate | 9:12 |  |
| 1-3 | Crystal Ball | 5:22 |  |
| 1-4 | Black Stone Wielder | 7:36 |  |
| 1-5 | Under the Oak | 6:54 |  |
| 1-6 | A Sorcerer's Pledge | 8:12 |  |
| 2-1 | Epicus Doomicus Metallicus with commentary by Leif Edling | 42:56 |  |
