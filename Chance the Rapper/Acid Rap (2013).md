---
title: "Acid Rap"
artist: "Chance the Rapper"
year: 2013
tidal_id: 397474752
tags:
  - Rap
  - Poprap
  - Hiphop
  - Chancetherapper
rating:
---

# Acid Rap
**Artist:** Chance the Rapper
**Year:** 2013

![[_covers/Chance the Rapper - Acid Rap.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/397474752
```
^button-avgh
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Chance%20the%20Rapper%20Acid%20Rap
```
^button-9jzj

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
| 1 | Good Ass Intro | 4:00 |  |
| 2 | Pusha Man | 7:25 |  |
| 3 | Cocoa Butter Kisses | 5:08 |  |
| 4 | Juice | 3:35 |  |
| 5 | Lost | 3:05 |  |
| 6 | Everybody’s Something | 4:37 |  |
| 7 | Interlude (That’s Love) | 2:30 |  |
| 8 | Favorite Song | 3:05 |  |
| 9 | NaNa | 3:21 |  |
| 10 | Smoke Again | 4:33 |  |
| 11 | Acid Rain | 3:37 |  |
| 12 | Chain Smoker | 3:31 |  |
| 13 | Everything’s Good (Good Ass outro) | 5:34 |  |
