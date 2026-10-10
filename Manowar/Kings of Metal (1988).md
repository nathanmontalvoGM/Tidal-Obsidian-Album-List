---
title: "Kings of Metal"
artist: "Manowar"
year: 1988
tidal_id: 3467185
tags:
  - Heavymetal
  - Powermetal
  - Truemetal
  - Numetal
rating:
---

# Kings of Metal
**Artist:** Manowar
**Year:** 1988

![[_covers/Manowar - Kings of Metal.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/3467185
```
^button-37fu
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Manowar%20Kings%20of%20Metal
```
^button-lrbg

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
| 1 | Wheels of Fire | 4:10 |  |
| 2 | Kings of Metal | 3:45 |  |
| 3 | Heart of Steel | 5:10 |  |
| 4 | Sting of the Bumblebee | 2:49 |  |
| 5 | The Crown and the Ring (Lament of the Kings) | 4:50 |  |
| 6 | Kingdom Come | 3:56 |  |
| 7 | Pleasure Slave | 5:38 |  |
| 8 | Hail and Kill | 5:58 |  |
| 9 | The Warrior's Prayer | 4:20 |  |
| 10 | Blood of the Kings | 7:29 |  |
