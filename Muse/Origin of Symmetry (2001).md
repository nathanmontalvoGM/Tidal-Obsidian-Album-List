---
title: "Origin of Symmetry"
artist: "Muse"
year: 2001
tidal_id: 68728981
tags:
  - Alternativerock
  - Rock
  - Muse
  - Progressivepop
rating:
---

# Origin of Symmetry
**Artist:** Muse
**Year:** 2001

![[_covers/Muse - Origin of Symmetry.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/68728981
```
^button-nwxt
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Muse%20Origin%20of%20Symmetry
```
^button-i8gf

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
| 1 | New Born | 6:03 |  |
| 2 | Bliss | 4:12 |  |
| 3 | Space Dementia | 6:20 |  |
| 4 | Hyper Music | 3:20 |  |
| 5 | Plug In Baby | 3:40 |  |
| 6 | Citizen Erased | 7:19 |  |
| 7 | Micro Cuts | 3:38 |  |
| 8 | Screenager | 4:20 |  |
| 9 | Darkshines | 4:47 |  |
| 10 | Feeling Good | 3:19 |  |
| 11 | Megalomania | 4:38 |  |
