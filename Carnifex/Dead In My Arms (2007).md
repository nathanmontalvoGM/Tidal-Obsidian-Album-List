---
title: "Dead In My Arms"
artist: "Carnifex"
year: 2007
tidal_id: 9197059
tags:
  - Deathcore
rating:
---

# Dead In My Arms
**Artist:** Carnifex
**Year:** 2007

![[_covers/Carnifex - Dead In My Arms.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/9197059
```
^button-h7jk
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Carnifex%20Dead%20In%20My%20Arms
```
^button-knwo

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
| 1 | Intro | 0:41 |  |
| 2 | Slit Wrist Savior | 4:16 |  |
| 3 | Hope Dies With the Decadent | 3:51 |  |
| 4 | Lie to My Face | 3:02 |  |
| 5 | Love Lies in Ashes | 3:43 |  |
| 6 | A Winter in Remorse | 3:02 |  |
| 7 | Collaborating Like Killers | 3:54 |  |
| 8 | My Heart in Atrophy | 3:00 |  |
| 9 | Dead in My Eyes | 1:39 |  |
| 10 | Dead in My Arms | 3:26 |  |
