---
title: "Bat Out Of Hell"
artist: "Meat Loaf"
year: 1977
tidal_id: 61126687
tags:
  - Rock
  - Classicrock
  - 70s
  - Hardrock
rating:
---

# Bat Out Of Hell
**Artist:** Meat Loaf
**Year:** 1977

![[_covers/Meat Loaf - Bat Out Of Hell.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/61126687
```
^button-rhoz
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Meat%20Loaf%20Bat%20Out%20Of%20Hell
```
^button-s100

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
| 1-1 | Bat Out of Hell | 9:50 |  |
| 1-2 | You Took the Words Right Out of My Mouth (Hot Summer Night) | 5:04 |  |
| 1-3 | Heaven Can Wait | 4:41 |  |
| 1-4 | All Revved Up With No Place to Go | 4:19 |  |
| 1-5 | Two Out of Three Ain’t Bad | 5:25 |  |
| 1-6 | Paradise by the Dashboard Light | 8:29 |  |
| 1-7 | For Crying Out Loud | 8:46 |  |
| 1-8 | Great Boleros of Fire (live intro) (live, 1978‐09‐01: Nassau Coliseum, Hempstead, Long Island, NY) | 3:48 |  |
| 1-9 | Bat Out of Hell (live, 1978‐09‐01: Nassau Coliseum, Hempstead, Long Island, NY) | 11:09 |  |
| 2-1 | Bat Out of Hell (5.1 mix) | 9:50 |  |
| 2-2 | You Took the Words Right Out of My Mouth (Hot Summer Night) (5.1 mix) | 5:04 |  |
| 2-3 | Heaven Can Wait (5.1 mix) | 4:41 |  |
| 2-4 | All Revved Up With No Place to Go (5.1 mix) | 4:19 |  |
| 2-5 | Two Out of Three Ain’t Bad (5.1 mix) | 5:25 |  |
| 2-6 | Paradise by the Dashboard Light (5.1 mix) | 8:29 |  |
| 2-7 | For Crying Out Loud (5.1 mix) | 8:46 |  |
| 2-8 | Great Boleros of Fire (live intro) (live, 1978‐09‐01: Nassau Coliseum, Hempstead, Long Island, NY) (5.1 mix) | 3:48 |  |
| 2-9 | Bat Out of Hell (live, 1978‐09‐01: Nassau Coliseum, Hempstead, Long Island, NY) (5.1 mix) | 11:09 |  |
