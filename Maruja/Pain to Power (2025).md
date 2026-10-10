---
title: "Pain to Power"
artist: "Maruja"
year: 2025
tidal_id: 457113845
tags:
  - Postrock
  - Postpunk
  - Raprock
  - Jazzrock
rating:
---

# Pain to Power
**Artist:** Maruja
**Year:** 2025

![[_covers/Maruja - Pain to Power.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/457113845
```
^button-ezhs
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Maruja%20Pain%20to%20Power
```
^button-vloh

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
| 1 | Bloodsport | 3:42 |  |
| 2 | Look Down on Us | 9:58 |  |
| 3 | Saoirse | 5:13 |  |
| 4 | Born to Die | 10:04 |  |
| 5 | Break the Tension | 3:44 |  |
| 6 | Trenches | 3:32 |  |
| 7 | Zaytoun | 4:20 |  |
| 8 | Reconcile | 9:40 |  |
