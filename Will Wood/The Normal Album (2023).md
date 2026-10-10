---
title: "The Normal Album"
artist: "Will Wood"
year: 2023
tidal_id: 199347397
tags:
  - Pianorock
  - Darkcabaret
  - Progressivepop
  - Indiepop
rating:
---

# The Normal Album
**Artist:** Will Wood
**Year:** 2023

![[_covers/Will Wood - The Normal Album.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/199347397
```
^button-qp89
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Will%20Wood%20The%20Normal%20Album
```
^button-c51g

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
| 1 | Suburbia Overture / Greetings from Mary Bell Township! / (Vampire) Culture / Love Me, Normally | 6:16 |  |
| 2 | 2econd 2ight 2eer (that was fun, goodbye.) | 3:26 |  |
| 3 | Laplace’s Angel (Hurt People? Hurt People!) | 4:01 |  |
| 4 | I / Me / Myself | 4:51 |  |
| 5 | …well, better than the alternative | 4:14 |  |
| 6 | Outliars and Hyppocrates: a fun fact about apples | 4:12 |  |
| 7 | BlackBoxWarrior (OKULTRA) | 4:54 |  |
| 8 | Marsha, Thankk You for the Dialectics, but I Need You to Leave | 5:19 |  |
| 9 | Love, Me Normally | 5:44 |  |
| 10 | Memento Mori: the most important thing in the world | 2:49 |  |
