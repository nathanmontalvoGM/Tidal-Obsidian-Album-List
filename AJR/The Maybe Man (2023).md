---
title: The Maybe Man
artist: AJR
year: 2023
tidal_id: 326417453
tags:
  - Pop
  - Alternativerock
  - Indiepop
  - Orchestral
rating:
---

# The Maybe Man
**Artist:** AJR
**Year:** 2023

![[_covers/AJR - The Maybe Man.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/326417453
```
^button-w58u
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=AJR%20The%20Maybe%20Man
```
^button-02fc

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
| 1 | Maybe Man | 3:40 |  |
| 2 | Touchy Feely Fool | 3:35 |  |
| 3 | Yes I'm a Mess | 2:44 |  |
| 4 | The Dumb Song | 3:45 |  |
| 5 | Inertia | 3:40 |  |
| 6 | Turning Out Pt. iii | 3:50 |  |
| 7 | Hole in the Bottom of My Brain | 3:07 |  |
| 8 | The DJ Is Crying for Help | 3:39 |  |
| 9 | I Won’t | 2:48 |  |
| 10 | Steve’s Going to London | 4:47 |  |
| 11 | God Is Really Real | 2:59 |  |
| 12 | 2085 | 5:31 |  |
