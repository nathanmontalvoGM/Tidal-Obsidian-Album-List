---
title: "HYPERYOUTH"
artist: "Joey Valence & Brae"
year: 2025
tidal_id: 453448229
tags:
  - Hiphop
  - Hardcorehiphop
  - Eastcoasthiphop
  - Aoty
rating:
---

# HYPERYOUTH
**Artist:** Joey Valence & Brae
**Year:** 2025

![[_covers/Joey Valence & Brae - HYPERYOUTH.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/453448229
```
^button-d72f
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Joey%20Valence%20%26%20Brae%20HYPERYOUTH
```
^button-y8w9

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
| 1 | HYPERYOUTH | 2:47 |  |
| 2 | LIVE RIGHT | 3:39 |  |
| 3 | WASSUP | 3:00 |  |
