---
title: "Cherish"
artist: "Kirinji"
year: 2019
tidal_id: 122414860
tags:
  - Pop
rating:
---

# Cherish
**Artist:** Kirinji
**Year:** 2019

![[_covers/Kirinji - Cherish.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/122414860
```
^button-4pat
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Kirinji%20Cherish
```
^button-svzb

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
| 1 | 「あの娘は誰？」とか言わせたい | 4:41 |  |
| 2 | killer tune kills me | 4:10 |  |
| 3 | 雑務 | 5:00 |  |
| 4 | Almond Eyes | 4:56 |  |
| 5 | shed blood! | 5:30 |  |
| 6 | 善人の反省 | 4:11 |  |
| 7 | Pizza VS Hamburger | 4:15 |  |
| 8 | 休日の過ごし方 | 4:03 |  |
| 9 | 隣で寝てる人 | 4:37 |  |
