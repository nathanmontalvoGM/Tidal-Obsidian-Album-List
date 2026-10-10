---
title: Diamond morning
artist: Karmanjakah
year: 2026
tidal_id: 501890559
tags:
  - Postmetal
  - Progressivemetal
rating:
---

# Diamond morning
**Artist:** Karmanjakah
**Year:** 2026


```button
name ▶ Play on Tidal
type link
action tidal://album/501890559
```
^button-n0ep
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Karmanjakah%20Diamond%20morning
```
^button-h049

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
| 1 | Dove | 4:05 |  |
| 2 | Eyes seeing eyes | 5:56 |  |
| 3 | Sun, astray | 5:19 |  |
| 4 | Moon, astray | 3:41 |  |
| 5 | Thousand horns | 6:42 |  |
| 6 | Sapphire | 1:48 |  |
| 7 | Ruby | 1:33 |  |
| 8 | Diamond Morning | 5:19 |  |
| 9 | Diamond Art | 1:21 |  |
| 10 | Diamond Train | 7:57 |  |
