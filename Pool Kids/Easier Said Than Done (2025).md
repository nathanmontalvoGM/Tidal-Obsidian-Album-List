---
title: Easier Said Than Done
artist: Pool Kids
year: 2025
tidal_id: 434857405
tags:
  - Emopop
  - DreamPop
  - Midwestemo
rating:
---

# Easier Said Than Done
**Artist:** Pool Kids
**Year:** 2025

![[_covers/Pool Kids - Easier Said Than Done.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/434857405
```
^button-6642
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Pool%20Kids%20Easier%20Said%20Than%20Done
```
^button-wr41

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
| 1 | Easier Said Than Done | 3:05 |  |
