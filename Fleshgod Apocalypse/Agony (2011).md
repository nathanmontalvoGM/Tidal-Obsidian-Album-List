---
title: "Agony"
artist: "Fleshgod Apocalypse"
year: 2011
tidal_id: 106183274
tags:
  - Technicaldeathmetal
  - Progdeathmetal
  - Symphonicmetal
  - Brutaldeathmetal
rating:
---

# Agony
**Artist:** Fleshgod Apocalypse
**Year:** 2011

![[_covers/Fleshgod Apocalypse - Agony.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/106183274
```
^button-5pj1
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Fleshgod%20Apocalypse%20Agony
```
^button-rfkn

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
| 1 | Temptation | 1:47 |  |
| 2 | The Hypocrisy | 5:31 |  |
| 3 | The Imposition | 4:58 |  |
| 4 | The Deceit | 6:03 |  |
| 5 | The Violation | 4:18 |  |
| 6 | The Egoism | 6:22 |  |
| 7 | The Betrayal | 5:31 |  |
| 8 | The Forsaking | 5:37 |  |
| 9 | The Oppression | 6:04 |  |
| 10 | Agony | 3:34 |  |
