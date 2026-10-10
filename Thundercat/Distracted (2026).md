---
title: "Distracted"
artist: "Thundercat"
year: 2026
tidal_id: 494487953
tags:
  - Neosoul
  - Psychedelicpop
rating:
---

# Distracted
**Artist:** Thundercat
**Year:** 2026

![[_covers/Thundercat - Distracted.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/494487953
```
^button-14kn
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Thundercat%20Distracted
```
^button-ys7x

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
| 1 | Candlelight | 2:35 |  |
| 2 | No More Lies | 5:27 |  |
| 3 | She Knows Too Much | 3:33 |  |
| 4 | I Did This to Myself | 2:30 |  |
| 5 | Funny Friends | 2:35 |  |
| 6 | What Is Left to Say | 3:39 |  |
| 7 | I Wish I Didn’t Waste Your Time | 2:44 |  |
| 8 | Anakin Learns His Fate | 3:22 |  |
| 9 | Walking on the Moon | 3:25 |  |
| 10 | This Thing We Call Love | 3:15 |  |
| 11 | ThunderWave | 3:14 |  |
| 12 | Pozole | 2:40 |  |
| 13 | A.D.D. Through the Roof | 3:36 |  |
| 14 | Great Americans | 2:13 |  |
| 15 | You Left Without Saying Goodbye | 1:54 |  |
