---
title: "Rakshak"
artist: "Bloodywood"
year: 2022
tidal_id: 240085301
tags:
  - FolkMetal
  - Numetal
  - Groovemetal
  - Bhangra
rating:
---

# Rakshak
**Artist:** Bloodywood
**Year:** 2022

![[_covers/Bloodywood - Rakshak.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/240085301
```
^button-eq2l
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Bloodywood%20Rakshak
```
^button-tirq

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
| 1 | Gaddaar | 4:44 |  |
| 2 | Aaj | 5:00 |  |
| 3 | Zanjeero Se | 4:11 |  |
| 4 | Machi Bhasad (album version) | 4:00 |  |
| 5 | Dana-Dan | 4:54 |  |
| 6 | Jee Veerey (album version) | 4:38 |  |
| 7 | Endurant (album version) | 4:46 |  |
| 8 | Yaad (album version) | 5:40 |  |
| 9 | BSDK.exe | 4:55 |  |
| 10 | Chakh Le | 4:25 |  |
