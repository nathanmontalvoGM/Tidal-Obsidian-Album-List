---
title: "Minewest Emo"
artist: "TanookiAlex"
year: 2024
tidal_id: 346901379
tags:
  - Midwestemo
  - Alternativerock
  - Postrock
  - Shoegaze
rating:
---

# Minewest Emo
**Artist:** TanookiAlex
**Year:** 2024

![[_covers/TanookiAlex - Minewest Emo.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/346901379
```
^button-stdo
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=TanookiAlex%20Minewest%20Emo
```
^button-2xsp

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
| 1 | Minecraft | 4:46 |  |
| 2 | Living Mice | 2:56 |  |
| 3 | Wet Hands | 2:12 |  |
| 4 | Cat | 3:13 |  |
| 5 | Clark | 3:20 |  |
| 6 | Dry Hands | 1:23 |  |
| 7 | Mice On Venus | 4:59 |  |
| 8 | Haggstrom | 2:53 |  |
| 9 | Subwoofer Lullaby | 3:35 |  |
| 10 | Door | 1:51 |  |
| 11 | Sweden | 3:35 |  |
