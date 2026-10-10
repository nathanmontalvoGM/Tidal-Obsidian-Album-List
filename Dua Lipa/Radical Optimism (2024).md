---
title: "Radical Optimism"
artist: "Dua Lipa"
year: 2024
tidal_id: 360212374
tags:
  - Pop
  - Dancepop
  - Disco
  - House
rating:
---

# Radical Optimism
**Artist:** Dua Lipa
**Year:** 2024

![[_covers/Dua Lipa - Radical Optimism.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/360212374
```
^button-udni
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Dua%20Lipa%20Radical%20Optimism
```
^button-fbey

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
| 1 | End of an Era | 3:16 |  |
| 2 | Houdini | 3:05 |  |
| 3 | Training Season | 3:29 |  |
| 4 | These Walls | 3:37 |  |
| 5 | Whatcha Doing | 3:18 |  |
| 6 | French Exit | 3:21 |  |
| 7 | Illusion | 3:08 |  |
| 8 | Falling Forever | 3:43 |  |
| 9 | Anything for Love | 2:21 |  |
| 10 | Maria | 3:07 |  |
| 11 | Happy for You | 4:05 |  |
