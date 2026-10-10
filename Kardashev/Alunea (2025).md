---
title: "Alunea"
artist: "Kardashev"
year: 2025
tidal_id: 406476717
tags:
  - Deathgaze
  - Progressivemetal
  - Atmosphericmetal
  - Progdeathmetal
rating:
---

# Alunea
**Artist:** Kardashev
**Year:** 2025

![[_covers/Kardashev - Alunea.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/406476717
```
^button-lheq
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Kardashev%20Alunea
```
^button-fvgy

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
| 1 | A Precipice. A Door. | 4:59 |  |
| 2 | Reunion | 4:52 |  |
| 3 | Seed of the Night | 5:18 |  |
| 4 | Speak Silence | 5:01 |  |
| 5 | Truth to Form | 5:23 |  |
| 6 | Edge of Forever | 5:24 |  |
| 7 | We Could Fold the Stars | 5:09 |  |
| 8 | Below Sun & Soil | 6:00 |  |
