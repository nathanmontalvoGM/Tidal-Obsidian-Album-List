---
title: "Hellfire"
artist: "black midi"
year: 2022
tidal_id: 234935928
tags:
  - AvantProg
  - Brutalprog
  - Progressivepop
  - ArtRock
rating:
---

# Hellfire
**Artist:** black midi
**Year:** 2022

![[_covers/black midi - Hellfire.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/234935928
```
^button-td5o
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=black%20midi%20Hellfire
```
^button-b9gm

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
| 1 | Hellfire | 1:24 |  |
| 2 | Sugar/Tzu | 3:51 |  |
| 3 | Eat Men Eat | 3:08 |  |
| 4 | Welcome to Hell | 4:10 |  |
| 5 | Still | 5:46 |  |
| 6 | Half Time | 0:26 |  |
| 7 | The Race Is About to Begin | 7:15 |  |
| 8 | Dangerous Liaisons | 4:14 |  |
| 9 | The Defence | 2:59 |  |
| 10 | 27 Questions | 5:43 |  |
