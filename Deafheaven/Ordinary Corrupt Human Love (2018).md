---
title: "Ordinary Corrupt Human Love"
artist: "Deafheaven"
year: 2018
tidal_id: 121048638
tags:
  - Postmetal
  - Blackgaze
  - Postrock
  - Shoegaze
rating:
---

# Ordinary Corrupt Human Love
**Artist:** Deafheaven
**Year:** 2018

![[_covers/Deafheaven - Ordinary Corrupt Human Love.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/121048638
```
^button-lk0b
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Deafheaven%20Ordinary%20Corrupt%20Human%20Love
```
^button-tyvl

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
| 1 | You Without End | 7:36 |  |
| 2 | Honeycomb | 11:04 |  |
| 3 | Canary Yellow | 12:17 |  |
| 4 | Near | 5:28 |  |
| 5 | Glint | 10:57 |  |
| 6 | Night People | 4:07 |  |
| 7 | Worthless Animal | 10:07 |  |
