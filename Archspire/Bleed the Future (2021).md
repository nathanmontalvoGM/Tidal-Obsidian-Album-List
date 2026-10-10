---
title: "Bleed the Future"
artist: "Archspire"
year: 2021
tidal_id: 189677757
tags:
  - Technicaldeathmetal
  - Mathmetal
  - Topmetalalbumsofthedecade20202029
  - Numetal
rating:
---

# Bleed the Future
**Artist:** Archspire
**Year:** 2021

![[_covers/Archspire - Bleed the Future.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/189677757
```
^button-0ugm
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Archspire%20Bleed%20the%20Future
```
^button-rbcp

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
| 1 | Drone Corpse Aviator | 3:46 |  |
| 2 | Golden Mouth of Ruin | 4:05 |  |
| 3 | Abandon the Linear | 4:36 |  |
| 4 | Bleed the Future | 3:48 |  |
| 5 | Drain of Incarnation | 4:20 |  |
| 6 | Acrid Canon | 4:09 |  |
| 7 | Reverie on the Onyx | 3:47 |  |
| 8 | A.U.M. | 3:04 |  |
