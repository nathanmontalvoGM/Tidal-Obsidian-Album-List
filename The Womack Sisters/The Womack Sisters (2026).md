---
title: "The Womack Sisters"
artist: "The Womack Sisters"
year: 2026
tidal_id: 515388445
tags: []
rating:
---

# The Womack Sisters
**Artist:** The Womack Sisters
**Year:** 2026

![[_covers/The Womack Sisters - The Womack Sisters.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/515388445
```
^button-nqba
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=The%20Womack%20Sisters%20The%20Womack%20Sisters
```
^button-5bbl

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
| 1 | Chauffeur | 4:36 |  |
| 2 | If You Want Me | 3:06 |  |
| 3 | Monster | 3:39 |  |
| 4 | If I Let You | 3:58 |  |
| 5 | I Just Don’t Want You (To Say Goodbye) | 3:30 |  |
| 6 | Laugher and Tears | 2:08 |  |
| 7 | Didn’t Mean Much to Me | 3:27 |  |
| 8 | You Went Away Too Long | 3:20 |  |
| 9 | I Am Your Season | 3:50 |  |
| 10 | All Around | 3:35 |  |
| 11 | My Sisters and Me | 2:11 |  |
