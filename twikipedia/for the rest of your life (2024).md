---
title: "for the rest of your life"
artist: "twikipedia"
year: 2024
tidal_id: 359606800
tags:
  - Indierock
  - Shoegaze
  - NoisePop
  - Powerpop
rating:
---

# for the rest of your life
**Artist:** twikipedia
**Year:** 2024

![[_covers/twikipedia - for the rest of your life.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/359606800
```
^button-wl6f
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=twikipedia%20for%20the%20rest%20of%20your%20life
```
^button-vb3i

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
| 1-1 | room for one | 3:12 |  |
| 1-2 | garden | 3:43 |  |
| 1-3 | cardboard boxes | 3:22 |  |
| 1-4 | learn yourself | 2:49 |  |
| 1-5 | figure me out | 2:31 |  |
| 1-6 | far apart | 5:21 |  |
| 1-7 | windchimes | 3:09 |  |
| 1-8 | boy | 5:03 |  |
| 2-1 | paper planes | 4:31 |  |
| 2-2 | dry your eyes | 3:30 |  |
| 2-3 | seams | 6:17 |  |
| 2-4 | anyone but you | 3:18 |  |
| 2-5 | final feliz | 4:10 |  |
| 2-6 | tudo | 2:29 |  |
| 2-7 | at once | 2:49 |  |
