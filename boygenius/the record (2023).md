---
title: "the record"
artist: "boygenius"
year: 2023
tidal_id: 286103660
tags:
  - Indierock
  - Indiefolk
  - Rock
  - Singersongwriter
rating:
---

# the record
**Artist:** boygenius
**Year:** 2023

![[_covers/boygenius - the record.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/286103660
```
^button-m1ka
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=boygenius%20the%20record
```
^button-m147

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
| 1 | Without You Without Them | 1:22 |  |
| 2 | $20 | 3:20 |  |
| 3 | Emily I’m Sorry | 3:35 |  |
| 4 | True Blue | 4:56 |  |
| 5 | Cool About It | 3:00 |  |
| 6 | Not Strong Enough | 3:55 |  |
| 7 | Revolution 0 | 4:17 |  |
| 8 | Leonard Cohen | 1:42 |  |
| 9 | Satanist | 4:50 |  |
| 10 | We’re in Love | 4:55 |  |
| 11 | Anti‐Curse | 3:19 |  |
| 12 | Letter to an Old Poet | 3:08 |  |
