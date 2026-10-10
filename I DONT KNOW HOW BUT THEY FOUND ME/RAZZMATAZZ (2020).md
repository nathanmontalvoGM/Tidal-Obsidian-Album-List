---
title: "RAZZMATAZZ"
artist: "I DONT KNOW HOW BUT THEY FOUND ME"
year: 2020
tidal_id: 158720756
tags:
  - Newwave
  - Indietronica
  - Indierock
  - Synthpop
rating:
---

# RAZZMATAZZ
**Artist:** I DONT KNOW HOW BUT THEY FOUND ME
**Year:** 2020

![[_covers/I DONT KNOW HOW BUT THEY FOUND ME - RAZZMATAZZ.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/158720756
```
^button-oel6
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=I%20DONT%20KNOW%20HOW%20BUT%20THEY%20FOUND%20ME%20RAZZMATAZZ
```
^button-edfw

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
| 1 | Leave Me Alone | 3:35 |  |
| 2 | Mad IQs | 3:02 |  |
| 3 | Nobody Likes the Opening Band | 2:15 |  |
| 4 | New Invention | 3:11 |  |
| 5 | From the Gallows | 2:42 |  |
| 6 | Clusterhug | 3:12 |  |
| 7 | Sugar Pills | 3:07 |  |
| 8 | Kiss Goodnight | 3:50 |  |
| 9 | Lights Go Down | 3:24 |  |
| 10 | Need You Here | 3:07 |  |
| 11 | Door | 1:32 |  |
| 12 | Razzmatazz | 4:18 |  |
