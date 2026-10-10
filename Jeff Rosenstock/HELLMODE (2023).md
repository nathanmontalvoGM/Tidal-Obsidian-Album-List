---
title: "HELLMODE"
artist: "Jeff Rosenstock"
year: 2023
tidal_id: 297910418
tags:
  - Powerpop
  - PopPunk
  - Indierock
  - Singersongwriter
rating:
---

# HELLMODE
**Artist:** Jeff Rosenstock
**Year:** 2023

![[_covers/Jeff Rosenstock - HELLMODE.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/297910418
```
^button-vkcp
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Jeff%20Rosenstock%20HELLMODE
```
^button-xddc

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
| 1 | WILL U STILL U | 3:20 |  |
| 2 | HEAD | 1:31 |  |
| 3 | LIKED U BETTER | 2:49 |  |
| 4 | DOUBT | 4:28 |  |
| 5 | FUTURE IS DUMB | 3:47 |  |
| 6 | SOFT LIVING | 4:46 |  |
| 7 | HEALMODE | 3:22 |  |
| 8 | LIFE ADMIN | 2:43 |  |
| 9 | I WANNA BE WRONG | 2:34 |  |
| 10 | GRAVEYARD SONG | 4:31 |  |
| 11 | 3 SUMMERS | 7:08 |  |
