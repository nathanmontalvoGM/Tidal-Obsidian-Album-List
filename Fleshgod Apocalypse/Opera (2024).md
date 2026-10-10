---
title: "Opera"
artist: "Fleshgod Apocalypse"
year: 2024
tidal_id: 364925432
tags:
  - Mathmetal
  - Symphonicmetal
  - Extrememetal
  - Numetal
rating:
---

# Opera
**Artist:** Fleshgod Apocalypse
**Year:** 2024

![[_covers/Fleshgod Apocalypse - Opera.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/364925432
```
^button-ebl0
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Fleshgod%20Apocalypse%20Opera
```
^button-2s7h

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
| 1 | Ode to Art (de' sepolcri) | 2:18 |  |
| 2 | I Can Never Die | 4:30 |  |
| 3 | Pendulum | 3:58 |  |
| 4 | Bloodclock | 5:14 |  |
| 5 | At War With My Soul | 5:06 |  |
| 6 | Morphine Waltz | 3:36 |  |
| 7 | Matricide 8.21 | 5:35 |  |
| 8 | Per aspera ad astra | 4:48 |  |
| 9 | Till Death Do Us Part | 5:31 |  |
| 10 | Opera | 2:44 |  |
