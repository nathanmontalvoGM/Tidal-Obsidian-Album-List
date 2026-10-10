---
title: "Diorama"
artist: "MØL"
year: 2021
tidal_id: 188752811
tags:
  - Bestof2022
  - Blackgaze
  - Topmetalalbumsofthedecade20202029
  - Blackmetal
rating:
---

# Diorama
**Artist:** MØL
**Year:** 2021

![[_covers/MØL - Diorama.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/188752811
```
^button-0gzu
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=M%C3%98L%20Diorama
```
^button-eevz

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
| 1 | Fraktur | 4:19 |  |
| 2 | Photophobic | 5:18 |  |
| 3 | Serf | 5:22 |  |
| 4 | Vestige | 5:38 |  |
| 5 | Redacted | 5:16 |  |
| 6 | Itinerari | 5:03 |  |
| 7 | Tvesind | 7:48 |  |
| 8 | Diorama | 7:14 |  |
