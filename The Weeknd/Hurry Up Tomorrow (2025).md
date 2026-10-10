---
title: "Hurry Up Tomorrow"
artist: "The Weeknd"
year: 2025
tidal_id: 414851656
tags:
  - Synthwave
  - Synthpop
  - Alternativerandb
  - Pop
rating:
---

# Hurry Up Tomorrow
**Artist:** The Weeknd
**Year:** 2025

![[_covers/The Weeknd - Hurry Up Tomorrow.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/414851656
```
^button-qwk2
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=The%20Weeknd%20Hurry%20Up%20Tomorrow
```
^button-liiq

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
| 1 | Wake Me Up | 5:08 |  |
| 2 | Cry for Me | 3:44 |  |
| 3 | I Can’t F****g Sing | 0:12 |  |
| 4 | São Paulo | 5:01 |  |
| 5 | Until We’re Skin & Bones | 0:22 |  |
| 6 | Baptized in Fear | 3:52 |  |
| 7 | Open Hearts | 3:54 |  |
| 8 | Opening Night | 1:36 |  |
| 9 | Reflections Laughing | 4:51 |  |
| 10 | Enjoy the Show | 5:01 |  |
| 11 | Given Up on Me | 5:54 |  |
| 12 | I Can’t Wait to Get There | 3:08 |  |
| 13 | Timeless | 4:16 |  |
| 14 | Niagara Falls | 4:37 |  |
| 15 | Take Me Back to LA | 4:13 |  |
| 16 | Big Sleep | 3:45 |  |
| 17 | Give Me Mercy | 3:36 |  |
| 18 | Drive | 3:08 |  |
| 19 | The Abyss | 4:42 |  |
| 20 | Red Terror | 3:51 |  |
| 21 | Without a Warning | 4:57 |  |
| 22 | Hurry Up Tomorrow | 4:51 |  |
