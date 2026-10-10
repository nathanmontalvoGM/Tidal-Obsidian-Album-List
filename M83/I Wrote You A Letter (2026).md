---
title: "I Wrote You A Letter"
artist: "M83"
year: 2026
tidal_id: 547816787
tags: []
rating:
---

# I Wrote You A Letter
**Artist:** M83
**Year:** 2026

![[_covers/M83 - I Wrote You A Letter.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/547816787
```
^button-2x57
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=M83%20I%20Wrote%20You%20A%20Letter
```
^button-8jwh

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
| 1 | Blister Sunrise | 3:21 |  |
| 2 | Opera | 6:49 |  |
| 3 | Siren Behold… Beasts | 5:09 |  |
| 4 | Aged | 6:39 |  |
| 5 | Losing Ground | 4:40 |  |
| 6 | Soldiers of Lust | 2:07 |  |
| 7 | Heart Motion Foto | 2:55 |  |
| 8 | Feeding Time | 5:52 |  |
| 9 | Traces of Love | 2:38 |  |
