---
title: "Prelude to Ecstasy"
artist: "The Last Dinner Party"
year: 2024
tidal_id: 342043044
tags:
  - Indierock
  - Glamrock
  - Poprock
  - Chamberpop
rating:
---

# Prelude to Ecstasy
**Artist:** The Last Dinner Party
**Year:** 2024

![[_covers/The Last Dinner Party - Prelude to Ecstasy.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/342043044
```
^button-dl94
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=The%20Last%20Dinner%20Party%20Prelude%20to%20Ecstasy
```
^button-6f6r

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
| 1 | Prelude to Ecstasy | 1:36 |  |
| 2 | Burn Alive | 3:21 |  |
| 3 | Caesar on a TV Screen | 3:49 |  |
| 4 | The Feminine Urge | 3:26 |  |
| 5 | On Your Side | 4:27 |  |
| 6 | Beautiful Boy | 3:47 |  |
| 7 | Gjuha | 1:29 |  |
| 8 | Sinner | 2:56 |  |
| 9 | My Lady of Mercy | 2:55 |  |
| 10 | Portrait of a Dead Girl | 4:57 |  |
| 11 | Nothing Matters | 3:02 |  |
| 12 | Mirror | 5:24 |  |
