---
title: The Skies Above Eternity
artist: Fellowship
year: 2024
tidal_id: 387780013
tags:
  - Powermetal
  - Symphonicmetal
rating:
---

# The Skies Above Eternity
**Artist:** Fellowship
**Year:** 2024

![[_covers/Fellowship - The Skies Above Eternity.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/387780013
```
^button-8usy
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Fellowship%20The%20Skies%20Above%20Eternity
```
^button-wnk0

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
| 1 | Hold Up Your Hearts (Again) | 4:48 |  |
| 2 | Victim | 5:23 |  |
| 3 | The Bitter Winds | 5:30 |  |
| 4 | Dawnbreaker | 5:18 |  |
| 5 | Eternity | 4:38 |  |
| 6 | King of Nothing | 4:12 |  |
| 7 | World End Slowly | 4:32 |  |
| 8 | A New Hope | 4:32 |  |
| 9 | Memories on the Wind | 2:00 |  |
| 10 | Iron Eyes | 6:23 |  |
