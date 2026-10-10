---
title: "I Didn't Mean To Haunt You"
artist: "Quadeca"
year: 2022
tidal_id: 258132984
tags:
  - Folktronica
  - ArtPop
  - ExperimentalHipHop
  - Glitchpop
rating:
---

# I Didn't Mean To Haunt You
**Artist:** Quadeca
**Year:** 2022

![[_covers/Quadeca - I Didn't Mean To Haunt You.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/258132984
```
^button-06r7
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Quadeca%20I%20Didn%27t%20Mean%20To%20Haunt%20You
```
^button-49ua

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
| 1 | sorry4dying | 4:44 |  |
| 2 | tell me a joke | 5:04 |  |
| 3 | don’t mind me | 5:09 |  |
| 4 | picking up hands | 4:59 |  |
| 5 | born yesterday | 6:01 |  |
| 6 | the memories we lost in translation | 1:42 |  |
| 7 | house settling | 4:52 |  |
| 8 | knots | 4:11 |  |
| 9 | fantasyworld | 7:18 |  |
| 10 | fractions of infinity | 5:23 |  |
| 11 | cassini's division | 8:16 |  |
