---
title: "Zerfall"
artist: "Ellende"
year: 2026
tidal_id: 470233168
tags:
  - Impossibleforliberalstodealwith
  - Blackmetal
  - Atmosphericmetal
  - Numetal
rating:
---

# Zerfall
**Artist:** Ellende
**Year:** 2026

![[_covers/Ellende - Zerfall.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/470233168
```
^button-9wt7
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Ellende%20Zerfall
```
^button-vttg

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
| 1 | Nur | 2:34 |  |
| 2 | Wahrheit Teil I | 7:03 |  |
| 3 | Wahrheit Teil II | 5:49 |  |
| 4 | Zerfall | 7:18 |  |
| 5 | Übertritt | 6:02 |  |
| 6 | Ode ans Licht | 4:23 |  |
| 7 | Zeitenwende Teil I | 6:36 |  |
| 8 | Zeitenwende Teil II | 5:01 |  |
| 9 | Reise | 7:09 |  |
