---
title: "Look For Your Mind!"
artist: "The Lemon Twigs"
year: 2026
tidal_id: 498548519
tags:
  - Musikexpressde
  - Plattentestsde
rating:
---

# Look For Your Mind!
**Artist:** The Lemon Twigs
**Year:** 2026

![[_covers/The Lemon Twigs - Look For Your Mind!.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/498548519
```
^button-hztb
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=The%20Lemon%20Twigs%20Look%20For%20Your%20Mind%21
```
^button-0gh1

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
| 1 | Look for Your Mind | 2:18 |  |
| 2 | 2 or 3 | 3:27 |  |
| 3 | Nothin’ but You | 3:35 |  |
| 4 | Gather Round | 3:01 |  |
| 5 | I Just Can’t Get Over Losing You | 2:08 |  |
| 6 | Fire and Gold | 3:30 |  |
| 7 | Mean to Me | 3:15 |  |
| 8 | Bring You Down | 2:49 |  |
| 9 | Yeah I Do | 1:54 |  |
| 10 | I Hurt You | 2:53 |  |
| 11 | You’re Still My Girl | 2:16 |  |
| 12 | Joy | 3:05 |  |
| 13 | My Heart Is in Your Hands Tonight | 3:13 |  |
| 14 | Your True Enemy | 3:50 |  |
