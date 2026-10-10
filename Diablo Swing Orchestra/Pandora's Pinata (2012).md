---
title: "Pandora's Pinata"
artist: "Diablo Swing Orchestra"
year: 2012
tidal_id: 97413250
tags:
  - ExitStrategyOfAWreckingBall
  - Aurora
  - VoodooMonAmour
  - MassRapture
rating:
---

# Pandora's Pinata
**Artist:** Diablo Swing Orchestra
**Year:** 2012

![[_covers/Diablo Swing Orchestra - Pandora's Pinata.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/97413250
```
^button-12x4
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Diablo%20Swing%20Orchestra%20Pandora%27s%20Pinata
```
^button-o5st

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
| 1 | Voodoo Mon Amour | 4:31 |  |
| 2 | Guerrilla Laments | 4:55 |  |
| 3 | Kevlar Sweethearts | 4:24 |  |
| 4 | How to Organize a Lynch Mob | 0:53 |  |
| 5 | Black Box Messiah | 2:57 |  |
| 6 | Exit Strategy of a Wrecking Ball | 6:01 |  |
| 7 | Aurora | 5:05 |  |
| 8 | Mass Rapture | 6:03 |  |
| 9 | Honey Trap Aftermath | 4:15 |  |
| 10 | Of Kali Ma Calibre | 4:25 |  |
| 11 | Justice for Saint Mary | 8:17 |  |
