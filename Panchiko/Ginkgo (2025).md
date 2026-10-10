---
title: "Ginkgo"
artist: "Panchiko"
year: 2025
tidal_id: 392563567
tags:
  - Indierock
  - Rock
  - Indie
  - Poprock
rating:
---

# Ginkgo
**Artist:** Panchiko
**Year:** 2025

![[_covers/Panchiko - Ginkgo.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/392563567
```
^button-p0ae
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Panchiko%20Ginkgo
```
^button-ozbn

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
| 1 | Florida | 4:11 |  |
| 2 | Ginkgo | 2:37 |  |
| 3 | Shandy in the Graveyard | 2:57 |  |
| 4 | Honeycomb | 3:14 |  |
| 5 | Shelled and Cooked | 2:13 |  |
| 6 | Lifestyle Trainers | 3:07 |  |
| 7 | Chapel of Salt | 3:08 |  |
| 8 | Vinegar | 2:15 |  |
| 9 | Mac’s Omelette | 3:58 |  |
| 10 | Subtitles | 2:47 |  |
| 11 | Formula | 2:43 |  |
| 12 | Rise and Fall | 3:19 |  |
| 13 | Innocent | 2:44 |  |
