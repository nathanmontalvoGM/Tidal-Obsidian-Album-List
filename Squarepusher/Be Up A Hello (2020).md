---
title: "Be Up A Hello"
artist: "Squarepusher"
year: 2020
tidal_id: 128786247
tags:
  - Idm
  - Instrumental
  - Electronicore
  - DrillandBass
rating:
---

# Be Up A Hello
**Artist:** Squarepusher
**Year:** 2020

![[_covers/Squarepusher - Be Up A Hello.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/128786247
```
^button-jzno
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Squarepusher%20Be%20Up%20A%20Hello
```
^button-qrsy

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
| 1 | Oberlove | 3:52 |  |
| 2 | Hitsonu | 4:13 |  |
| 3 | Nervelevers | 5:29 |  |
| 4 | Speedcrank | 5:53 |  |
| 5 | Detroit People Mover | 4:20 |  |
| 6 | Vortrack | 5:27 |  |
| 7 | Terminal Slam | 4:56 |  |
| 8 | Mekrev Bass | 7:11 |  |
| 9 | 80 Ondula | 5:47 |  |
