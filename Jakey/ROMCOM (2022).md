---
title: "ROMCOM"
artist: "Jakey"
year: 2022
tidal_id: 261177665
tags:
  - Cloudrap
  - Altpop
  - Poprap
  - Rap
rating:
---

# ROMCOM
**Artist:** Jakey
**Year:** 2022

![[_covers/Jakey - ROMCOM.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/261177665
```
^button-dp0l
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Jakey%20ROMCOM
```
^button-dj14

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
| 1 | Drive Off a Bridge | 3:21 |  |
| 2 | Like Totally Freak Me Out | 3:04 |  |
| 3 | Every Day | 3:11 |  |
| 4 | Survival Horror | 3:06 |  |
| 5 | Pine Barrens | 3:49 |  |
| 6 | Reeboks or the Nikes | 3:41 |  |
| 7 | Tommy Hanks | 3:05 |  |
| 8 | Fat Head | 4:36 |  |
