---
title: "Slaughter Of The Soul"
artist: "At The Gates"
year: 1995
tidal_id: 13917157
tags:
  - Melodicdeathmetal
  - Mathmetal
rating:
---

# Slaughter Of The Soul
**Artist:** At The Gates
**Year:** 1995

![[_covers/At The Gates - Slaughter Of The Soul.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/13917157
```
^button-jvyu
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=At%20The%20Gates%20Slaughter%20Of%20The%20Soul
```
^button-b5sy

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
| 1 | Blinded by Fear | 3:11 |  |
| 2 | Slaughter of the Soul | 3:03 |  |
| 3 | Cold | 3:27 |  |
| 4 | Under a Serpent Sun | 3:59 |  |
| 5 | Into the Dead Sky | 2:12 |  |
| 6 | Suicide Nation | 3:36 |  |
| 7 | World of Lies | 3:35 |  |
| 8 | Unto Others | 3:11 |  |
| 9 | Nausea | 2:23 |  |
| 10 | Need | 2:36 |  |
| 11 | The Flames of the End | 2:56 |  |
