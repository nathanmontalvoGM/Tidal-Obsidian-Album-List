---
title: "Frailty"
artist: "Jane Remover"
year: 2021
tidal_id: 202237410
tags:
  - Indietronica
  - NoisePop
  - Emopop
  - Glitchpop
rating:
---

# Frailty
**Artist:** Jane Remover
**Year:** 2021

![[_covers/Jane Remover - Frailty.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/202237410
```
^button-ptvq
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Jane%20Remover%20Frailty
```
^button-j1dp

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
| 1-1 | goldfish | 3:01 |  |
| 1-2 | your clothes | 4:14 |  |
| 1-3 | misplace | 3:53 |  |
| 1-4 | pretender | 3:41 |  |
| 1-5 | search party | 4:58 |  |
| 1-6 | buzzcut, daisy | 2:30 |  |
| 1-7 | movies for guys | 5:45 |  |
| 1-8 | kodak moment | 6:07 |  |
| 2-1 | can you tell? | 3:28 |  |
| 2-2 | how to lie | 3:45 |  |
| 2-3 | champ | 6:16 |  |
| 2-4 | eyes off the wheel, i’m a star | 3:53 |  |
| 2-5 | let’s go home | 5:32 |  |
| 2-6 | can you tell? (live version) | 3:15 |  |
| 2-7 | might be crazy | 3:24 |  |
