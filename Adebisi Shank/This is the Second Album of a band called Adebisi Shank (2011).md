---
title: "This is the Second Album of a band called Adebisi Shank"
artist: "Adebisi Shank"
year: 2011
tidal_id: 430139090
tags:
  - Mathrock
  - Experimentalrock
  - Bestof2019
  - Titleisafullsentence
rating:
---

# This is the Second Album of a band called Adebisi Shank
**Artist:** Adebisi Shank
**Year:** 2011

![[_covers/Adebisi Shank - This is the Second Album of a band called Adebisi Shank.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/430139090
```
^button-oi4f
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Adebisi%20Shank%20This%20is%20the%20Second%20Album%20of%20a%20band%20called%20Adebisi%20Shank
```
^button-mpou

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
| 1 | International Dreambeat | 3:50 |  |
| 2 | Masa | 3:45 |  |
| 3 | Genki Shank | 4:47 |  |
| 4 | Micromachines | 3:36 |  |
| 5 | (-_-) | 2:03 |  |
| 6 | Logdrum | 6:04 |  |
| 7 | Bones | 2:52 |  |
| 8 | Frunk | 3:06 |  |
| 9 | Europa | 3:57 |  |
| 10 | Century City | 5:05 |  |
