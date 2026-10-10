---
title: "Das Album"
artist: "We Butter The Bread With Butter"
year: 2021
tidal_id: 187437362
tags:
  - German
  - Metalcore
  - Album
  - Deathcore
rating:
---

# Das Album
**Artist:** We Butter The Bread With Butter
**Year:** 2021

![[_covers/We Butter The Bread With Butter - Das Album.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/187437362
```
^button-bbsr
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=We%20Butter%20The%20Bread%20With%20Butter%20Das%20Album
```
^button-158t

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
| 1 | Das Album Intro | 1:03 |  |
| 2 | Dreh auf! | 3:02 |  |
| 3 | 20 km/h | 3:11 |  |
| 4 | N!CE | 3:06 |  |
| 5 | Schreibwarenfachverkäufer | 3:33 |  |
| 6 | Läuft | 2:36 |  |
| 7 | Jump 'n' Run | 3:50 |  |
| 8 | Sprich sie einfach an | 2:49 |  |
| 9 | Meine Finger sind zu klein | 4:00 |  |
| 10 | Piks mich | 3:49 |  |
| 11 | Metal | 3:24 |  |
| 12 | Angriff der Dönerteller | 3:37 |  |
| 13 | Letzter Song | 3:22 |  |
