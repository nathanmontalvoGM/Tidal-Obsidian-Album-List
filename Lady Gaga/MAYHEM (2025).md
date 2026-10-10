---
title: "MAYHEM"
artist: "Lady Gaga"
year: 2025
tidal_id: 421850005
tags:
  - Electropop
  - Pop
  - Dancepop
  - Synthpop
rating:
---

# MAYHEM
**Artist:** Lady Gaga
**Year:** 2025

![[_covers/Lady Gaga - MAYHEM.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/421850005
```
^button-uj8x
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Lady%20Gaga%20MAYHEM
```
^button-i68z

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
| 1-1 | Disease | 3:49 |  |
| 1-2 | Abracadabra | 3:43 |  |
| 1-3 | Garden of Eden | 3:59 |  |
| 1-4 | Perfect Celebrity | 3:49 |  |
| 1-5 | Vanish Into You | 4:04 |  |
| 1-6 | Killah | 3:30 |  |
| 1-7 | Zombieboy | 3:33 |  |
| 1-8 | LoveDrug | 3:13 |  |
| 1-9 | How Bad Do U Want Me | 3:58 |  |
| 1-10 | Don’t Call Tonight | 3:45 |  |
| 2-1 | Shadow of a Man | 3:19 |  |
| 2-2 | The Beast | 3:54 |  |
| 2-3 | Blade of Grass | 4:17 |  |
| 2-4 | Die With a Smile | 4:11 |  |
