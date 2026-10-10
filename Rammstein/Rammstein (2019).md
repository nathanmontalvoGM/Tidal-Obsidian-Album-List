---
title: "Rammstein"
artist: "Rammstein"
year: 2019
tidal_id: 109100968
tags:
  - Industrialmetal
  - Neuedeutscheharte
  - Numetal
  - Industrialrock
rating:
---

# Rammstein
**Artist:** Rammstein
**Year:** 2019

![[_covers/Rammstein - Rammstein.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/109100968
```
^button-he0d
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Rammstein%20Rammstein
```
^button-de93

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
| 1 | Stripped | 4:27 |  |
| 2 | Du hast | 3:56 |  |
| 3 | Wut will nicht sterben | 4:27 |  |
| 4 | Du riechst so gut '98 | 4:25 |  |
| 5 | Rammstein | 4:28 |  |
| 6 | Bestrafe mich | 3:39 |  |
| 7 | Sehnsucht | 4:06 |  |
| 8 | Wilder Wein | 5:43 |  |
| 9 | Bück dich | 3:24 |  |
| 10 | Engel | 4:26 |  |
| 11 | Wollt ihr das Bett in Flammen sehen? | 5:22 |  |
| 12 | Seemann | 4:50 |  |
| 13 | Der Meister | 4:11 |  |
| 14 | Küss mich (Fellfrosch) | 3:32 |  |
| 15 | Tier | 3:48 |  |
| 16 | Das Modell | 4:46 |  |
| 17 | Alter Mann | 4:22 |  |
