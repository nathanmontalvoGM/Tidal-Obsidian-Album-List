---
title: "Stung!"
artist: "Pond"
year: 2024
tidal_id: 346509423
tags:
  - Neopsych
  - 2024releases
  - Psychedelicrock
rating:
---

# Stung!
**Artist:** Pond
**Year:** 2024

![[_covers/Pond - Stung!.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/346509423
```
^button-y604
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Pond%20Stung%21
```
^button-v53h

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
| 1 | Constant Picnic | 3:29 |  |
| 2 | (I’m) Stung | 3:55 |  |
| 3 | Neon River | 4:12 |  |
| 4 | So Lo | 3:48 |  |
| 5 | Black Lung | 4:28 |  |
| 6 | Sunrise for the Lonely | 3:30 |  |
| 7 | Elf Bar Blues | 2:06 |  |
| 8 | Edge of the World Pt. 3 | 8:07 |  |
| 9 | Stars in Silken Sheets | 0:35 |  |
| 10 | Boys Don’t Crash | 3:46 |  |
| 11 | O, UV Ray | 4:15 |  |
| 12 | Last Elvis | 3:34 |  |
| 13 | Elephant Gun | 3:16 |  |
| 14 | Fell From Grace With the Sea | 5:17 |  |
