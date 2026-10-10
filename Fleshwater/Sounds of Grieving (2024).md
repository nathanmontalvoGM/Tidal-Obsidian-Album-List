---
title: "Sounds of Grieving"
artist: "Fleshwater"
year: 2024
tidal_id: 335452484
tags:
  - Shoegaze
  - DreamPop
  - Rock
  - Indietronica
rating:
---

# Sounds of Grieving
**Artist:** Fleshwater
**Year:** 2024

![[_covers/Fleshwater - Sounds of Grieving.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/335452484
```
^button-86he
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Fleshwater%20Sounds%20of%20Grieving
```
^button-4gmr

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
| 1 | woohoo (“what if” mix) | 2:50 |  |
| 2 | what the f#%! was said | 2:26 |  |
| 3 | i’m not here | 2:34 |  |
| 4 | save these memories | 4:19 |  |
| 5 | closet (acoustic) | 2:35 |  |
| 6 | linda claire (mirsy mix) | 3:12 |  |
| 7 | the sound of grieving | 5:08 |  |
