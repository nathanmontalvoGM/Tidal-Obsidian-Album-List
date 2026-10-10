---
title: "The Click (Deluxe Edition)"
artist: "AJR"
year: 2017
tidal_id: 492949321
tags:
  - SuperExperimental
  - Pop
  - HeardLive
  - DigitalTendencies
rating:
---

# The Click (Deluxe Edition)
**Artist:** AJR
**Year:** 2017

![[_covers/AJR - The Click (Deluxe Edition).jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/492949321
```
^button-6nga
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=AJR%20The%20Click%20%28Deluxe%20Edition%29
```
^button-2469

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
| 1 | Overture | 3:34 |  |
| 2 | The Good Part | 3:47 |  |
| 3 | Weak | 3:21 |  |
| 4 | Sober Up | 3:38 |  |
| 5 | Drama | 3:24 |  |
| 6 | Turning Out | 4:20 |  |
| 7 | No Grass Today | 4:19 |  |
| 8 | Three‐Thirty | 3:30 |  |
| 9 | Call My Dad | 2:15 |  |
| 10 | I’m Not Famous | 3:40 |  |
| 11 | Netflix Trip | 3:57 |  |
| 12 | Bud Like You | 3:50 |  |
| 13 | Come Hang Out | 4:26 |  |
| 14 | Burn the House Down | 3:32 |  |
| 15 | Role Models | 3:12 |  |
| 16 | Normal | 3:05 |  |
| 17 | Pretender (acoustic) | 3:01 |  |
