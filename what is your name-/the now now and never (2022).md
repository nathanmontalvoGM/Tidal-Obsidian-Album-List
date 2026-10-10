---
title: "the now now and never"
artist: "what is your name?"
year: 2022
tidal_id: 238851423
tags:
  - Postrock
  - Shoegaze
  - Rock
  - Indietronica
rating:
---

# the now now and never
**Artist:** what is your name?
**Year:** 2022

![[_covers/what is your name- - the now now and never.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/238851423
```
^button-uml8
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=what%20is%20your%20name%3F%20the%20now%20now%20and%20never
```
^button-8rug

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
| 1 | the now now and never | 9:13 |  |
| 2 | 3, 2, 1.. | 0:20 |  |
| 3 | heartache st. | 4:48 |  |
| 4 | youthful days | 9:22 |  |
| 5 | you can’t turn back time | 7:32 |  |
| 6 | saturday | 2:27 |  |
| 7 | that unrequited feeling | 6:10 |  |
| 8 | hella old | 3:11 |  |
