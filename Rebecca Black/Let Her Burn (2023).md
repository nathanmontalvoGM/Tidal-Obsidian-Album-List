---
title: "Let Her Burn"
artist: "Rebecca Black"
year: 2023
tidal_id: 270325285
tags:
  - Electropop
  - Vinyl
  - Pop
  - Alternativerock
rating:
---

# Let Her Burn
**Artist:** Rebecca Black
**Year:** 2023

![[_covers/Rebecca Black - Let Her Burn.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/270325285
```
^button-4xcf
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Rebecca%20Black%20Let%20Her%20Burn
```
^button-e4kd

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
| 1 | Erase You | 3:17 |  |
| 2 | Destroy Me | 3:02 |  |
| 3 | Misery Loves Company | 2:49 |  |
| 4 | Crumbs | 3:13 |  |
| 5 | Doe Eyed | 2:35 |  |
| 6 | Sick to My Stomach | 4:14 |  |
| 7 | What Am I Gonna Do With You | 2:38 |  |
| 8 | Cry Hard Enough | 2:49 |  |
| 9 | Look at You | 2:44 |  |
| 10 | Performer | 3:14 |  |
