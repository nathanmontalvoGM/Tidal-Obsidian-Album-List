---
title: "An Undying Love for a Burning World"
artist: "Neurosis"
year: 2026
tidal_id: 504855403
tags:
  - Numetal
rating:
---

# An Undying Love for a Burning World
**Artist:** Neurosis
**Year:** 2026

![[_covers/Neurosis - An Undying Love for a Burning World.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/504855403
```
^button-3s50
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Neurosis%20An%20Undying%20Love%20for%20a%20Burning%20World
```
^button-46ei

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
| 1 | We Are Torn Wide Open | 0:52 |  |
| 2 | Mirror Deep | 5:39 |  |
| 3 | First Red Rays | 8:27 |  |
| 4 | Blind | 9:05 |  |
| 5 | Seething and Scattered | 8:13 |  |
| 6 | Untethered | 4:02 |  |
| 7 | In the Waiting Hours | 10:15 |  |
| 8 | Last Light | 16:57 |  |
