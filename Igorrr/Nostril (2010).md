---
title: "Nostril"
artist: "Igorrr"
year: 2010
tidal_id: 142885907
tags:
  - Breakcore
  - Idm
  - Electronicore
  - Experimentalrock
rating:
---

# Nostril
**Artist:** Igorrr
**Year:** 2010

![[_covers/Igorrr - Nostril.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/142885907
```
^button-68sp
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Igorrr%20Nostril
```
^button-8o4v

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
| 1 | Double Monk | 2:56 |  |
| 2 | Tendon | 4:29 |  |
| 3 | Excessive Funeral | 3:29 |  |
| 4 | Very Long Chicken | 3:30 |  |
| 5 | Melting Nails | 2:39 |  |
| 6 | Pavor nocturnus | 4:21 |  |
| 7 | Caros | 0:51 |  |
| 8 | Cruciform Dachshund | 3:42 |  |
| 9 | Half a Pony | 2:23 |  |
| 10 | Unpleasant Sonata | 2:14 |  |
| 11 | Dentist | 0:43 |  |
| 12 | Fryzura konika | 2:50 |  |
| 13 | Veins | 4:28 |  |
| 14 | Moldy Eye | 4:26 |  |
