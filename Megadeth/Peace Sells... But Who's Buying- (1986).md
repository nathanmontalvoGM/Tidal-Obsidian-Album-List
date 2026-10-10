---
title: "Peace Sells... But Who's Buying?"
artist: "Megadeth"
year: 1986
tidal_id: 77622277
tags:
  - Thrashmetal
  - Heavymetal
  - Numetal
  - Speedmetal
rating:
---

# Peace Sells... But Who's Buying?
**Artist:** Megadeth
**Year:** 1986

![[_covers/Megadeth - Peace Sells... But Who's Buying-.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/77622277
```
^button-inc6
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Megadeth%20Peace%20Sells...%20But%20Who%27s%20Buying%3F
```
^button-m2iv

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
| 1 | Wake Up Dead | 3:37 |  |
| 2 | The Conjuring | 5:02 |  |
| 3 | Peace Sells | 4:02 |  |
| 4 | Devil’s Island | 5:05 |  |
| 5 | Good Mourning / Black Friday | 6:39 |  |
| 6 | Bad Omen | 4:03 |  |
| 7 | I Ain’t Superstitious | 2:45 |  |
| 8 | My Last Words | 4:55 |  |
| 9 | Wake Up Dead (Randy Burns mix) | 3:40 |  |
| 10 | The Conjuring (Randy Burns mix) | 5:01 |  |
| 11 | Peace Sells (Randy Burns mix) | 4:00 |  |
| 12 | Good Mourning / Black Friday (Randy Burns mix) | 6:39 |  |
