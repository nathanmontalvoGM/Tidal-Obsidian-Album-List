---
title: "Permanent Waves"
artist: "Rush"
year: 1980
tidal_id: 77598513
tags:
  - Progressivepop
  - Hardrock
  - Classicrock
  - Rock
rating:
---

# Permanent Waves
**Artist:** Rush
**Year:** 1980

![[_covers/Rush - Permanent Waves.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/77598513
```
^button-emlw
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Rush%20Permanent%20Waves
```
^button-jn5f

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
| 1 | The Spirit of Radio | 4:59 |  |
| 2 | Freewill | 5:24 |  |
| 3 | Jacob’s Ladder | 7:31 |  |
| 4 | Entre nous | 4:38 |  |
| 5 | Different Strings | 3:52 |  |
| 6 | Natural Science | 9:16 |  |
