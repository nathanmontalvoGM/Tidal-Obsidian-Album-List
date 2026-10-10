---
title: Trench
artist: twenty one pilots
year: 2018
tidal_id: 96027021
tags:
  - Favorite
  - Indiepop
  - Alternativerock
  - Rock
  - Indietronica
rating: "8.4"
---

# Trench
**Artist:** twenty one pilots
**Year:** 2018

![[_covers/twenty one pilots - Trench.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/96027021
```
^button-qeto
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=twenty%20one%20pilots%20Trench
```
^button-tw94

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

| #   | Title               | Duration | Rating /10 |
| --- | ------------------- | -------- | ---------- |
| 1-1 | Jumpsuit            | 3:59     | 10         |
| 1-2 | Levitate            | 2:26     | 10         |
| 1-3 | Morph               | 4:19     | 10         |
| 1-4 | My Blood            | 3:49     | 10         |
| 1-5 | Chlorine            | 5:24     | 9.5        |
| 1-6 | Smithereens         | 2:57     | 6          |
| 1-7 | Neon Gravestones    | 4:00     | 8.5        |
| 2-1 | The Hype            | 4:25     | 8          |
| 2-2 | Nico and the Niners | 3:45     | 7.5        |
| 2-3 | Cut My Lip          | 4:43     | 7          |
| 2-4 | Bandito             | 5:31     | 6.5        |
| 2-5 | Pet Cheetah         | 3:18     | 9          |
| 2-6 | Legend              | 2:53     | 7          |
| 2-7 | Leave the City      | 4:40     | 8          |
