---
title: "Modern Vampires of the City"
artist: "Vampire Weekend"
year: 2013
tidal_id: 20134593
tags:
  - Indie
  - Indierock
  - Indiepop
  - 10s
rating:
---

# Modern Vampires of the City
**Artist:** Vampire Weekend
**Year:** 2013

![[_covers/Vampire Weekend - Modern Vampires of the City.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/20134593
```
^button-zzl9
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Vampire%20Weekend%20Modern%20Vampires%20of%20the%20City
```
^button-6dq9

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
| 1 | Obvious Bicycle | 4:11 |  |
| 2 | Unbelievers | 3:22 |  |
| 3 | Step | 4:11 |  |
| 4 | Diane Young | 2:40 |  |
| 5 | Don’t Lie | 3:33 |  |
| 6 | Hannah Hunt | 3:57 |  |
| 7 | Everlasting Arms | 3:03 |  |
| 8 | Finger Back | 3:25 |  |
| 9 | Worship You | 3:21 |  |
| 10 | Ya Hey | 5:12 |  |
| 11 | Hudson | 4:14 |  |
| 12 | Young Lion | 1:45 |  |
