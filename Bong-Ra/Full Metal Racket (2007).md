---
title: "Full Metal Racket"
artist: "Bong-Ra"
year: 2007
tidal_id: 431021959
tags:
  - Breakcore
  - Cybergrind
  - Numetal
  - Grindcore
rating:
---

# Full Metal Racket
**Artist:** Bong-Ra
**Year:** 2007

![[_covers/Bong-Ra - Full Metal Racket.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/431021959
```
^button-c17g
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Bong-Ra%20Full%20Metal%20Racket
```
^button-d6u1

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
| 1 | Terrorizah | 4:15 |  |
| 2 | Slaytronic | 4:43 |  |
| 3 | Necrogoat | 4:52 |  |
| 4 | Earache | 5:10 |  |
| 5 | Bloody Cenotaph | 3:49 |  |
| 6 | Jo Bench | 4:45 |  |
| 7 | Ram Waster | 5:10 |  |
| 8 | DSTRCTV | 3:41 |  |
| 9 | Grindkrush (Doormouse remix) | 3:25 |  |
| 10 | Painkiller (Sickboy remix) | 3:39 |  |
