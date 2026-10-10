---
title: "Connla's Well"
artist: "Maruja"
year: 2024
tidal_id: 355101345
tags:
  - Postrock
  - Postpunk
  - Artpunk
  - Jazzrock
rating:
---

# Connla's Well
**Artist:** Maruja
**Year:** 2024

![[_covers/Maruja - Connla's Well.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/355101345
```
^button-wxfj
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Maruja%20Connla%27s%20Well
```
^button-pnm7

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
| 1 | Connla’s Well | 1:52 |  |
| 2 | The Invisible Man | 6:05 |  |
| 3 | Zeitgeist | 3:02 |  |
| 4 | One Hand Behind the Devil | 4:09 |  |
| 5 | Resisting Resistance | 5:58 |  |
