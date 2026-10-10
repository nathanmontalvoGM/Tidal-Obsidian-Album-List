---
title: "Nu Delhi"
artist: "Bloodywood"
year: 2025
tidal_id: 423887661
tags:
  - FolkMetal
  - Numetal
  - Groovemetal
  - Indian
rating:
---

# Nu Delhi
**Artist:** Bloodywood
**Year:** 2025

![[_covers/Bloodywood - Nu Delhi.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/423887661
```
^button-kvxy
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Bloodywood%20Nu%20Delhi
```
^button-bhhg

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
| 1 | Nu Delhi | 4:28 |  |
