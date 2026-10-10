---
title: "Appaloosa"
artist: "Orville Peck"
year: 2025
tidal_id: 468760969
tags:
  - Alternativecountry
  - Country
  - Countryfolk
  - Singersongwriter
rating:
---

# Appaloosa
**Artist:** Orville Peck
**Year:** 2025

![[_covers/Orville Peck - Appaloosa.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/468760969
```
^button-nwhj
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Orville%20Peck%20Appaloosa
```
^button-fs8l

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
| 1 | Dreaded Sundown | 3:23 |  |
| 2 | Drift Away | 3:35 |  |
| 3 | Atchafalaya | 3:46 |  |
| 4 | Maybe This Time | 3:59 |  |
| 5 | Oh My Days | 3:33 |  |
| 6 | My Side of the Mountain | 3:21 |  |
| 7 | It's the End of the World | 3:24 |  |
