---
title: "The Forever Story"
artist: "JID"
year: 2022
tidal_id: 244862978
tags:
  - Hiphop
  - Neosoul
  - Southernhiphop
  - Rap
rating:
---

# The Forever Story
**Artist:** JID
**Year:** 2022

![[_covers/JID - The Forever Story.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/244862978
```
^button-l7lb
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=JID%20The%20Forever%20Story
```
^button-klg5

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
| 1 | Galaxy | 0:52 |  |
| 2 | Raydar | 3:24 |  |
| 3 | Dance Now | 3:47 |  |
| 4 | Crack Sandwich | 4:57 |  |
| 5 | Can’t Punk Me | 3:23 |  |
| 6 | Surround Sound | 3:49 |  |
| 7 | Kody Blu 31 | 3:44 |  |
| 8 | Bruddanem | 3:55 |  |
| 9 | Sistanem | 6:09 |  |
| 10 | Can’t Make U Change | 4:48 |  |
| 11 | Stars | 4:18 |  |
| 12 | Just in Time | 3:27 |  |
| 13 | Money | 4:26 |  |
| 14 | Better Days | 4:14 |  |
| 15 | Lauder Too | 3:53 |  |
