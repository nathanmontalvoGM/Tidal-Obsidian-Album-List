---
title: "A Head Full of Moonlight"
artist: "Good Tiger"
year: 2016
tidal_id: 52651192
tags:
  - Progressivemetal
  - Progressivepop
  - Posthardcore
  - Mathrock
rating:
---

# A Head Full of Moonlight
**Artist:** Good Tiger
**Year:** 2016

![[_covers/Good Tiger - A Head Full of Moonlight.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/52651192
```
^button-bic9
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Good%20Tiger%20A%20Head%20Full%20of%20Moonlight
```
^button-s82e

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
| 1 | Where Are the Birds | 3:31 |  |
| 2 | Snake Oil | 3:39 |  |
| 3 | Enjoy the Rain | 3:41 |  |
| 4 | I Paint What I See | 3:42 |  |
| 5 | Aspirations | 3:35 |  |
| 6 | Latchkey Kids | 4:24 |  |
| 7 | All Her Own Teeth | 4:05 |  |
| 8 | Understanding Silence | 3:26 |  |
| 9 | ’67 Pontiac Firebird | 4:52 |  |
