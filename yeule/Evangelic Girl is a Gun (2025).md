---
title: "Evangelic Girl is a Gun"
artist: "yeule"
year: 2025
tidal_id: 421590283
tags:
  - Alternativerock
  - Electronicore
  - Indierock
  - Indietronica
rating:
---

# Evangelic Girl is a Gun
**Artist:** yeule
**Year:** 2025

![[_covers/yeule - Evangelic Girl is a Gun.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/421590283
```
^button-uaik
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=yeule%20Evangelic%20Girl%20is%20a%20Gun
```
^button-6u80

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
| 1 | Evangelic Girl Is a Gun | 3:03 |  |
| 2 | Skullcrusher | 2:07 |  |
| 3 | Eko | 3:43 |  |
