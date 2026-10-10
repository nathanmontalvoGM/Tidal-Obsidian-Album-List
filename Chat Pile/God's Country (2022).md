---
title: "God's Country"
artist: "Chat Pile"
year: 2022
tidal_id: 225188684
tags:
  - Noiserock
  - SludgeMetal
  - Posthardcore
  - Sludge
rating:
---

# God's Country
**Artist:** Chat Pile
**Year:** 2022

![[_covers/Chat Pile - God's Country.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/225188684
```
^button-tazc
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Chat%20Pile%20God%27s%20Country
```
^button-1tp1

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
| 1 | Slaughterhouse | 4:12 |  |
| 2 | Why | 3:31 |  |
| 3 | Pamela | 4:57 |  |
| 4 | Wicked Puppet Dance | 3:07 |  |
| 5 | Anywhere | 5:47 |  |
| 6 | Tropical Beaches, Inc. | 3:46 |  |
| 7 | The Mask | 2:57 |  |
| 8 | I Don’t Care If I Burn | 2:54 |  |
| 9 | grimace_smoking_weed.jpeg | 9:05 |  |
