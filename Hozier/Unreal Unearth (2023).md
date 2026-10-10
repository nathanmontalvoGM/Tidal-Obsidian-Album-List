---
title: "Unreal Unearth"
artist: "Hozier"
year: 2023
tidal_id: 310756333
tags:
  - Folk
  - Blues
  - Rock
  - Souk
rating:
---

# Unreal Unearth
**Artist:** Hozier
**Year:** 2023

![[_covers/Hozier - Unreal Unearth.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/310756333
```
^button-uzh1
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Hozier%20Unreal%20Unearth
```
^button-kp4n

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
| 1 | De Selby (Part 1) | 3:40 |  |
| 2 | De Selby (Part 2) | 3:48 |  |
| 3 | First Time | 3:53 |  |
| 4 | Francesca | 4:30 |  |
| 5 | I, Carrion (Icarian) | 3:17 |  |
| 6 | Eat Your Young | 4:04 |  |
| 7 | Damage Gets Done | 4:29 |  |
| 8 | Who We Are | 4:06 |  |
| 9 | Son of Nyx | 3:19 |  |
| 10 | All Things End | 3:37 |  |
| 11 | To Someone From a Warm Climate (Uiscefhuaraithe) | 4:01 |  |
| 12 | Butchered Tongue | 2:30 |  |
| 13 | Anything But | 3:45 |  |
| 14 | Abstract (Psychopomp) | 4:04 |  |
| 15 | Unknown / Nth | 4:40 |  |
| 16 | First Light | 4:52 |  |
