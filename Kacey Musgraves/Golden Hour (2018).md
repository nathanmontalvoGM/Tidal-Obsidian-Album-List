---
title: "Golden Hour"
artist: "Kacey Musgraves"
year: 2018
tidal_id: 86330313
tags:
  - Country
  - Softrock
  - Contemporarycountry
  - Singersongwriter
rating:
---

# Golden Hour
**Artist:** Kacey Musgraves
**Year:** 2018

![[_covers/Kacey Musgraves - Golden Hour.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/86330313
```
^button-tejf
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Kacey%20Musgraves%20Golden%20Hour
```
^button-nabz

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
| 1 | Slow Burn | 4:06 |  |
| 2 | Lonely Weekend | 3:45 |  |
| 3 | Butterflies | 3:39 |  |
| 4 | Oh, What a World | 4:00 |  |
| 5 | Mother | 1:17 |  |
| 6 | Love Is a Wild Thing | 4:15 |  |
| 7 | Space Cowboy | 3:36 |  |
| 8 | Happy & Sad | 4:02 |  |
| 9 | Velvet Elvis | 2:33 |  |
| 10 | Wonder Woman | 4:00 |  |
| 11 | High Horse | 3:32 |  |
| 12 | Golden Hour | 3:16 |  |
| 13 | Rainbow | 3:34 |  |
| 14 | Merry Go ’round | 3:29 |  |
| 15 | Follow Your Arrow | 3:19 |  |
| 16 | High Horse (Violents remix) | 3:42 |  |
