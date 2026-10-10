---
title: "Most Normal"
artist: "Gilla Band"
year: 2022
tidal_id: 248539820
tags:
  - Nowave
  - Noiserock
  - Industrialrock
  - Experimentalrock
rating:
---

# Most Normal
**Artist:** Gilla Band
**Year:** 2022

![[_covers/Gilla Band - Most Normal.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/248539820
```
^button-2trp
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Gilla%20Band%20Most%20Normal
```
^button-1eo3

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
| 1 | The Gum | 2:49 |  |
| 2 | Eight Fivers | 2:20 |  |
| 3 | Backwash | 3:21 |  |
| 4 | Gushie | 1:10 |  |
| 5 | Bin Liner Fashion | 2:18 |  |
| 6 | Capgras | 0:55 |  |
| 7 | The Weirds | 6:44 |  |
| 8 | I Was Away | 4:38 |  |
| 9 | Almost Soon | 3:23 |  |
| 10 | Red Polo Neck | 1:59 |  |
| 11 | Pratfall | 2:35 |  |
| 12 | Post Ryan | 4:26 |  |
