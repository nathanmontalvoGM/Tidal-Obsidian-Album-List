---
title: "Punisher"
artist: "Phoebe Bridgers"
year: 2020
tidal_id: 135629244
tags:
  - Indierock
  - Singersongwriter
  - Indie
  - Rock
rating:
---

# Punisher
**Artist:** Phoebe Bridgers
**Year:** 2020

![[_covers/Phoebe Bridgers - Punisher.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/135629244
```
^button-2hk2
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Phoebe%20Bridgers%20Punisher
```
^button-wyl3

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
| 1 | DVD Menu | 1:09 |  |
| 2 | Garden Song | 3:39 |  |
| 3 | Kyoto | 3:04 |  |
| 4 | Punisher | 3:09 |  |
| 5 | Halloween | 4:31 |  |
| 6 | Chinese Satellite | 3:37 |  |
| 7 | Moon Song | 4:37 |  |
| 8 | Savior Complex | 4:01 |  |
| 9 | ICU | 3:10 |  |
| 10 | Graceland Too | 3:56 |  |
| 11 | I Know the End | 5:44 |  |
