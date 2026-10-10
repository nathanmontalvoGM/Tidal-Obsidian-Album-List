---
title: "Selected Ambient Works 85-92"
artist: "Aphex Twin"
year: 1992
tidal_id: 59962969
tags:
  - Ambient
  - Electronicore
  - Idm
  - Chillout
rating:
---

# Selected Ambient Works 85-92
**Artist:** Aphex Twin
**Year:** 1992

![[_covers/Aphex Twin - Selected Ambient Works 85-92.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/59962969
```
^button-c0w2
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Aphex%20Twin%20Selected%20Ambient%20Works%2085-92
```
^button-8wv2

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
| 1 | Xtal | 4:54 |  |
| 2 | Tha | 9:07 |  |
| 3 | Pulsewidth | 3:48 |  |
| 4 | Ageispolis | 5:23 |  |
| 5 | i | 1:17 |  |
| 6 | Green Calx | 6:05 |  |
| 7 | Heliosphan | 4:53 |  |
| 8 | We are the music makers | 7:43 |  |
| 9 | Schottkey 7th Path | 5:08 |  |
| 10 | Ptolemy | 7:14 |  |
| 11 | Hedphelym | 6:03 |  |
| 12 | Delphium | 5:29 |  |
| 13 | Actium | 7:35 |  |
