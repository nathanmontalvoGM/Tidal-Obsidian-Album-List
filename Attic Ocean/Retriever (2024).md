---
title: Retriever
artist: Attic Ocean
year: 2024
tidal_id: 385711862
tags:
  - "#DreamPop"
  - Shoegaze
rating:
---

# Retriever
**Artist:** Attic Ocean
**Year:** 2024

![[_covers/Attic Ocean - Retriever.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/385711862
```
^button-2r41
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Attic%20Ocean%20Retriever
```
^button-44f3

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
| 1 | Young Again | 2:49 |  |
| 2 | Lilies and Sea | 4:39 |  |
| 3 | Glow | 4:06 |  |
| 4 | Sleepless | 3:17 |  |
| 5 | Weeks Into Years | 3:40 |  |
