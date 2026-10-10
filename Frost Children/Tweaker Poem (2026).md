---
title: "Tweaker Poem"
artist: "Frost Children"
year: 2026
tidal_id: 540650737
tags: []
rating:
---

# Tweaker Poem
**Artist:** Frost Children
**Year:** 2026

![[_covers/Frost Children - Tweaker Poem.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/540650737
```
^button-89fi
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Frost%20Children%20Tweaker%20Poem
```
^button-953u

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
| 1 | Satellites | 3:31 |  |
| 2 | Creep | 4:00 |  |
| 3 | Afterlife | 2:49 |  |
| 4 | Gutted | 3:26 |  |
| 5 | Light Leak | 3:35 |  |
| 6 | Faster | 3:36 |  |
