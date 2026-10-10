---
title: "The New Sound"
artist: "Geordie Greep"
year: 2024
tidal_id: 386875537
tags:
  - Progressivepop
  - ArtRock
  - Jazzrock
  - Rock
rating:
---

# The New Sound
**Artist:** Geordie Greep
**Year:** 2024

![[_covers/Geordie Greep - The New Sound.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/386875537
```
^button-mlm4
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Geordie%20Greep%20The%20New%20Sound
```
^button-7pni

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
| 1 | Blues | 5:42 |  |
| 2 | Terra | 4:18 |  |
| 3 | Holy, Holy | 6:03 |  |
| 4 | The New Sound | 4:47 |  |
| 5 | Walk Up | 4:25 |  |
| 6 | Through a War | 5:44 |  |
| 7 | Bongo Season | 2:35 |  |
| 8 | Motorbike | 6:01 |  |
| 9 | As If Waltz | 7:53 |  |
| 10 | The Magician | 12:20 |  |
| 11 | If You Are But a Dream | 3:07 |  |
