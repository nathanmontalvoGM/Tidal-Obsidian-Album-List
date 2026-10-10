---
title: "Ascension"
artist: "Mirar"
year: 2025
tidal_id: 409492040
tags:
  - Mathmetal
  - Neoclassicaldjent
  - Experimentalmetal
  - Thall
rating:
---

# Ascension
**Artist:** Mirar
**Year:** 2025

![[_covers/Mirar - Ascension.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/409492040
```
^button-cgnh
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Mirar%20Ascension
```
^button-oedf

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
| 1 | Couronne | 2:10 |  |
| 2 | Tombe | 4:22 |  |
| 3 | Mauvais Œil | 2:50 |  |
| 4 | Charnier | 3:34 |  |
| 5 | Faux‐Amis | 5:15 |  |
| 6 | Présage | 3:27 |  |
| 7 | Épreuve | 4:58 |  |
| 8 | Sur Ses Épaules | 4:22 |  |
| 9 | Failles | 3:18 |  |
| 10 | Défiance | 4:40 |  |
| 11 | Confiance | 3:10 |  |
| 12 | Ma Pierre | 3:13 |  |
| 13 | Saint Matthieu | 3:50 |  |
