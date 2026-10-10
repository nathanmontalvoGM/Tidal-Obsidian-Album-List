---
title: "Matriphagy"
artist: "Tallah"
year: 2020
tidal_id: 142789457
tags:
  - Metalcore
  - Numetal
  - Industrialmetal
  - Rock
rating:
---

# Matriphagy
**Artist:** Tallah
**Year:** 2020

![[_covers/Tallah - Matriphagy.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/142789457
```
^button-kdru
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Tallah%20Matriphagy
```
^button-r2pi

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
| 1 | [redacted] | 1:12 |  |
| 2 | No One Should Read This | 4:43 |  |
| 3 | Kungan | 4:36 |  |
| 4 | Overconfidence | 5:06 |  |
| 5 | Placenta | 4:08 |  |
| 6 | L.E.D. | 4:16 |  |
| 7 | The Silo | 4:47 |  |
| 8 | We, the Sad | 5:09 |  |
| 9 | Too Quick to Grieve | 6:00 |  |
| 10 | Cottonmouth | 2:53 |  |
| 11 | Murder Seed | 4:28 |  |
| 12 | the borderline of pain | 0:48 |  |
| 13 | Red Light | 5:06 |  |
