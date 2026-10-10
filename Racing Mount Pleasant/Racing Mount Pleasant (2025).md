---
title: "Racing Mount Pleasant"
artist: "Racing Mount Pleasant"
year: 2025
tidal_id: 447151886
tags:
  - Chamberpop
  - Postrock
  - ArtRock
  - Rock
rating:
---

# Racing Mount Pleasant
**Artist:** Racing Mount Pleasant
**Year:** 2025

![[_covers/Racing Mount Pleasant - Racing Mount Pleasant.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/447151886
```
^button-0sr9
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Racing%20Mount%20Pleasant%20Racing%20Mount%20Pleasant
```
^button-c4mp

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
| 1 | Your New Place | 7:32 |  |
| 2 | Tenspeed (Shallows) | 3:51 |  |
| 3 | Heavy Red | 1:30 |  |
| 4 | Emily | 5:55 |  |
| 5 | Seminary | 4:56 |  |
| 6 | You | 4:07 |  |
| 7 | You, Pt. 2 | 4:07 |  |
| 8 | Racing Mount Pleasant | 5:15 |  |
| 9 | Call It Easy | 7:00 |  |
| 10 | Outlast | 5:01 |  |
| 11 | 34th Floor | 1:31 |  |
| 12 | Seyburn | 2:12 |  |
| 13 | Your Old Place | 4:33 |  |
