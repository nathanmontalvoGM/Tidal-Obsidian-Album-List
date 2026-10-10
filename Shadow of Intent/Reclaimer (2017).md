---
title: "Reclaimer"
artist: "Shadow of Intent"
year: 2017
tidal_id: 71823180
tags:
  - MelodicDeathGroove
  - Technicaldeathcore
  - Symphonicdeathcore
  - Deathcore
rating:
---

# Reclaimer
**Artist:** Shadow of Intent
**Year:** 2017

![[_covers/Shadow of Intent - Reclaimer.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/71823180
```
^button-y7iq
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Shadow%20of%20Intent%20Reclaimer
```
^button-zvmv

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
| 1 | We Descend… | 2:14 |  |
| 2 | The Return | 4:45 |  |
| 3 | The Horror Within | 6:10 |  |
| 4 | The Catacombs | 4:43 |  |
| 5 | The Mad Tyrant’s Betrayal | 5:14 |  |
| 6 | The Gathering of All | 4:20 |  |
| 7 | The Heretic Prevails | 4:48 |  |
| 8 | The Prophet’s Beckoning | 5:04 |  |
| 9 | The Forsaken Effigy | 4:04 |  |
| 10 | The Great Schism | 4:21 |  |
| 11 | The Mausoleum of Liars | 4:49 |  |
| 12 | The Tartarus Impalement | 7:52 |  |
