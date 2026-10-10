---
title: "That! Feels Good!"
artist: "Jessie Ware"
year: 2023
tidal_id: 290581948
tags:
  - Disco
  - Pop
  - Dancepop
  - Alternativedance
rating:
---

# That! Feels Good!
**Artist:** Jessie Ware
**Year:** 2023

![[_covers/Jessie Ware - That! Feels Good!.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/290581948
```
^button-i4rb
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Jessie%20Ware%20That%21%20Feels%20Good%21
```
^button-xwvu

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
| 1 | That! Feels Good! | 4:22 |  |
| 2 | Free Yourself | 3:54 |  |
| 3 | Pearls | 4:03 |  |
| 4 | Hello Love | 4:42 |  |
| 5 | Begin Again | 5:24 |  |
| 6 | Beautiful People | 3:35 |  |
| 7 | Freak Me Now | 3:28 |  |
| 8 | Shake the Bottle | 3:23 |  |
| 9 | Lightning | 3:10 |  |
| 10 | These Lips | 4:21 |  |
