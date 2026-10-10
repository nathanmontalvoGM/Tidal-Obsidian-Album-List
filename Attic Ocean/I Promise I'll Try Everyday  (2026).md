---
title: "I Promise I'll Try Everyday "
artist: "Attic Ocean"
year: 2026
tidal_id: 533799063
tags: []
rating:
---

# I Promise I'll Try Everyday 
**Artist:** Attic Ocean
**Year:** 2026

![[_covers/Attic Ocean - I Promise I'll Try Everyday .jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/533799063
```
^button-hl6a
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Attic%20Ocean%20I%20Promise%20I%27ll%20Try%20Everyday%E2%80%A8
```
^button-6t6s

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
| 1 | Could It Be You | 3:44 |  |
| 2 | Aurora | 3:00 |  |
| 3 | Coastal | 3:06 |  |
| 4 | Love Spells | 3:57 |  |
| 5 | Sun | 4:46 |  |
