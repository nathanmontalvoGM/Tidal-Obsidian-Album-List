---
title: "Dark Connection"
artist: "Beast In Black"
year: 2021
tidal_id: 196296303
tags:
  - Powermetal
  - Heavymetal
  - Cover
  - Crossover
rating:
---

# Dark Connection
**Artist:** Beast In Black
**Year:** 2021

![[_covers/Beast In Black - Dark Connection.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/196296303
```
^button-4aon
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Beast%20In%20Black%20Dark%20Connection
```
^button-cfdo

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
| 1 | Blade Runner | 4:08 |  |
| 2 | Bella Donna | 3:53 |  |
| 3 | Highway to Mars | 5:14 |  |
| 4 | Hardcore | 3:34 |  |
| 5 | One Night in Tokyo | 3:07 |  |
| 6 | Moonlight Rendezvous | 5:39 |  |
| 7 | Revengeance Machine | 4:09 |  |
| 8 | Dark New World | 3:58 |  |
| 9 | To the Last Drop of Blood | 3:55 |  |
| 10 | Broken Survivors | 4:26 |  |
| 11 | My Dystopia | 5:52 |  |
| 12 | Battle Hymn | 6:55 |  |
| 13 | They Don’t Care About Us | 4:33 |  |
