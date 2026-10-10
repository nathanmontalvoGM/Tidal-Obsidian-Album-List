---
title: "Shoelace & A Knot"
artist: "yungatita"
year: 2024
tidal_id: 327845874
tags:
  - Nmf240105
  - Indierock
  - Poprock
  - Rock
rating:
---

# Shoelace & A Knot
**Artist:** yungatita
**Year:** 2024

![[_covers/yungatita - Shoelace & A Knot.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/327845874
```
^button-hto0
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=yungatita%20Shoelace%20%26%20A%20Knot
```
^button-ukgn

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
| 1 | Poppy | 2:11 |  |
| 2 | Reckless | 3:35 |  |
| 3 | Other | 3:25 |  |
| 4 | Armchair | 4:55 |  |
| 5 | Descenda | 3:30 |  |
| 6 | 2 Cigs | 2:24 |  |
| 7 | Pick at Your Face | 4:29 |  |
| 8 | Crack of Your Jaw | 4:07 |  |
| 9 | Whiplash | 4:21 |  |
| 10 | Pack It Up | 2:50 |  |
