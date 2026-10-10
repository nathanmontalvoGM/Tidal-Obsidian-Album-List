---
title: "Heavener"
artist: "Invent Animate"
year: 2023
tidal_id: 379605132
tags:
  - Metalcore
rating:
---

# Heavener
**Artist:** Invent Animate
**Year:** 2023

![[_covers/Invent Animate - Heavener.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/379605132
```
^button-clb6
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Invent%20Animate%20Heavener
```
^button-oyzk

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
| 1 | Absence Persistent | 3:49 |  |
| 2 | Shade Astray | 4:35 |  |
| 3 | Labyrinthine | 3:43 |  |
| 4 | Without a Whisper | 4:17 |  |
| 5 | False Meridian | 5:00 |  |
| 6 | Reverie | 3:10 |  |
| 7 | Immolation of Night | 3:50 |  |
| 8 | Purity Weeps | 4:08 |  |
| 9 | Void Surfacing | 4:30 |  |
| 10 | Emberglow | 4:21 |  |
| 11 | Elysium | 4:48 |  |
