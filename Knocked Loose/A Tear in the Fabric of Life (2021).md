---
title: "A Tear in the Fabric of Life"
artist: "Knocked Loose"
year: 2021
tidal_id: 198547249
tags:
  - Metalcore
  - Hardcore
  - HardcorePunk
  - Numetal
rating:
---

# A Tear in the Fabric of Life
**Artist:** Knocked Loose
**Year:** 2021

![[_covers/Knocked Loose - A Tear in the Fabric of Life.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/198547249
```
^button-fhok
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Knocked%20Loose%20A%20Tear%20in%20the%20Fabric%20of%20Life
```
^button-eawv

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
| 1 | Where Light Divides the Holler | 3:42 |  |
| 2 | God Knows | 3:35 |  |
| 3 | Forced to Stay | 3:55 |  |
| 4 | Contorted in the Faille | 3:55 |  |
| 5 | Return to Passion | 1:13 |  |
| 6 | Permanent | 4:42 |  |
