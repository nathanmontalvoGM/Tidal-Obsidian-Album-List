---
title: "Who Are You When No One Is Watching?"
artist: "Graphic Nature"
year: 2024
tidal_id: 359828113
tags:
  - Metalcore
  - Album2023
rating:
---

# Who Are You When No One Is Watching?
**Artist:** Graphic Nature
**Year:** 2024

![[_covers/Graphic Nature - Who Are You When No One Is Watching-.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/359828113
```
^button-nvlx
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Graphic%20Nature%20Who%20Are%20You%20When%20No%20One%20Is%20Watching%3F
```
^button-kwck

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
| 1 | Who Are You? |  |  |
| 2 | Locked In |  |  |
| 3 | Blinded |  |  |
| 4 | Human | 3:44 |  |
| 5 | Something I'm Not | 3:25 |  |
| 6 | Breathe |  |  |
| 7 | Session24. |  |  |
| 8 | N.F.A |  |  |
| 9 | Fractured | 3:42 |  |
| 10 | Low |  |  |
| 11 | To the Grave | 4:07 |  |
| 12 | When No One Is Watching |  |  |
| 13 | For You |  |  |
