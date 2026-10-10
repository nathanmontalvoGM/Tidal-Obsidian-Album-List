---
title: "Images and Words"
artist: "Dream Theater"
year: 1992
tidal_id: 1845519
tags:
  - Progressivemetal
  - Progressivepop
  - Numetal
  - Dreamtheater
rating:
---

# Images and Words
**Artist:** Dream Theater
**Year:** 1992

![[_covers/Dream Theater - Images and Words.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/1845519
```
^button-4vql
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Dream%20Theater%20Images%20and%20Words
```
^button-rqvw

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
| 1-1 | Pull Me Under | 8:11 |  |
| 1-2 | Another Day | 4:22 |  |
| 1-3 | Take the Time | 8:21 |  |
| 1-4 | Surrounded | 5:28 |  |
| 2-1 | Metropolis – Part I (The Miracle and the Sleeper) | 9:30 |  |
| 2-2 | Under a Glass Moon | 7:02 |  |
| 2-3 | Wait for Sleep | 2:31 |  |
| 2-4 | Learning to Live | 11:30 |  |
