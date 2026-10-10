---
title: "Disquiet"
artist: "Unreqvited"
year: 2020
tidal_id: 175551878
tags:
  - Blackgaze
  - Ambient
  - Blackmetal
  - Shoegaze
rating:
---

# Disquiet
**Artist:** Unreqvited
**Year:** 2020

![[_covers/Unreqvited - Disquiet.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/175551878
```
^button-lfq8
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Unreqvited%20Disquiet
```
^button-vcw7

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
| 1 | Birth | 2:45 |  |
| 2 | The Autumn Fire | 7:08 |  |
| 3 | Disquiet | 9:22 |  |
| 4 | A Tear From the Oak | 3:00 |  |
| 5 | An Ocean of Ire | 2:58 |  |
| 6 | Maydena | 7:36 |  |
| 7 | Death | 9:00 |  |
