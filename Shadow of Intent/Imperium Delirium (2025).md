---
title: "Imperium Delirium"
artist: "Shadow of Intent"
year: 2025
tidal_id: 429326462
tags:
  - Bestalbums2025
  - Symphonicdeathcore
  - Vocalsbybenduerr
  - Deathcore
rating:
---

# Imperium Delirium
**Artist:** Shadow of Intent
**Year:** 2025

![[_covers/Shadow of Intent - Imperium Delirium.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/429326462
```
^button-twt5
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Shadow%20of%20Intent%20Imperium%20Delirium
```
^button-gtt6

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
| 1 | Prepare to Die | 4:01 |  |
| 2 | Flying the Black Flag | 3:57 |  |
| 3 | Infinity of Horrors | 4:14 |  |
| 4 | Mechanical Chaos | 3:50 |  |
| 5 | They Murdered Sleep | 4:01 |  |
| 6 | The Facets of Propaganda | 5:19 |  |
| 7 | Feeding the Meatgrinder | 4:03 |  |
| 8 | Vehement Draconian Vengeance | 3:55 |  |
| 9 | Beholding the Sickness of Civilization | 4:30 |  |
| 10 | Apocalypse Canvas | 4:49 |  |
| 11 | No Matter the Cost | 4:16 |  |
| 12 | Imperium Delirium | 7:34 |  |
