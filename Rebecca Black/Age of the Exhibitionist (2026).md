---
title: "Age of the Exhibitionist"
artist: "Rebecca Black"
year: 2026
tidal_id: 536088056
tags: []
rating:
---

# Age of the Exhibitionist
**Artist:** Rebecca Black
**Year:** 2026

![[_covers/Rebecca Black - Age of the Exhibitionist.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/536088056
```
^button-aetx
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Rebecca%20Black%20Age%20of%20the%20Exhibitionist
```
^button-0aab

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
| 1 | Anaheim Star | 2:46 |  |
| 2 | Hot Wet Delirious | 3:08 |  |
| 3 | Exhibitionism | 3:37 |  |
| 4 | Corsetry | 3:33 |  |
| 5 | Miss Delicious | 3:21 |  |
| 6 | Pistol | 3:14 |  |
| 7 | Backstage Baby Interlude | 1:38 |  |
| 8 | Michael. | 3:32 |  |
| 9 | Visions Again | 3:42 |  |
| 10 | Waschesalon | 3:12 |  |
| 11 | Metamorphia | 3:35 |  |
| 12 | Speakerphone | 2:41 |  |
