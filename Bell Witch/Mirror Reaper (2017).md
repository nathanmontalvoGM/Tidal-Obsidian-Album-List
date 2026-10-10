---
title: "Mirror Reaper"
artist: "Bell Witch"
year: 2017
tidal_id: 312433627
tags:
  - Doommetal
  - FuneralDoomMetal
  - Sludge
  - Slowcore
rating:
---

# Mirror Reaper
**Artist:** Bell Witch
**Year:** 2017

![[_covers/Bell Witch - Mirror Reaper.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/312433627
```
^button-31j5
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Bell%20Witch%20Mirror%20Reaper
```
^button-qwox

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
| 1-1 | Mirror Reaper: As Above | 48:12 |  |
| 2-1 | Mirror Reaper: So Below | 35:29 |  |
