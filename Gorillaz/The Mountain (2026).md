---
title: "The Mountain"
artist: "Gorillaz"
year: 2026
tidal_id: 500753046
tags:
  - Synthpop
  - ArtPop
  - Psychedelicpop
  - Hiphop
rating:
---

# The Mountain
**Artist:** Gorillaz
**Year:** 2026

![[_covers/Gorillaz - The Mountain.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/500753046
```
^button-oamr
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Gorillaz%20The%20Mountain
```
^button-uw70

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
| 1 | The Mountain | 4:50 |  |
| 2 | The Moon Cave | 4:57 |  |
| 3 | The Happy Dictator | 4:44 |  |
| 4 | The Hardest Thing | 2:18 |  |
| 5 | Orange County | 3:28 |  |
| 6 | The God of Lying | 3:09 |  |
| 7 | The Empty Dream Machine | 5:40 |  |
| 8 | The Manifesto | 7:19 |  |
| 9 | The Plastic Guru | 3:14 |  |
| 10 | Delirium | 3:52 |  |
| 11 | Damascus | 4:04 |  |
| 12 | The Shadowy Light | 5:39 |  |
| 13 | Casablanca | 3:46 |  |
| 14 | The Sweet Prince | 4:33 |  |
| 15 | The Sad God | 4:49 |  |
