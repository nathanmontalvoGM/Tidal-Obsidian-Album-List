---
title: "A Laughing Death in Meatspace"
artist: "Tropical Fuck Storm"
year: 2018
tidal_id: 92329373
tags:
  - Punkblues
  - Artpunk
  - Psychedelicrock
  - Noiserock
rating:
---

# A Laughing Death in Meatspace
**Artist:** Tropical Fuck Storm
**Year:** 2018

![[_covers/Tropical Fuck Storm - A Laughing Death in Meatspace.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/92329373
```
^button-bhfr
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Tropical%20Fuck%20Storm%20A%20Laughing%20Death%20in%20Meatspace
```
^button-26qy

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
| 1 | You Let My Tyres Down | 5:41 |  |
| 2 | Antimatter Animals | 5:14 |  |
| 3 | Chameleon Paint | 4:30 |  |
| 4 | The Future of History | 4:25 |  |
| 5 | Two Afternoons | 4:33 |  |
| 6 | Soft Power | 5:48 |  |
| 7 | Shellfish Toxin | 5:35 |  |
| 8 | A Laughing Death in Meatspace | 5:30 |  |
| 9 | Rubber Bullies | 6:01 |  |
