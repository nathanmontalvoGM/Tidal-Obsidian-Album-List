---
title: "Something Worth Waiting For"
artist: "Friko"
year: 2026
tidal_id: 487209030
tags:
  - Indierock
rating:
---

# Something Worth Waiting For
**Artist:** Friko
**Year:** 2026

![[_covers/Friko - Something Worth Waiting For.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/487209030
```
^button-kzql
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Friko%20Something%20Worth%20Waiting%20For
```
^button-nd1d

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
| 1 | Guess | 3:46 |  |
| 2 | Still Around | 3:24 |  |
| 3 | Choo Choo | 3:20 |  |
| 4 | Alice | 4:15 |  |
| 5 | Certainty | 5:27 |  |
| 6 | Hot Air Balloon | 5:07 |  |
| 7 | Seven Degrees | 4:15 |  |
| 8 | Something Worth Waiting For | 5:54 |  |
| 9 | Dear Bicycle | 6:10 |  |
