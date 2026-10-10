---
title: "Halfway to the Place Behind the Stars"
artist: "Streetlight Manifesto"
year: 2026
tidal_id: 535896308
tags: []
rating:
---

# Halfway to the Place Behind the Stars
**Artist:** Streetlight Manifesto
**Year:** 2026

![[_covers/Streetlight Manifesto - Halfway to the Place Behind the Stars.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/535896308
```
^button-28sx
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Streetlight%20Manifesto%20Halfway%20to%20the%20Place%20Behind%20the%20Stars
```
^button-ldi7

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
| 1 | Oooo (halfway version) | 1:36 |  |
| 2 | Enormous (halfway version) | 7:18 |  |
| 3 | Everything to Everyone (halfway version) | 6:30 |  |
| 4 | All the Pieces (halfway version) | 8:03 |  |
| 5 | Imagine This (halfway version) | 6:08 |  |
| 6 | How Do You Sleep at Night? (halfway version) | 5:13 |  |
