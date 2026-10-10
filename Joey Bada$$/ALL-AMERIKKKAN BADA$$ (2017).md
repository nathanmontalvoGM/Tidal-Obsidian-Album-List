---
title: "ALL-AMERIKKKAN BADA$$"
artist: "Joey Bada$$"
year: 2017
tidal_id: 134832236
tags:
  - Hiphop
  - Conscioushiphop
  - Poprap
  - Boombap
rating:
---

# ALL-AMERIKKKAN BADA$$
**Artist:** Joey Bada$$
**Year:** 2017

![[_covers/Joey Bada$$ - ALL-AMERIKKKAN BADA$$.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/134832236
```
^button-m2mn
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Joey%20Bada%24%24%20ALL-AMERIKKKAN%20BADA%24%24
```
^button-7b2j

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
| 1 | Good Morning Amerikkka | 1:38 |  |
| 2 | For My People | 3:52 |  |
| 3 | Temptation | 4:04 |  |
| 4 | Land of the Free | 4:43 |  |
| 5 | Devastated | 3:27 |  |
| 6 | Y U Don't Love Me? (Miss Amerikkka) | 3:19 |  |
| 7 | Rockabye Baby | 3:43 |  |
| 8 | Ring the Alarm | 4:20 |  |
| 9 | Super Predator | 4:11 |  |
| 10 | Babylon | 5:36 |  |
| 11 | Legendary | 4:38 |  |
| 12 | Amerikkkan Idol | 6:11 |  |
