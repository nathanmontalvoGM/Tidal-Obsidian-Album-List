---
title: "Funeral"
artist: "Arcade Fire"
year: 2004
tidal_id: 75194842
tags:
  - Indierock
  - Indie
  - Alternativerock
  - Rock
rating:
---

# Funeral
**Artist:** Arcade Fire
**Year:** 2004

![[_covers/Arcade Fire - Funeral.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/75194842
```
^button-vj4y
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Arcade%20Fire%20Funeral
```
^button-fulj

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
| 1 | Neighborhood #1 (Tunnels) | 4:48 |  |
| 2 | Neighborhood #2 (Laïka) | 3:32 |  |
| 3 | Une année sans lumière | 3:40 |  |
| 4 | Neighborhood #3 (Power Out) | 5:12 |  |
| 5 | Neighborhood #4 (7 Kettles) | 4:49 |  |
| 6 | Crown of Love | 4:42 |  |
| 7 | Wake Up | 5:35 |  |
| 8 | Haïti | 4:07 |  |
| 9 | Rebellion (Lies) | 5:10 |  |
| 10 | In the Backseat | 6:20 |  |
