---
title: "The Eminem Show"
artist: "Eminem"
year: 2002
tidal_id: 573283
tags:
  - Rap
  - Hiphop
  - Eminem
  - 00s
rating:
---

# The Eminem Show
**Artist:** Eminem
**Year:** 2002

![[_covers/Eminem - The Eminem Show.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/573283
```
^button-vii4
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Eminem%20The%20Eminem%20Show
```
^button-b3z4

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
| 1 | Curtains Up (skit) | 0:29 |  |
| 2 | White America | 5:24 |  |
| 3 | Business | 4:11 |  |
| 4 | Cleanin’ Out My Closet | 4:57 |  |
| 5 | Square Dance | 5:24 |  |
| 6 | The Kiss (skit) | 1:15 |  |
| 7 | Soldier | 3:46 |  |
| 8 | Say Goodbye Hollywood | 4:32 |  |
| 9 | Drips | 4:45 |  |
| 10 | Without Me | 4:50 |  |
| 11 | Paul Rosenberg (skit) | 0:22 |  |
| 12 | Sing for the Moment | 5:39 |  |
| 13 | Superman | 5:50 |  |
| 14 | Hailie’s Song | 5:20 |  |
| 15 | Steve Berman (skit) | 0:33 |  |
| 16 | When the Music Stops | 4:28 |  |
| 17 | Say What You Say | 5:09 |  |
| 18 | Till I Collapse | 4:57 |  |
| 19 | My Dad’s Gone Crazy | 4:26 |  |
| 20 | Curtains Close (skit) | 1:02 |  |
