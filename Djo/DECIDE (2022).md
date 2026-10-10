---
title: "DECIDE"
artist: "Djo"
year: 2022
tidal_id: 246282414
tags:
  - Synthpop
  - Indiepop
  - Neopsychedelia
  - Psychedelicpop
rating:
---

# DECIDE
**Artist:** Djo
**Year:** 2022

![[_covers/Djo - DECIDE.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/246282414
```
^button-n2xc
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Djo%20DECIDE
```
^button-49rm

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
| 1 | Runner | 4:19 |  |
| 2 | Gloom | 2:00 |  |
| 3 | Half Life | 3:47 |  |
| 4 | Fool | 1:54 |  |
| 5 | On and On | 4:03 |  |
| 6 | End of Beginning | 2:39 |  |
| 7 | I Want Your Video | 2:08 |  |
| 8 | Climax | 3:55 |  |
| 9 | Change | 2:57 |  |
| 10 | Is That All It Takes | 0:20 |  |
| 11 | Go for It | 3:01 |  |
| 12 | Figure You Out | 3:04 |  |
| 13 | Slither | 1:51 |  |
