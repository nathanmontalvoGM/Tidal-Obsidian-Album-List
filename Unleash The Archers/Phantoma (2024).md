---
title: Phantoma
artist: Unleash The Archers
year: 2024
tidal_id: 335473443
tags:
  - Powermetal
  - Conceptalbum
  - Mdm
rating:
---

# Phantoma
**Artist:** Unleash The Archers
**Year:** 2024

![[_covers/Unleash The Archers - Phantoma.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/335473443
```
^button-uqk5
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Unleash%20The%20Archers%20Phantoma
```
^button-hdlo

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
| 1 | Human Era | 5:40 |  |
| 2 | Ph4/NT0mA | 6:30 |  |
| 3 | Buried in Code | 3:39 |  |
| 4 | The Collective | 5:53 |  |
| 5 | Green & Glass | 5:30 |  |
| 6 | Gods in Decay | 5:02 |  |
| 7 | Give It Up or Give It All | 7:35 |  |
| 8 | Ghosts in the Mist | 5:46 |  |
| 9 | Seeking Vengeance | 5:22 |  |
| 10 | Blood Empress | 5:10 |  |
