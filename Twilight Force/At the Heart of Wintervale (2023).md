---
title: "At the Heart of Wintervale"
artist: "Twilight Force"
year: 2023
tidal_id: 253922982
tags:
  - Powermetal
  - Symphonicmetal
  - Fantasymetal
rating:
---

# At the Heart of Wintervale
**Artist:** Twilight Force
**Year:** 2023

![[_covers/Twilight Force - At the Heart of Wintervale.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/253922982
```
^button-el8p
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Twilight%20Force%20At%20the%20Heart%20of%20Wintervale
```
^button-qepj

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
| 1 | Twilight Force | 4:11 |  |
| 2 | At the Heart of Wintervale | 4:50 |  |
| 3 | Dragonborn | 4:00 |  |
| 4 | Highlands of the Elder Dragon | 10:32 |  |
| 5 | Skyknights of Aldaria | 5:13 |  |
| 6 | A Familiar Memory | 1:18 |  |
| 7 | Sunlight Knight | 4:28 |  |
| 8 | The Last Crystal Bearer | 10:20 |  |
| 9 | The Sapphire Dragon of Arcane Might Is Back Again | 3:35 |  |
| 10 | Skyknights of Aldaria (orchestral version) | 5:14 |  |
| 11 | The Last Crystal Bearer (orchestral version) | 10:20 |  |
