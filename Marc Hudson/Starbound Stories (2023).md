---
title: "Starbound Stories"
artist: "Marc Hudson"
year: 2023
tidal_id: 298431613
tags:
  - Numetal
  - Powermetal
  - Heavymetal
  - Uk
rating:
---

# Starbound Stories
**Artist:** Marc Hudson
**Year:** 2023

![[_covers/Marc Hudson - Starbound Stories.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/298431613
```
^button-umhh
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Marc%20Hudson%20Starbound%20Stories
```
^button-c8mk

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
| 1 | As the Twilight met the Sea | 2:02 |  |
| 2 | Freedom Heart | 6:10 |  |
| 3 | Dracula X! | 5:45 |  |
| 4 | Stars | 5:42 |  |
| 5 | The Siren | 5:40 |  |
| 6 | Astralive | 4:26 |  |
| 7 | Swansong | 5:23 |  |
| 8 | Call of the Martyrs | 8:07 |  |
| 9 | Starbound Stories | 6:57 |  |
| 10 | One more sight of the sun with You | 4:46 |  |
