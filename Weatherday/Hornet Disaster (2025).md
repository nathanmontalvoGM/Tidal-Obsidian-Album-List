---
title: "Hornet Disaster"
artist: "Weatherday"
year: 2025
tidal_id: 407147757
tags:
  - Emo
  - NoisePop
  - Slackerrock
  - Rock
rating:
---

# Hornet Disaster
**Artist:** Weatherday
**Year:** 2025

![[_covers/Weatherday - Hornet Disaster.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/407147757
```
^button-xd67
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Weatherday%20Hornet%20Disaster
```
^button-5qbn

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
| 1 | Hornet Disaster | 1:53 |  |
| 2 | Meanie | 2:38 |  |
| 3 | Angel | 1:54 |  |
| 4 | Take Care of Yourself (Paper‐Like Nests) | 3:46 |  |
| 5 | Hug | 4:51 |  |
| 6 | Radar Ballet | 4:50 |  |
| 7 | Green Tea Seaweed Sea | 6:20 |  |
| 8 | Blood Online | 3:24 |  |
| 9 | Blanket | 4:00 |  |
| 10 | Pulka | 3:30 |  |
| 11 | Heartbeats | 2:30 |  |
| 12 | Chopland Sedans | 4:27 |  |
| 13 | Cooperative Calligraphy | 4:04 |  |
| 14 | Ripped Apart by Hands | 3:46 |  |
| 15 | Nostalgia Drive Avatar | 8:17 |  |
| 16 | Aldehydes | 3:33 |  |
| 17 | Tiara | 3:42 |  |
| 18 | Agatha’s Goldfish (Sparkling Water) | 6:02 |  |
| 19 | Heaven Smile | 2:44 |  |
