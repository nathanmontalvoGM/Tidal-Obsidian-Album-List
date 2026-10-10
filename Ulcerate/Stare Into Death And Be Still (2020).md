---
title: "Stare Into Death And Be Still"
artist: "Ulcerate"
year: 2020
tidal_id: 133259394
tags:
  - Technicaldeathmetal
  - Progressivemetal
  - Mathmetal
  - Dissonantdeathmetal
rating:
---

# Stare Into Death And Be Still
**Artist:** Ulcerate
**Year:** 2020

![[_covers/Ulcerate - Stare Into Death And Be Still.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/133259394
```
^button-r0it
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Ulcerate%20Stare%20Into%20Death%20And%20Be%20Still
```
^button-wqeb

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
| 1 | Stare Into Death and Be Still | 8:24 |  |
