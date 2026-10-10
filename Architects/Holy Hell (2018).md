---
title: "Holy Hell"
artist: "Architects"
year: 2018
tidal_id: 121049468
tags:
  - Metalcore
  - Progressivemetal
  - Technicaldeathmetal
  - Posthardcore
rating:
---

# Holy Hell
**Artist:** Architects
**Year:** 2018

![[_covers/Architects - Holy Hell.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/121049468
```
^button-mmc9
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Architects%20Holy%20Hell
```
^button-xhur

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
| 1 | Death Is Not Defeat | 3:45 |  |
| 2 | Hereafter | 4:15 |  |
| 3 | Mortal After All | 3:39 |  |
| 4 | Holy Hell | 4:13 |  |
| 5 | Damnation | 4:08 |  |
| 6 | Royal Beggars | 4:01 |  |
| 7 | Modern Misery | 4:13 |  |
| 8 | Dying to Heal | 3:50 |  |
| 9 | The Seventh Circle | 1:48 |  |
| 10 | Doomsday | 4:08 |  |
| 11 | A Wasted Hymn | 4:34 |  |
