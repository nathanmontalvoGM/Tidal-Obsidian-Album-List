---
title: "The Answer to Infection (Redux)"
artist: "Cholera"
year: 2026
tidal_id: 540953130
tags: []
rating:
---

# The Answer to Infection (Redux)
**Artist:** Cholera
**Year:** 2026

![[_covers/Cholera - The Answer to Infection (Redux).jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/540953130
```
^button-f0rz
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Cholera%20The%20Answer%20to%20Infection%20%28Redux%29
```
^button-7u9i

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
| 1 | Outbreak (Redux) | 1:55 |  |
| 2 | Things That Were Shall Be Again (Redux) | 3:09 |  |
| 3 | Persuasions Convey My Torment (Redux) | 2:56 |  |
| 4 | This Love Is Your Lie (Redux) | 3:39 |  |
| 5 | The Answer to Infection (Redux) | 2:43 |  |
| 6 | Jerry's Kids (Redux) | 2:13 |  |
| 7 | Bloodstained (Redux) | 3:00 |  |
| 8 | On Goes the Show (Redux) | 3:32 |  |
