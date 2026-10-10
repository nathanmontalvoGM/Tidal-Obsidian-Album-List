---
title: "Abyss"
artist: "Unleash The Archers"
year: 2020
tidal_id: 141536149
tags:
  - Powermetal
  - Numetal
  - Heavymetal
  - Rock
rating:
---

# Abyss
**Artist:** Unleash The Archers
**Year:** 2020

![[_covers/Unleash The Archers - Abyss.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/141536149
```
^button-6lm5
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Unleash%20The%20Archers%20Abyss
```
^button-0n9q

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
| 1 | Waking Dream | 3:45 |  |
| 2 | Abyss | 6:44 |  |
| 3 | Through Stars | 5:34 |  |
| 4 | Legacy | 5:26 |  |
| 5 | Return to Me | 5:34 |  |
| 6 | Soulbound | 3:54 |  |
| 7 | Faster Than Light | 5:11 |  |
| 8 | The Wind That Shapes the Land | 8:36 |  |
| 9 | Carry the Flame | 4:42 |  |
| 10 | Afterlife | 7:30 |  |
