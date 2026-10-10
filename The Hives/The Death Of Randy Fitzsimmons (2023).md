---
title: "The Death Of Randy Fitzsimmons"
artist: "The Hives"
year: 2023
tidal_id: 287696659
tags:
  - GaragePunk
  - Playful
  - Witty
  - Energetic
rating:
---

# The Death Of Randy Fitzsimmons
**Artist:** The Hives
**Year:** 2023

![[_covers/The Hives - The Death Of Randy Fitzsimmons.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/287696659
```
^button-norz
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=The%20Hives%20The%20Death%20Of%20Randy%20Fitzsimmons
```
^button-olfo

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
| 1 | Bogus Operandi | 3:43 |  |
| 2 | Trapdoor Solution | 1:03 |  |
| 3 | Countdown to Shutdown | 3:13 |  |
| 4 | Rigor Mortis Radio | 2:28 |  |
| 5 | Stick Up | 2:19 |  |
| 6 | Smoke & Mirrors | 3:01 |  |
| 7 | Crash Into the Weekend | 2:58 |  |
| 8 | Two Kinds of Trouble | 2:44 |  |
| 9 | The Way the Story Goes | 2:56 |  |
| 10 | The Bomb | 2:13 |  |
| 11 | What Did I Ever Do to You? | 3:09 |  |
| 12 | Step Out of the Way | 1:39 |  |
