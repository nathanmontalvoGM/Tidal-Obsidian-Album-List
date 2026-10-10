---
title: Blue Rev
artist: Alvvays
year: 2022
tidal_id: 256079079
tags:
  - Favorite
  - NoisePop
  - Indiepop
  - Shoegaze
  - DreamPop
rating:
---

# Blue Rev
**Artist:** Alvvays
**Year:** 2022

![[_covers/Alvvays - Blue Rev.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/256079079
```
^button-wwyx
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Alvvays%20Blue%20Rev
```
^button-3rpc

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

| #   | Title                | Duration | Rating /10 |
| --- | -------------------- | -------- | ---------- |
| 1   | Pharmacist           | 2:04     | 8          |
| 2   | Easy on Your Own?    | 2:55     | 10         |
| 3   | After the Earthquake | 3:05     | 7.5        |
| 4   | Tom Verlaine         | 3:26     |            |
| 5   | Pressed              | 2:10     |            |
| 6   | Many Mirrors         | 2:59     |            |
| 7   | Very Online Guy      | 2:22     |            |
| 8   | Velveteen            | 3:10     |            |
| 9   | Tile by Tile         | 2:58     |            |
| 10  | Pomeranian Spinster  | 3:25     |            |
| 11  | Belinda Says         | 2:45     |            |
| 12  | Bored in Bristol     | 3:00     |            |
| 13  | Lottery Noises       | 3:18     |            |
| 14  | Fourth Figure        | 1:20     |            |
