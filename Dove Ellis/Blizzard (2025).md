---
title: "Blizzard"
artist: "Dove Ellis"
year: 2025
tidal_id: 467460858
tags:
  - Folk
  - Folkrock
rating:
---

# Blizzard
**Artist:** Dove Ellis
**Year:** 2025

![[_covers/Dove Ellis - Blizzard.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/467460858
```
^button-cdkq
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Dove%20Ellis%20Blizzard
```
^button-7nz9

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
| 1 | Little Left Hope | 4:19 |  |
| 2 | Pale Song | 2:45 |  |
| 3 | Love Is | 3:08 |  |
| 4 | When You Tie Your Hair Up | 4:28 |  |
| 5 | Jaundice | 2:03 |  |
| 6 | Heaven Has No Wings | 2:50 |  |
| 7 | It Is a Blizzard | 2:36 |  |
| 8 | Feathers, Cash | 4:27 |  |
| 9 | To the Sandals | 4:08 |  |
| 10 | Away You Stride | 3:44 |  |
