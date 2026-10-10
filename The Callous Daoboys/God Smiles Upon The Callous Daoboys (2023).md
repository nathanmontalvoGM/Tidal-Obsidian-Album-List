---
title: "God Smiles Upon The Callous Daoboys"
artist: "The Callous Daoboys"
year: 2023
tidal_id: 333675455
tags:
  - Mathcore
  - Numetal
  - Metalcore
  - Posthardcore
rating:
---

# God Smiles Upon The Callous Daoboys
**Artist:** The Callous Daoboys
**Year:** 2023

![[_covers/The Callous Daoboys - God Smiles Upon The Callous Daoboys.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/333675455
```
^button-0hwz
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=The%20Callous%20Daoboys%20God%20Smiles%20Upon%20The%20Callous%20Daoboys
```
^button-8jdt

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
| 1 | Pushing the Pink Envelope | 4:11 |  |
| 2 | Waco Jesus | 3:41 |  |
| 3 | Designer Shroud of Turin | 5:26 |  |
