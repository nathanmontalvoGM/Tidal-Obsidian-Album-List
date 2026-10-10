---
title: "Piss In The Wind"
artist: "Joji"
year: 2026
tidal_id: 496062524
tags:
  - Altpop
  - Alternativerandb
  - Rnb
  - Wave
rating:
---

# Piss In The Wind
**Artist:** Joji
**Year:** 2026

![[_covers/Joji - Piss In The Wind.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/496062524
```
^button-lj3k
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Joji%20Piss%20In%20The%20Wind
```
^button-mfrx

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
| 1 | PIXELATED KISSES | 1:50 |  |
| 2 | Cigarette | 1:50 |  |
| 3 | Last of a Dying Breed | 2:29 |  |
| 4 | LOVE YOU LESS | 3:21 |  |
| 5 | If It Only Gets Better | 1:08 |  |
| 6 | Love Me Better | 1:53 |  |
| 7 | Piece of You | 2:15 |  |
| 8 | Hotel California | 2:08 |  |
| 9 | Tarmac | 1:35 |  |
| 10 | Forehead Touch the Ground | 1:56 |  |
| 11 | Past Won’t Leave My Bed | 2:46 |  |
| 12 | Fade to Black | 1:15 |  |
| 13 | CAN’T SEE SH*T IN THE CLUB | 2:51 |  |
| 14 | Sojourn | 2:56 |  |
| 15 | DYKILY | 2:37 |  |
| 16 | Rose Colored | 2:33 |  |
| 17 | Silhouette Man | 1:26 |  |
| 18 | Fragments | 1:59 |  |
| 19 | Horses to Water | 2:17 |  |
| 20 | Strange Home | 2:50 |  |
| 21 | Dior | 1:53 |  |
