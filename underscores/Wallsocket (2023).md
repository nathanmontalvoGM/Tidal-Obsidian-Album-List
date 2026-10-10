---
title: "Wallsocket"
artist: "underscores"
year: 2023
tidal_id: 316804338
tags:
  - Indietronica
  - Electropop
  - Indierock
  - Rock
rating:
---

# Wallsocket
**Artist:** underscores
**Year:** 2023

![[_covers/underscores - Wallsocket.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/316804338
```
^button-3fi6
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=underscores%20Wallsocket
```
^button-6nzu

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
| 1-1 | Cops and robbers | 4:26 |  |
| 1-2 | Locals (Girls like us) | 4:18 |  |
| 1-3 | Duhhhhhhhhhhhhhhhhh | 4:07 |  |
| 1-4 | You don’t even know who I am | 4:04 |  |
| 1-5 | Johnny johnny johnny | 4:05 |  |
| 1-6 | Shoot to kill, kill your darlings | 5:04 |  |
| 1-7 | Horror movie soundtrack | 3:52 |  |
| 2-1 | Old money bitch | 4:06 |  |
| 2-2 | Geez louise | 7:20 |  |
| 2-3 | Seventyseven dog years | 4:35 |  |
| 2-4 | Uncanny long arms | 5:26 |  |
| 2-5 | Good luck final girl | 3:28 |  |
