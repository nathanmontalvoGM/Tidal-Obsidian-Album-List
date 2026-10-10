---
title: "Alaska"
artist: "Between The Buried And Me"
year: 2005
tidal_id: 75669905
tags:
  - Progressivemetal
  - Metalcore
  - Mathmetal
  - Alternativemetal
rating:
---

# Alaska
**Artist:** Between The Buried And Me
**Year:** 2005

![[_covers/Between The Buried And Me - Alaska.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/75669905
```
^button-mvpf
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Between%20The%20Buried%20And%20Me%20Alaska
```
^button-in9y

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
| 1 | All Bodies | 6:12 |  |
| 2 | Alaska | 3:57 |  |
| 3 | Croakies and Boatshoes | 2:22 |  |
| 4 | Selkies: The Endless Obsession | 7:23 |  |
| 5 | Breathe In, Breathe Out | 0:55 |  |
| 6 | Roboturner | 7:07 |  |
| 7 | Backwards Marathon | 8:27 |  |
| 8 | Medicine Wheel | 4:18 |  |
| 9 | The Primer | 4:46 |  |
| 10 | Autodidact | 5:30 |  |
| 11 | Laser Speed | 2:53 |  |
