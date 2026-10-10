---
title: "Everlasting Flame"
artist: "Dreamtale"
year: 2022
tidal_id: 221641560
tags:
  - Numetal
rating:
---

# Everlasting Flame
**Artist:** Dreamtale
**Year:** 2022

![[_covers/Dreamtale - Everlasting Flame.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/221641560
```
^button-7ash
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Dreamtale%20Everlasting%20Flame
```
^button-2hxt

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
| 1 | King of Kings | 4:52 |  |
| 2 | Blood of the Morning Star | 5:25 |  |
| 3 | Last Goodbyes | 3:21 |  |
| 4 | Ghostride | 6:09 |  |
| 5 | Immortal Souls | 4:59 |  |
| 6 | No Shadow Goes Too Far | 4:33 |  |
| 7 | Summer Rose | 3:50 |  |
| 8 | The Glory | 3:55 |  |
| 9 | Eye for an Eye | 4:44 |  |
| 10 | Lady Dragon (2022) | 5:04 |  |
| 11 | Silent Scream | 4:06 |  |
| 12 | Tanhupullo | 2:32 |  |
| 13 | Sleeping Beauty (2022) | 4:49 |  |
| 14 | Pirates' Lullaby | 2:17 |  |
