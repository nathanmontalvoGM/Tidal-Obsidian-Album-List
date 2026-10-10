---
title: Black Void
artist: Abbie Falls
year: 2025
tidal_id: 447350846
tags:
  - Metalcore
  - Deathcore
rating:
---

# Black Void
**Artist:** Abbie Falls
**Year:** 2025

![[_covers/Abbie Falls - Black Void.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/447350846
```
^button-dfr9
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Abbie%20Falls%20Black%20Void
```
^button-7vqt

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
| 1 | Black Void | 3:38 |  |
| 2 | Hellbound | 3:40 |  |
| 3 | Victim | 4:21 |  |
| 4 | Purge | 3:13 |  |
