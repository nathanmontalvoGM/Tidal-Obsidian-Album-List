---
title: "Home, Like Noplace Is There"
artist: "The Hotelier"
year: 2014
tidal_id: 177371156
tags:
  - Emo
  - Midwestemo
  - Punk
  - PopPunk
rating:
---

# Home, Like Noplace Is There
**Artist:** The Hotelier
**Year:** 2014

![[_covers/The Hotelier - Home, Like Noplace Is There.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/177371156
```
^button-4uaf
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=The%20Hotelier%20Home%2C%20Like%20Noplace%20Is%20There
```
^button-2934

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
| 1 | An Introduction to the Album | 4:32 |  |
| 2 | The Scope of All of This Rebuilding | 2:26 |  |
| 3 | In Framing | 2:59 |  |
| 4 | Your Deep Rest | 3:47 |  |
| 5 | Among the Wildflowers | 5:48 |  |
| 6 | Life in Drag | 2:21 |  |
| 7 | Housebroken | 4:50 |  |
| 8 | Discomfort Revisited | 3:59 |  |
| 9 | Dendron | 5:27 |  |
