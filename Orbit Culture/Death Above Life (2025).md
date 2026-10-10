---
title: "Death Above Life"
artist: "Orbit Culture"
year: 2025
tidal_id: 436143039
tags:
  - Mathmetal
  - Groovemetal
  - MelodicDeathGroove
  - Bestalbums2025
rating:
---

# Death Above Life
**Artist:** Orbit Culture
**Year:** 2025

![[_covers/Orbit Culture - Death Above Life.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/436143039
```
^button-s7im
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Orbit%20Culture%20Death%20Above%20Life
```
^button-5ki2

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
| 1 | Inferna | 6:45 |  |
| 2 | Bloodhound | 5:04 |  |
| 3 | Inside the Waves | 4:39 |  |
| 4 | The Tales of War | 5:10 |  |
| 5 | Hydra | 4:49 |  |
| 6 | Nerve | 5:54 |  |
| 7 | Death Above Life | 5:31 |  |
| 8 | The Storm | 4:15 |  |
| 9 | Neural Collapse | 6:21 |  |
| 10 | The Path I Walk | 4:56 |  |
| 11 | Nuclear God | 5:09 |  |
