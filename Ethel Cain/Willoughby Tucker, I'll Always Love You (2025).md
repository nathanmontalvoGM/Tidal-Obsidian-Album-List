---
title: "Willoughby Tucker, I'll Always Love You"
artist: "Ethel Cain"
year: 2025
tidal_id: 439908063
tags:
  - Slowcore
  - Ambient
  - Americana
  - Singer-Songwriter
rating:
---

# Willoughby Tucker, I'll Always Love You
**Artist:** Ethel Cain
**Year:** 2025

![[_covers/Ethel Cain - Willoughby Tucker, I'll Always Love You.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/439908063
```
^button-arba
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Ethel%20Cain%20Willoughby%20Tucker%2C%20I%27ll%20Always%20Love%20You
```
^button-9k9k

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
| 1 | Janie | 5:00 |  |
| 2 | Willoughby’s Theme | 4:52 |  |
| 3 | Fuck Me Eyes | 6:05 |  |
| 4 | Nettles | 8:04 |  |
| 5 | Willoughby’s Interlude | 7:27 |  |
| 6 | Dust Bowl | 6:26 |  |
| 7 | A Knock at the Door | 5:24 |  |
| 8 | Radio Towers | 5:12 |  |
| 9 | Tempest | 10:01 |  |
| 10 | Waco, Texas | 15:16 |  |
