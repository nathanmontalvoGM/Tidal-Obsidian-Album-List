---
title: "Mezmerize"
artist: "System Of A Down"
year: 2005
tidal_id: 560262
tags:
  - Alternativemetal
  - Numetal
  - Rock
  - Alternativerock
rating:
---

# Mezmerize
**Artist:** System Of A Down
**Year:** 2005

![[_covers/System Of A Down - Mezmerize.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/560262
```
^button-0wk8
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=System%20Of%20A%20Down%20Mezmerize
```
^button-06dd

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
| 1 | Soldier Side (intro) | 1:03 |  |
| 2 | B.Y.O.B. | 4:15 |  |
| 3 | Revenga | 3:48 |  |
| 4 | Cigaro | 2:11 |  |
| 5 | Radio/Video | 4:09 |  |
| 6 | This Cocaine Makes Me Feel Like I’m on This Song | 2:08 |  |
| 7 | Violent Pornography | 3:31 |  |
| 8 | Question! | 3:20 |  |
| 9 | Sad Statue | 3:25 |  |
| 10 | Old School Hollywood | 2:56 |  |
| 11 | Lost in Hollywood | 5:20 |  |
