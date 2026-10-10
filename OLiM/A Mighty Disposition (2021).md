---
title: "A Mighty Disposition"
artist: "OLiM"
year: 2021
tidal_id: 202748659
tags: []
rating:
---

# A Mighty Disposition
**Artist:** OLiM
**Year:** 2021

![[_covers/OLiM - A Mighty Disposition.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/202748659
```
^button-bnpl
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=OLiM%20A%20Mighty%20Disposition
```
^button-7zoo

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
| 1 | The Ethereal Whim Bent Toward a Light | 6:55 |  |
| 2 | Canvas of the Void Dotted with Vast Quantity | 8:11 |  |
| 3 | Presence Beyond Words | 7:37 |  |
| 4 | Nearing an Infinite Height for the Familiar | 6:14 |  |
| 5 | Remember | 5:05 |  |
