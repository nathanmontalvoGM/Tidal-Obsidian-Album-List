---
title: "After Laughter"
artist: "Paramore"
year: 2017
tidal_id: 73856849
tags:
  - Newwave
  - Poprock
  - Synthpop
  - Pop
rating:
---

# After Laughter
**Artist:** Paramore
**Year:** 2017

![[_covers/Paramore - After Laughter.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/73856849
```
^button-ea2s
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Paramore%20After%20Laughter
```
^button-h8op

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
| 1 | Hard Times | 3:03 |  |
| 2 | Rose‐Colored Boy | 3:33 |  |
| 3 | Told You So | 3:09 |  |
| 4 | Forgiveness | 3:40 |  |
| 5 | Fake Happy | 3:56 |  |
| 6 | 26 | 3:42 |  |
| 7 | Pool | 3:53 |  |
| 8 | Grudges | 3:07 |  |
| 9 | Caught in the Middle | 3:34 |  |
| 10 | Idle Worship | 3:18 |  |
| 11 | No Friend | 3:24 |  |
| 12 | Tell Me How | 4:20 |  |
