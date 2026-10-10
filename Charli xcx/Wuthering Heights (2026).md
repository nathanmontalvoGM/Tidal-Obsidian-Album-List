---
title: "Wuthering Heights"
artist: "Charli xcx"
year: 2026
tidal_id: 497934606
tags:
  - Synthpop
  - ArtPop
  - Classicalcrossover
  - Neoclassicaldarkwave
rating:
---

# Wuthering Heights
**Artist:** Charli xcx
**Year:** 2026

![[_covers/Charli xcx - Wuthering Heights.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/497934606
```
^button-hwhz
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Charli%20xcx%20Wuthering%20Heights
```
^button-h0if

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
| 1 | House | 3:15 |  |
| 2 | Wall of Sound | 2:24 |  |
| 3 | Dying for You | 3:02 |  |
| 4 | Always Everywhere | 3:03 |  |
| 5 | Chains of Love | 2:50 |  |
| 6 | Out of Myself | 2:19 |  |
| 7 | Open up | 1:26 |  |
| 8 | Seeing Things | 2:30 |  |
| 9 | Altars | 2:56 |  |
| 10 | Eyes of the World | 3:44 |  |
| 11 | My Reminder | 3:33 |  |
| 12 | Funny Mouth | 3:33 |  |
