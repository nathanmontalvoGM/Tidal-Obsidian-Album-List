---
title: "Parasocial"
artist: "Arythmia"
year: 2025
tidal_id: 424879354
tags: []
rating:
---

# Parasocial
**Artist:** Arythmia
**Year:** 2025

![[_covers/Arythmia - Parasocial.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/424879354
```
^button-9aih
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Arythmia%20Parasocial
```
^button-0jrt

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
| 1 | Waking Up from a Dream | 1:46 |  |
| 2 | Consolation Prize | 1:55 |  |
| 3 | The Cost of Living | 3:20 |  |
| 4 | Brill | 2:37 |  |
| 5 | Silver Lining | 2:41 |  |
| 6 | On Second Thought | 1:55 |  |
| 7 | Mirrors | 3:19 |  |
| 8 | Embrace | 2:05 |  |
| 9 | Bygone Era | 3:04 |  |
| 10 | I'll Be Happy Then | 3:50 |  |
| 11 | Falling Back Asleep | 2:40 |  |
