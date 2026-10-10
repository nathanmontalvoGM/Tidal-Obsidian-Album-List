---
title: Clancy
artist: twenty one pilots
year: 2024
tidal_id: 364834730
tags:
  - Favorite
  - Rock
  - Triphop
  - Altpop
  - Alternativerock
rating: "7.2"
---

# Clancy
**Artist:** twenty one pilots
**Year:** 2024

![[_covers/twenty one pilots - Clancy.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/364834730
```
^button-xz0d
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=twenty%20one%20pilots%20Clancy
```
^button-52zq

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

| #   | Title                         | Duration | Rating /10 |
| --- | ----------------------------- | -------- | ---------- |
| 1   | Overcompensate                | 3:56     | 9          |
| 2   | Next Semester                 | 3:54     | 8          |
| 3   | Backslide                     | 3:00     | 7          |
| 4   | Midwest Indigo                | 3:16     | 7          |
| 5   | Routines in the Night         | 3:22     | 8          |
| 6   | Vignette                      | 3:22     | 6.5        |
| 7   | The Craving (Jenna’s version) | 2:54     | 6          |
| 8   | Lavish                        | 2:38     | 5          |
| 9   | Navigating                    | 3:43     | 9          |
| 10  | Snap Back                     | 3:30     | 6.5        |
| 11  | Oldies Station                | 3:48     | 7.5        |
| 12  | At the Risk of Feeling Dumb   | 3:23     | 7          |
| 13  | Paladin Strait                | 6:28     | 7          |
|     |                               |          |            |
