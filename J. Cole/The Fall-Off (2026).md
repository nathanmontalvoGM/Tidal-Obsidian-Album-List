---
title: "The Fall-Off"
artist: "J. Cole"
year: 2026
tidal_id: 496439179
tags:
  - Rap
  - Hiphop
  - Jcole
  - Boombap
rating:
---

# The Fall-Off
**Artist:** J. Cole
**Year:** 2026

![[_covers/J. Cole - The Fall-Off.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/496439179
```
^button-pbnt
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=J.%20Cole%20The%20Fall-Off
```
^button-oamv

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
| 1-1 | 29 Intro | 0:57 |  |
| 1-2 | Two Six | 3:16 |  |
| 1-3 | SAFETY | 5:18 |  |
| 1-4 | Run a Train | 4:02 |  |
| 1-5 | Poor Thang | 4:50 |  |
| 1-6 | Legacy | 3:55 |  |
| 1-7 | Bunce Road Blues | 5:10 |  |
| 1-8 | WHO TF IZ U | 4:37 |  |
| 1-9 | Drum n Bass | 4:14 |  |
| 1-10 | The Let Out | 4:14 |  |
| 1-11 | Bombs in the Ville / Hit the Gas | 4:06 |  |
| 1-12 | Lonely at the Top | 3:24 |  |
| 2-1 | 39 Intro | 6:06 |  |
| 2-2 | The Fall-Off is Inevitable | 2:56 |  |
| 2-3 | The Villest | 4:30 |  |
| 2-4 | Old Dog | 3:22 |  |
| 2-5 | Life Sentence | 4:12 |  |
| 2-6 | Only You | 4:46 |  |
| 2-7 | Man Up Above | 4:58 |  |
| 2-8 | I Love Her Again | 5:32 |  |
| 2-9 | What If | 5:19 |  |
| 2-10 | Quik Stop | 4:24 |  |
| 2-11 | and the whole world is the Ville | 4:35 |  |
| 2-12 | Ocean Way | 2:34 |  |
