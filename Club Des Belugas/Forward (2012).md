---
title: "Forward"
artist: "Club Des Belugas"
year: 2012
tidal_id: 139986856
tags:
  - NuJazz
  - Lounge
  - Jazz
  - GimmeSummaDatSwaaang
rating:
---

# Forward
**Artist:** Club Des Belugas
**Year:** 2012

![[_covers/Club Des Belugas - Forward.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/139986856
```
^button-z8ld
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Club%20Des%20Belugas%20Forward
```
^button-p8ha

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
| 1 | Save A Little Love For Me | 3:32 |  |
| 2 | Straight to Memphis | 5:15 |  |
| 3 | Peanut Vendor (Club Des Belugas remix) | 3:43 |  |
| 4 | All Aboard | 4:15 |  |
| 5 | Forward | 3:37 |  |
| 6 | Desperately Trying (Swing mix) | 3:47 |  |
| 7 | Close Your Eyes | 4:11 |  |
| 8 | I Shouldn't I Wouldn't (Club des Belugas Remix) | 3:52 |  |
| 9 | The Beat Is Rhythm | 4:28 |  |
| 10 | Dat Thang | 4:01 |  |
| 11 | Posing | 3:23 |  |
| 12 | The Hunting (Club Des Belugas remix) | 4:02 |  |
| 13 | Sweet Lovin' | 3:39 |  |
| 14 | Ocean Cruise | 4:10 |  |
| 15 | Is This Real | 4:22 |  |
| 16 | Glorious Beach Livin' | 3:36 |  |
