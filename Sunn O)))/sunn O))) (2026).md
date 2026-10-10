---
title: "sunn O)))"
artist: "Sunn O)))"
year: 2026
tidal_id: 487713580
tags:
  - DroneMetal
  - Numetal
rating:
---

# sunn O)))
**Artist:** Sunn O)))
**Year:** 2026

![[_covers/Sunn O))) - sunn O))).jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/487713580
```
^button-hyt1
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Sunn%20O%29%29%29%20sunn%20O%29%29%29
```
^button-v2hg

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
| 1 | XXANN | 18:21 |  |
| 2 | Does Anyone Hear Like Venom? | 7:33 |  |
| 3 | Butch’s Guns | 14:12 |  |
| 4 | Mindrolling | 18:12 |  |
| 5 | Everett Moses | 10:54 |  |
| 6 | Glory Black | 10:25 |  |
