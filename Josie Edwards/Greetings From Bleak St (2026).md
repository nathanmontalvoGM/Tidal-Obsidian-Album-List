---
title: "Greetings From Bleak St."
artist: "Josie Edwards"
year: 2026
tidal_id: 534393992
tags: []
rating:
---

# Greetings From Bleak St.
**Artist:** Josie Edwards
**Year:** 2026

![[_covers/Josie Edwards - Greetings From Bleak St.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/534393992
```
^button-dlsi
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Josie%20Edwards%20Greetings%20From%20Bleak%20St.
```
^button-gpb0

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
| 1 | Gravedigger | 2:46 |  |
| 2 | Burgundy Place | 2:51 |  |
| 3 | The Poet and Her Vice (Happy Ending) | 2:54 |  |
| 4 | Hide Away | 2:53 |  |
| 5 | Dog Prophecies | 3:45 |  |
| 6 | Chemical Light | 3:46 |  |
