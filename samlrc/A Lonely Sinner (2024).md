---
title: "A Lonely Sinner"
artist: "samlrc"
year: 2024
tidal_id: 349750093
tags:
  - Postrock
  - Shoegaze
  - Ambient
  - Postmetal
rating:
---

# A Lonely Sinner
**Artist:** samlrc
**Year:** 2024

![[_covers/samlrc - A Lonely Sinner.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/349750093
```
^button-1418
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=samlrc%20A%20Lonely%20Sinner
```
^button-dbes

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
| 1 | Lamb Theme | 1:48 |  |
| 2 | Philautia | 12:00 |  |
| 3 | Sinner | 7:55 |  |
| 4 | Flowerfields | 4:44 |  |
| 5 | Storge | 11:42 |  |
| 6 | Sheep Theme | 3:05 |  |
| 7 | For M. | 5:13 |  |
| 8 | The Beauty of the Present Moment | 2:38 |  |
