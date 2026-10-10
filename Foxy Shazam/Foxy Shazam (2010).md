---
title: "Foxy Shazam"
artist: "Foxy Shazam"
year: 2010
tidal_id: 3663964
tags:
  - Alternativerock
  - 9of10stars
  - Rock
  - Glamrock
rating:
---

# Foxy Shazam
**Artist:** Foxy Shazam
**Year:** 2010

![[_covers/Foxy Shazam - Foxy Shazam.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/3663964
```
^button-mco2
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Foxy%20Shazam%20Foxy%20Shazam
```
^button-0ia7

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
| 1 | Intro/Bombs Away | 3:20 |  |
| 2 | Wanna Be Angel | 3:22 |  |
| 3 | Count Me Out | 3:31 |  |
| 4 | Bye Bye Symphony | 4:07 |  |
| 5 | Unstoppable | 3:33 |  |
| 6 | Second Floor | 3:59 |  |
| 7 | Oh Lord | 4:10 |  |
| 8 | Connect | 3:27 |  |
| 9 | Only Way to My Heart… | 4:43 |  |
| 10 | Killin' It | 3:58 |  |
| 11 | Evil Thoughts | 4:17 |  |
