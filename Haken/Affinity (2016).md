---
title: "Affinity"
artist: "Haken"
year: 2016
tidal_id: 57770227
tags:
  - Progressivemetal
  - Progressivepop
  - Numetal
  - Intro
rating:
---

# Affinity
**Artist:** Haken
**Year:** 2016

![[_covers/Haken - Affinity.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/57770227
```
^button-6gab
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Haken%20Affinity
```
^button-6okg

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
| 1 | affinity.exe | 1:24 |  |
| 2 | Initiate | 4:16 |  |
| 3 | 1985 | 9:09 |  |
| 4 | Lapse | 4:44 |  |
| 5 | The Architect | 15:40 |  |
| 6 | Earthrise | 4:48 |  |
| 7 | Red Giant | 6:06 |  |
| 8 | The Endless Knot | 5:50 |  |
| 9 | Bound by Gravity | 9:29 |  |
