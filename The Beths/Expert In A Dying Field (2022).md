---
title: "Expert In A Dying Field"
artist: "The Beths"
year: 2022
tidal_id: 248506900
tags:
  - Powerpop
  - Rock
  - Indie
  - Indiepop
rating:
---

# Expert In A Dying Field
**Artist:** The Beths
**Year:** 2022

![[_covers/The Beths - Expert In A Dying Field.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/248506900
```
^button-jzsb
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=The%20Beths%20Expert%20In%20A%20Dying%20Field
```
^button-sc6l

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
| 1 | Expert in a Dying Field | 4:11 |  |
| 2 | Knees Deep | 3:39 |  |
| 3 | Silence Is Golden | 2:56 |  |
| 4 | Your Side | 4:41 |  |
| 5 | I Want to Listen | 2:12 |  |
| 6 | Head in the Clouds | 4:01 |  |
| 7 | Best Left | 3:58 |  |
| 8 | Change in the Weather | 3:42 |  |
| 9 | When You Know You Know | 4:08 |  |
| 10 | A Passing Rain | 3:15 |  |
| 11 | I Told You That I Was Afraid | 3:21 |  |
| 12 | 2am | 4:49 |  |
| 13 | I Told You That I Was Afraid (acoustic) | 3:11 |  |
| 14 | When You Know You Know (acoustic) | 4:03 |  |
| 15 | A Real Thing | 3:34 |  |
| 16 | Watching the Credits | 3:15 |  |
| 17 | Keep the Distance (demo) | 4:08 |  |
| 18 | Expert in a Dying Field (demo) | 4:09 |  |
| 19 | I Want to Listen (demo) | 2:59 |  |
| 20 | 2am (demo) | 3:41 |  |
