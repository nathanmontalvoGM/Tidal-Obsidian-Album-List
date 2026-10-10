---
title: "Axis Mundi"
artist: "Imminence"
year: 2026
tidal_id: 566033940
tags: []
rating:
---

# Axis Mundi
**Artist:** Imminence
**Year:** 2026

![[_covers/Imminence - Axis Mundi.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/566033940
```
^button-uubl
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Imminence%20Axis%20Mundi
```
^button-vkwb

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
| 1 | Twisting in the Wind | 4:13 |  |
| 2 | The Sword That Never Bends | 3:46 |  |
| 3 | Devil May Try | 4:11 |  |
| 4 | Crestfallen | 4:04 |  |
| 5 | False Light | 3:24 |  |
| 6 | If Not Now, When | 3:57 |  |
| 7 | Didn’t Think About You (Lately) | 3:48 |  |
| 8 | Leviathan | 5:07 |  |
| 9 | Shed Your Skin | 4:53 |  |
| 10 | Power Divine | 3:54 |  |
| 11 | Exodus | 4:57 |  |
