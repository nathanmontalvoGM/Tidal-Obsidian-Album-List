---
title: "Rossz Csillag Alatt Született"
artist: "Venetian Snares"
year: 2005
tidal_id: 111947317
tags:
  - Breakcore
  - ModernClassical
  - Electronicore
  - Idm
rating:
---

# Rossz Csillag Alatt Született
**Artist:** Venetian Snares
**Year:** 2005

![[_covers/Venetian Snares - Rossz Csillag Alatt Született.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/111947317
```
^button-ljik
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Venetian%20Snares%20Rossz%20Csillag%20Alatt%20Sz%C3%BCletett
```
^button-sg13

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
| 1 | Sikertelenség | 0:40 |  |
| 2 | Szerencsétlen | 4:55 |  |
| 3 | Öngyilkos vasárnap | 3:26 |  |
| 4 | Felbomlasztott mentőkocsi | 3:44 |  |
| 5 | Hajnal | 7:46 |  |
| 6 | Galamb egyedül | 1:36 |  |
| 7 | Második galamb | 6:01 |  |
| 8 | Szamár madár | 5:48 |  |
| 9 | Hiszékeny | 1:39 |  |
| 10 | Kétsarkú mozgalom | 8:50 |  |
| 11 | Senki dala | 2:16 |  |
