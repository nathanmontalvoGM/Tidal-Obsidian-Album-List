---
title: "NEVER ENOUGH"
artist: "Turnstile"
year: 2025
tidal_id: 440155726
tags:
  - Shoegaze
  - Alternativerock
  - Posthardcore
  - Rock
rating:
---

# NEVER ENOUGH
**Artist:** Turnstile
**Year:** 2025

![[_covers/Turnstile - NEVER ENOUGH.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/440155726
```
^button-lowo
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Turnstile%20NEVER%20ENOUGH
```
^button-syh8

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
| 1 | NEVER ENOUGH | 4:47 |  |
| 2 | SOLE | 3:25 |  |
| 3 | I CARE | 3:53 |  |
| 4 | DREAMING | 2:36 |  |
| 5 | LIGHT DESIGN | 2:09 |  |
| 6 | DULL | 2:18 |  |
| 7 | SUNSHOWER | 3:40 |  |
| 8 | LOOK OUT FOR ME | 6:43 |  |
| 9 | CEILING | 1:13 |  |
| 10 | SEEIN’ STARS | 3:06 |  |
| 11 | BIRDS | 2:26 |  |
| 12 | SLOWDIVE | 3:33 |  |
| 13 | TIME IS HAPPENING | 2:06 |  |
| 14 | MAGIC MAN | 3:13 |  |
