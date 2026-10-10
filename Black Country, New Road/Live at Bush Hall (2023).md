---
title: "Live at Bush Hall"
artist: "Black Country, New Road"
year: 2023
tidal_id: 274738150
tags:
  - Progressivepop
  - Chamberpop
  - ArtRock
  - BaroquePop
rating:
---

# Live at Bush Hall
**Artist:** Black Country, New Road
**Year:** 2023

![[_covers/Black Country, New Road - Live at Bush Hall.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/274738150
```
^button-9zvp
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Black%20Country%2C%20New%20Road%20Live%20at%20Bush%20Hall
```
^button-coj9

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
| 1 | Up Song |  |  |
| 2 | The Boy |  |  |
| 3 | I Won’t Always Love You |  |  |
| 4 | Across the Pond Friend |  |  |
| 5 | Laughing Song |  |  |
| 6 | Intermission |  |  |
| 7 | The Wrong Trousers |  |  |
| 8 | Turbines |  |  |
| 9 | Dancers |  |  |
| 10 | Up Song (reprise) |  |  |
