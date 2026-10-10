---
title: "Silver Romance"
artist: "Freedom Call"
year: 2024
tidal_id: 344172738
tags:
  - Numetal
rating:
---

# Silver Romance
**Artist:** Freedom Call
**Year:** 2024

![[_covers/Freedom Call - Silver Romance.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/344172738
```
^button-uq25
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Freedom%20Call%20Silver%20Romance
```
^button-gro4

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
| 1 | Silver Romance | 4:07 |  |
| 2 | Symphony of Avalon | 4:05 |  |
| 3 | Supernova | 3:55 |  |
| 4 | Infinity | 4:22 |  |
| 5 | Out of Space | 3:23 |  |
| 6 | Distant Horizon | 4:14 |  |
| 7 | In Quest of Love | 4:34 |  |
| 8 | Blue Giant | 3:51 |  |
| 9 | Meteorite | 3:02 |  |
| 10 | Big Bang Universe | 4:36 |  |
| 11 | New Haven | 3:54 |  |
| 12 | High Above | 4:01 |  |
| 13 | Metal Generation | 4:51 |  |
