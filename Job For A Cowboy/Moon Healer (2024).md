---
title: "Moon Healer"
artist: "Job For A Cowboy"
year: 2024
tidal_id: 313871734
tags:
  - Progressivemetal
  - Technicaldeathmetal
rating:
---

# Moon Healer
**Artist:** Job For A Cowboy
**Year:** 2024

![[_covers/Job For A Cowboy - Moon Healer.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/313871734
```
^button-uj8b
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Job%20For%20A%20Cowboy%20Moon%20Healer
```
^button-syby

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
| 1 | Beyond the Chemical Doorway | 4:10 |  |
| 2 | Etched in Oblivion | 4:14 |  |
| 3 | Grinding Wheels of Ophanim | 5:52 |  |
| 4 | The Sun Gave Me Ashes So I Sought Out the Moon | 4:03 |  |
| 5 | Into the Crystalline Crypts | 4:21 |  |
| 6 | A Sorrow‐Filled Moon | 5:37 |  |
| 7 | The Agony Seeping Storm | 4:11 |  |
| 8 | The Forever Rot | 6:40 |  |
