---
title: "Human Overboard"
artist: "James and the Shame"
year: 2022
tidal_id: 243642530
tags:
  - Country
  - Folk
  - Americana
rating:
---

# Human Overboard
**Artist:** James and the Shame
**Year:** 2022

![[_covers/James and the Shame - Human Overboard.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/243642530
```
^button-9nvz
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=James%20and%20the%20Shame%20Human%20Overboard
```
^button-rvdo

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
| 1 | Believe Me | 4:07 |  |
| 2 | Flash of Rationality | 2:54 |  |
| 3 | Give a Damn | 3:26 |  |
| 4 | Sorry | 3:51 |  |
| 5 | Where We're Going | 4:05 |  |
| 6 | Creek and Back | 3:51 |  |
| 7 | Only Thing | 3:35 |  |
| 8 | Kill a Man | 3:51 |  |
| 9 | In Vain | 3:41 |  |
| 10 | Fruit | 4:03 |  |
| 11 | Old Letters | 3:15 |  |
