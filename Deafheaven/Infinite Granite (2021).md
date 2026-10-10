---
title: "Infinite Granite"
artist: "Deafheaven"
year: 2021
tidal_id: 430132752
tags:
  - Shoegaze
  - DreamPop
  - Blackgaze
  - Electronicore
rating:
---

# Infinite Granite
**Artist:** Deafheaven
**Year:** 2021

![[_covers/Deafheaven - Infinite Granite.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/430132752
```
^button-8vrj
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Deafheaven%20Infinite%20Granite
```
^button-odnw

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
| 1 | Shellstar | 6:06 |  |
| 2 | In Blur | 5:29 |  |
| 3 | Great Mass of Color | 6:00 |  |
| 4 | Neptune Raining Diamonds | 3:05 |  |
| 5 | Lament for Wasps | 7:08 |  |
| 6 | Villain | 5:41 |  |
| 7 | The Gnashing | 5:34 |  |
| 8 | Other Language | 6:10 |  |
| 9 | Mombasa | 8:17 |  |
