---
title: "Bloodmoon: I"
artist: "Converge"
year: 2021
tidal_id: 196017208
tags:
  - GothicMetal
  - SludgeMetal
  - Doommetal
  - Postmetal
rating:
---

# Bloodmoon: I
**Artist:** Converge
**Year:** 2021

![[_covers/Converge - Bloodmoon- I.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/196017208
```
^button-hjpj
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Converge%20Bloodmoon%3A%20I
```
^button-1hat

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
| 1 | Blood Moon | 7:51 |  |
| 2 | Viscera of Men | 5:29 |  |
| 3 | Coil | 6:08 |  |
| 4 | Flower Moon | 4:38 |  |
| 5 | Tongues Playing Dead | 4:12 |  |
| 6 | Lord of Liars | 3:21 |  |
| 7 | Failure Forever | 4:03 |  |
| 8 | Scorpion’s Sting | 5:48 |  |
| 9 | Daimon | 6:59 |  |
| 10 | Crimson Stone | 6:47 |  |
| 11 | Blood Dawn | 3:31 |  |
