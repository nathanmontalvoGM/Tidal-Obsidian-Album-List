---
title: "Sunbather"
artist: "Deafheaven"
year: 2013
tidal_id: 20749616
tags:
  - Blackmetal
  - Postrock
  - Shoegaze
  - Blackgaze
rating:
---

# Sunbather
**Artist:** Deafheaven
**Year:** 2013

![[_covers/Deafheaven - Sunbather.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/20749616
```
^button-gj41
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Deafheaven%20Sunbather
```
^button-qc71

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
| 1 | Dream House | 9:14 |  |
| 2 | Irresistible | 3:13 |  |
| 3 | Sunbather | 10:16 |  |
| 4 | Please Remember | 6:26 |  |
| 5 | Vertigo | 14:37 |  |
| 6 | Windows | 4:42 |  |
| 7 | The Pecan Tree | 11:26 |  |
