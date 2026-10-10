---
title: "YOUNG&DANGEROUS"
artist: "The Struts"
year: 2018
tidal_id: 96966811
tags:
  - Rock
  - MyTopSongs
  - MyScribbled
  - Nhl19
rating:
---

# YOUNG&DANGEROUS
**Artist:** The Struts
**Year:** 2018

![[_covers/The Struts - YOUNG&DANGEROUS.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/96966811
```
^button-xzub
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=The%20Struts%20YOUNG%26DANGEROUS
```
^button-rvu5

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
| 1 | Body Talks | 2:58 |  |
| 2 | Primadonna Like Me | 3:24 |  |
| 3 | In Love With a Camera | 3:22 |  |
| 4 | Bulletproof Baby | 3:13 |  |
| 5 | Who Am I? | 3:16 |  |
| 6 | People | 3:28 |  |
| 7 | Fire (Part 1) | 4:12 |  |
| 8 | Somebody New | 3:58 |  |
| 9 | Tatler Magazine | 3:05 |  |
| 10 | I Do It So Well | 3:18 |  |
| 11 | Freak Like You | 3:18 |  |
| 12 | Ashes (Part 2) | 4:37 |  |
| 13 | Body Talks | 2:57 |  |
