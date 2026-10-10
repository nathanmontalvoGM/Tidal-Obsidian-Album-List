---
title: "This Better Be Something Great"
artist: "Westside Cowboy"
year: 2025
tidal_id: 442598539
tags:
  - Americana
  - Folk
  - Indierock
  - Powerpop
rating:
---

# This Better Be Something Great
**Artist:** Westside Cowboy
**Year:** 2025

![[_covers/Westside Cowboy - This Better Be Something Great.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/442598539
```
^button-zbw0
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Westside%20Cowboy%20This%20Better%20Be%20Something%20Great
```
^button-9hcs

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
| 1 | I’ve Never Met Anyone I Thought I Could Really Love (Until I Met You) | 2:47 |  |
| 2 | Alright Alright Alright | 2:01 |  |
| 3 | Drunk Surfer | 3:54 |  |
| 4 | Shells | 3:51 |  |
| 5 | Slowly I’m Sure | 2:06 |  |
