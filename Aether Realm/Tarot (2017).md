---
title: "Tarot"
artist: "Aether Realm"
year: 2017
tidal_id: 139517568
tags:
  - Melodicdeathmetal
  - Rock
rating:
---

# Tarot
**Artist:** Aether Realm
**Year:** 2017

![[_covers/Aether Realm - Tarot.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/139517568
```
^button-vwjw
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Aether%20Realm%20Tarot
```
^button-26wb

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
| 1 | The Fool | 7:54 |  |
| 2 | Tarot | 4:23 |  |
| 3 | The Tower | 2:56 |  |
| 4 | King of Cups | 4:59 |  |
| 5 | Death | 4:28 |  |
| 6 | The Chariot | 6:24 |  |
| 7 | The Devil | 8:45 |  |
| 8 | The Emperor | 2:48 |  |
| 9 | Strength | 6:17 |  |
| 10 | Temperance | 5:27 |  |
| 11 | The Sun, The Moon, The Star | 19:09 |  |
