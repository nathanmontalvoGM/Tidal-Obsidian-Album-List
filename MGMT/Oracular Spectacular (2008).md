---
title: "Oracular Spectacular"
artist: "MGMT"
year: 2008
tidal_id: 1317014
tags:
  - Indie
  - Electronicore
  - Alternativerock
  - Psychedelicpop
rating:
---

# Oracular Spectacular
**Artist:** MGMT
**Year:** 2008

![[_covers/MGMT - Oracular Spectacular.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/1317014
```
^button-zwcr
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=MGMT%20Oracular%20Spectacular
```
^button-7quc

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
| 1 | Time to Pretend | 4:21 |  |
| 2 | Weekend Wars | 4:10 |  |
| 3 | The Handshake | 3:39 |  |
| 4 | The Youth | 3:47 |  |
| 5 | Electric Feel | 3:49 |  |
| 6 | 4th Dimensional Transition | 3:58 |  |
| 7 | Pieces of What | 2:43 |  |
| 8 | Of Moons, Birds & Monsters | 4:46 |  |
| 9 | Kids | 5:03 |  |
| 10 | Future Reflections | 3:58 |  |
| 11 | Metanoia | 13:49 |  |
| 12 | Electric Feel (demo version) | 4:24 |  |
| 13 | Electric Feel (Justice remix) | 5:25 |  |
| 14 | Kids (Soulwax remix) | 5:39 |  |
