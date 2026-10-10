---
title: "Ashen"
artist: "Humanity's Last Breath"
year: 2023
tidal_id: 283523407
tags:
  - Mathmetal
  - Deathcore
  - Heavymetal
rating:
---

# Ashen
**Artist:** Humanity's Last Breath
**Year:** 2023

![[_covers/Humanity's Last Breath - Ashen.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/283523407
```
^button-nb6p
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Humanity%27s%20Last%20Breath%20Ashen
```
^button-j5e7

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
| 1 | Blood Spilled | 5:00 |  |
| 2 | Linger | 3:59 |  |
| 3 | Lifeless, Deathless | 3:56 |  |
| 4 | Withering | 4:05 |  |
| 5 | Instill | 4:42 |  |
| 6 | Labyrinthian | 4:01 |  |
| 7 | Catastrophize | 4:10 |  |
| 8 | Death Spiral | 4:24 |  |
| 9 | Shell | 3:58 |  |
| 10 | Passage | 4:14 |  |
| 11 | Burden | 1:15 |  |
| 12 | Bearer | 3:47 |  |
