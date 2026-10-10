---
title: Odyssey Of Respair
artist: Netherwalker
year: 2025
tidal_id: 515551845
tags:
  - Deathcore
  - Symphonicmetal
rating:
---

# Odyssey Of Respair
**Artist:** Netherwalker
**Year:** 2025

![[_covers/Netherwalker - Odyssey Of Respair.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/515551845
```
^button-96jm
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Netherwalker%20Odyssey%20Of%20Respair
```
^button-xtet

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
| 1 | Prologue | 1:44 |  |
| 2 | Thine King Weeps for Mercy | 2:45 |  |
| 3 | Battle of Tredem | 4:09 |  |
| 4 | An Opulent Pillaging of the Treacherous Goblin Encampment | 3:29 |  |
| 5 | Sea of Sirens | 5:06 |  |
| 6 | Eyes of Obscura | 1:18 |  |
| 7 | Servant to Instinct | 4:17 |  |
| 8 | Tavern | 4:06 |  |
| 9 | Frost Troll | 3:54 |  |
| 10 | Destiny Will Decide | 1:38 |  |
| 11 | Crystal Knight | 5:53 |  |
| 12 | The Elden Stav | 3:08 |  |
| 13 | For Princess Elizabeth, We Fly! | 7:16 |  |
| 14 | Army of Darkness | 7:52 |  |
