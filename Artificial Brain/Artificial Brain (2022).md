---
title: "Artificial Brain"
artist: "Artificial Brain"
year: 2022
tidal_id: 221024063
tags:
  - Dissonantdeathmetal
  - Technicaldeathmetal
  - Profoundlore
  - Blackmetal
rating:
---

# Artificial Brain
**Artist:** Artificial Brain
**Year:** 2022

![[_covers/Artificial Brain - Artificial Brain.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/221024063
```
^button-d445
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Artificial%20Brain%20Artificial%20Brain
```
^button-1e9x

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
| 1 | Artificial Brain | 2:38 |  |
| 2 | Glitch Cannon | 3:38 |  |
| 3 | Celestial Cyst | 4:30 |  |
| 4 | A Lofty Grave | 4:37 |  |
| 5 | Tome of the Exiled Engineer | 4:32 |  |
| 6 | Embalmed With Magma | 5:35 |  |
| 7 | Parasite Signal | 3:05 |  |
| 8 | Cryogenic Dreamworld | 5:45 |  |
| 9 | Insects and Android Eyes | 4:55 |  |
| 10 | Last Words of the Wobbling Sun | 6:08 |  |
