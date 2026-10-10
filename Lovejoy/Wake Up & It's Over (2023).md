---
title: "Wake Up & It's Over"
artist: "Lovejoy"
year: 2023
tidal_id: 286975796
tags:
  - Alternativerock
  - Indierock
  - Postbritpop
rating:
---

# Wake Up & It's Over
**Artist:** Lovejoy
**Year:** 2023

![[_covers/Lovejoy - Wake Up & It's Over.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/286975796
```
^button-k11z
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Lovejoy%20Wake%20Up%20%26%20It%27s%20Over
```
^button-kiuv

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
| 1 | Portrait of a Blank Slate | 3:47 |  |
| 2 | Call Me What You Like | 3:47 |  |
| 3 | Consequences | 3:10 |  |
| 4 | Warsaw | 3:30 |  |
| 5 | Scum | 3:52 |  |
| 6 | It’s Golden Hour Somewhere | 3:24 |  |
