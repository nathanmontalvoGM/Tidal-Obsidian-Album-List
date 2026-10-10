---
title: "Too Fast to Die"
artist: "Archspire"
year: 2026
tidal_id: 475956275
tags:
  - Technicaldeathmetal
rating:
---

# Too Fast to Die
**Artist:** Archspire
**Year:** 2026

![[_covers/Archspire - Too Fast to Die.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/475956275
```
^button-0fza
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Archspire%20Too%20Fast%20to%20Die
```
^button-8csu

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
| 1 | Liminal Cypher | 5:17 |  |
| 2 | Red Goliath | 5:02 |  |
| 3 | Carrion Ladder | 4:24 |  |
| 4 | Anomalous Descent | 4:14 |  |
| 5 | The Vessel | 4:41 |  |
| 6 | Limb of Leviticus | 5:43 |  |
| 7 | Deadbolt the Backward | 4:33 |  |
| 8 | Too Fast to Die | 5:32 |  |
