---
title: "Alien"
artist: "Strapping Young Lad"
year: 2005
tidal_id: 52000194
tags:
  - Industrialmetal
  - Progressivemetal
  - Progdeathmetal
  - Thrashmetal
rating:
---

# Alien
**Artist:** Strapping Young Lad
**Year:** 2005

![[_covers/Strapping Young Lad - Alien.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/52000194
```
^button-kqim
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Strapping%20Young%20Lad%20Alien
```
^button-w8uy

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
| 1 | Imperial | 2:17 |  |
| 2 | Skeksis | 6:42 |  |
| 3 | Shitstorm | 4:22 |  |
| 4 | Love? | 4:53 |  |
| 5 | Shine | 5:13 |  |
| 6 | We Ride | 2:37 |  |
| 7 | Possessions | 4:12 |  |
| 8 | Two Weeks | 3:28 |  |
| 9 | Thalamus | 3:58 |  |
| 10 | Zen | 5:02 |  |
| 11 | Info Dump | 11:56 |  |
