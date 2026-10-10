---
title: "Songs for the General Public"
artist: "The Lemon Twigs"
year: 2020
tidal_id: 151915946
tags:
  - Glamrock
  - Poprock
  - Powerpop
  - Newwave
rating:
---

# Songs for the General Public
**Artist:** The Lemon Twigs
**Year:** 2020

![[_covers/The Lemon Twigs - Songs for the General Public.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/151915946
```
^button-ov9j
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=The%20Lemon%20Twigs%20Songs%20for%20the%20General%20Public
```
^button-vxlf

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
| 1 | Hell on Wheels | 3:40 |  |
| 2 | Live in Favor of Tomorrow | 3:24 |  |
| 3 | No One Holds You (Closer Than the One You Haven’t Met) | 3:30 |  |
| 4 | Fight | 3:03 |  |
| 5 | Somebody Loving You | 3:51 |  |
| 6 | Moon | 4:06 |  |
| 7 | The One | 2:26 |  |
| 8 | Only a Fool | 3:25 |  |
| 9 | Hog | 4:24 |  |
| 10 | Why Do Lovers Own Each Other? | 2:45 |  |
| 11 | Leather Together | 3:28 |  |
| 12 | Ashamed | 5:20 |  |
