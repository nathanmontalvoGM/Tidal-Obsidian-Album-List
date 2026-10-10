---
title: "Picnic at the Cemetery"
artist: "Bella Poarch"
year: 2026
tidal_id: 559463211
tags: []
rating:
---

# Picnic at the Cemetery
**Artist:** Bella Poarch
**Year:** 2026

![[_covers/Bella Poarch - Picnic at the Cemetery.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/559463211
```
^button-xrh4
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Bella%20Poarch%20Picnic%20at%20the%20Cemetery
```
^button-afte

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
| 1 | Hideaway | 2:19 |  |
| 2 | Ribcage | 3:00 |  |
| 3 | My Boy | 2:30 |  |
| 4 | Stay Gone | 4:27 |  |
| 5 | Bighead | 2:40 |  |
| 6 | Loverghost | 3:05 |  |
| 7 | Down | 2:21 |  |
| 8 | Chase Me | 2:40 |  |
| 9 | Nice To Meet Ya | 3:05 |  |
| 10 | My Heaven Is Alone | 2:49 |  |
| 11 | Pomegranate | 2:50 |  |
| 12 | Garden | 2:51 |  |
