---
title: "After the Magic"
artist: "Parannoul"
year: 2023
tidal_id: 273688157
tags:
  - Shoegaze
  - Indierock
  - Postrock
  - Indietronica
rating:
---

# After the Magic
**Artist:** Parannoul
**Year:** 2023

![[_covers/Parannoul - After the Magic.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/273688157
```
^button-ao5d
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Parannoul%20After%20the%20Magic
```
^button-lr5k

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
| 1 | 북극성 (Polaris) | 4:22 |  |
| 2 | 불면증 (Insomnia) | 4:49 |  |
| 3 | 도착 (Arrival) | 7:44 |  |
| 4 | 우리는 밤이 되면 빛난다 (We Shine at Night) | 6:27 |  |
| 5 | Parade | 7:34 |  |
| 6 | 스케치북 (Sketchbook) | 7:02 |  |
| 7 | Imagination | 4:37 |  |
| 8 | Sound Inside Me, Waves Inside You | 5:13 |  |
| 9 | 개화 (Blossom) | 6:11 |  |
| 10 | After the Magic | 5:02 |  |
