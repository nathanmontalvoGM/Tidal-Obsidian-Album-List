---
title: "I Get Wet"
artist: "Andrew W.K."
year: 2001
tidal_id: 578167
tags:
  - Rock
  - Hardrock
  - Partymetal
  - Heavymetal
rating:
---

# I Get Wet
**Artist:** Andrew W.K.
**Year:** 2001

![[_covers/Andrew W.K - I Get Wet.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/578167
```
^button-gb3v
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Andrew%20W.K.%20I%20Get%20Wet
```
^button-7ahs

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
| 1 | It’s Time to Party | 1:30 |  |
| 2 | Party Hard | 3:04 |  |
| 3 | Girls Own Love | 3:13 |  |
| 4 | Ready to Die | 2:54 |  |
| 5 | Take It Off | 3:10 |  |
| 6 | I Love NYC | 3:11 |  |
| 7 | She Is Beautiful | 3:33 |  |
| 8 | Party Til You Puke | 2:34 |  |
| 9 | Fun Night | 3:23 |  |
| 10 | Got to Do It | 3:55 |  |
| 11 | I Get Wet | 3:23 |  |
| 12 | Don’t Stop Living in the Red | 1:40 |  |
