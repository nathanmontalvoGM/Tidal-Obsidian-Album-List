---
title: "A Boat on the Sea"
artist: "Moron Police"
year: 2019
tidal_id: 112688193
tags:
  - Punk
  - Heavymetal
  - Alternativemetal
  - Progressivepop
rating:
---

# A Boat on the Sea
**Artist:** Moron Police
**Year:** 2019

![[_covers/Moron Police - A Boat on the Sea.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/112688193
```
^button-fl31
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Moron%20Police%20A%20Boat%20on%20the%20Sea
```
^button-pc8u

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
| 1 | Hocus Pocus | 1:20 |  |
| 2 | The Phantom Below | 4:12 |  |
| 3 | The Invisible King | 4:05 |  |
| 4 | Beware the Blue Skies | 4:11 |  |
| 5 | The Dog Song | 3:20 |  |
| 6 | Captain Awkward | 5:12 |  |
| 7 | The Undersea | 3:27 |  |
| 8 | Isn't It Easy! | 6:57 |  |
| 9 | Cult of Tuna | 4:05 |  |
| 10 | Starlight Cinema (demo) | 2:35 |  |
| 11 | Desolation (demo) | 2:37 |  |
| 12 | Japanese Pogo Stick Adventure! | 3:49 |  |
