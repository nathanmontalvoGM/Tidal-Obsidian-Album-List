---
title: Se Bueno
artist: TURQUOISEDEATH
year: 2023
tidal_id: 305246383
tags:
  - Atmosphericdrumandbass
  - DreamPop
  - Shoegaze
rating:
---

# Se Bueno
**Artist:** TURQUOISEDEATH
**Year:** 2023

![[_covers/TURQUOISEDEATH - Se Bueno.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/305246383
```
^button-6tg5
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=TURQUOISEDEATH%20Se%20Bueno
```
^button-ecg3

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
| 1 | Eureka! | 1:12 |  |
| 2 | The Sky Fell | 3:17 |  |
| 3 | Crawl Space | 5:09 |  |
| 4 | Sinking Into You | 5:00 |  |
| 5 | Dive | 6:52 |  |
| 6 | Guessabelle | 7:10 |  |
| 7 | Starfields | 8:48 |  |
| 8 | Vertigo | 7:48 |  |
| 9 | Escape Your Dream | 4:57 |  |
