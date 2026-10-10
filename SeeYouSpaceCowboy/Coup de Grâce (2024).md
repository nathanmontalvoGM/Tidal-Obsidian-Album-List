---
title: "Coup de Grâce"
artist: "SeeYouSpaceCowboy..."
year: 2024
tidal_id: 345706296
tags:
  - Metalcore
  - Mathcore
  - Sasscore
  - Emo
rating:
---

# Coup de Grâce
**Artist:** SeeYouSpaceCowboy...
**Year:** 2024

![[_covers/SeeYouSpaceCowboy - Coup de Grâce.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/345706296
```
^button-jlwg
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=SeeYouSpaceCowboy...%20Coup%20de%20Gr%C3%A2ce
```
^button-4k8w

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
| 1 | Allow Us to Set the Scene | 2:26 |  |
| 2 | Subtle Whispers to Take Your Breath Away | 3:06 |  |
| 3 | And the Two Slipped Into the Shadows | 3:25 |  |
| 4 | Red Wine and Discontent | 3:33 |  |
| 5 | Lubricant Like Kerosene | 3:17 |  |
| 6 | Respite for a Tragic Tale | 1:56 |  |
| 7 | Silhouettes in Motion | 2:47 |  |
| 8 | To the Dance Floor for Shelter | 4:19 |  |
| 9 | Rhythm and Rapture | 3:01 |  |
| 10 | Sister With a Gun | 3:01 |  |
| 11 | Chewing the Scenery | 3:48 |  |
| 12 | Curtain Call | 4:24 |  |
