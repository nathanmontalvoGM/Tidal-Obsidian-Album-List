---
title: "Neotheater"
artist: "AJR"
year: 2019
tidal_id: 481866853
tags:
  - Fire
  - Pop
  - Indie
  - Indiepop
rating:
---

# Neotheater
**Artist:** AJR
**Year:** 2019

![[_covers/AJR - Neotheater.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/481866853
```
^button-lx6k
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=AJR%20Neotheater
```
^button-be31

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
| 1 | Next Up Forever | 4:16 |  |
| 2 | Birthday Party | 3:43 |  |
| 3 | 100 Bad Days | 3:32 |  |
| 4 | Don’t Throw Out My Legos | 4:10 |  |
| 5 | Break My Face | 3:46 |  |
| 6 | Turning Out, Pt. II | 3:43 |  |
| 7 | The Entertainment’s Here | 3:07 |  |
| 8 | Karma | 4:05 |  |
| 9 | Beats | 3:18 |  |
| 10 | Wow, I’m Not Crazy | 3:16 |  |
| 11 | Dear Winter | 2:48 |  |
| 12 | Finale (Can’t Wait to See What You Do Next) | 4:37 |  |
