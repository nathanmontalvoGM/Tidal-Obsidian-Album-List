---
title: "viagr aboys"
artist: "Viagra Boys"
year: 2025
tidal_id: 428837316
tags:
  - Satire
  - Postpunk
  - Album
  - Artpunk
rating:
---

# viagr aboys
**Artist:** Viagra Boys
**Year:** 2025

![[_covers/Viagra Boys - viagr aboys.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/428837316
```
^button-1etm
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Viagra%20Boys%20viagr%20aboys
```
^button-7ma9

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
| 1 | Man Made of Meat | 3:09 |  |
| 2 | The Bog Body | 2:53 |  |
| 3 | Uno II | 2:15 |  |
| 4 | Pyramid of Health | 3:15 |  |
| 5 | Dirty Boyz | 3:44 |  |
| 6 | Medicine for Horses | 2:50 |  |
| 7 | Waterboy | 2:58 |  |
| 8 | Store Policy | 3:35 |  |
| 9 | You N33d Me | 3:53 |  |
| 10 | Best in Show pt. IV | 5:28 |  |
| 11 | River King | 3:16 |  |
