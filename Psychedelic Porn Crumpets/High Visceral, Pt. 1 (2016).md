---
title: "High Visceral, Pt. 1"
artist: "Psychedelic Porn Crumpets"
year: 2016
tidal_id: 57727310
tags:
  - Psychedelicrock
  - Progressivepop
  - Psychedelicpop
  - Heavypsych
rating:
---

# High Visceral, Pt. 1
**Artist:** Psychedelic Porn Crumpets
**Year:** 2016

![[_covers/Psychedelic Porn Crumpets - High Visceral, Pt. 1.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/57727310
```
^button-4tci
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Psychedelic%20Porn%20Crumpets%20High%20Visceral%2C%20Pt.%201
```
^button-sra3

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
| 1 | Cornflake | 3:37 |  |
| 2 | Cubensis Lenses | 5:43 |  |
| 3 | Marmalade March | 4:45 |  |
| 4 | …and the Addled Abstraction of Being | 6:26 |  |
| 5 | High Visceral | 2:31 |  |
| 6 | Surf’s Up | 3:13 |  |
| 7 | Gallop to Southport | 2:33 |  |
| 8 | Found God in a Tomato | 8:54 |  |
| 9 | Entropy | 1:54 |  |
| 10 | Denmark/Van Gogh & Gone | 7:29 |  |
