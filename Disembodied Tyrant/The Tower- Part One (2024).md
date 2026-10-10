---
title: "The Tower: Part One"
artist: "Disembodied Tyrant"
year: 2024
tidal_id: 385181218
tags:
  - Deathcore
  - Technicaldeathcore
  - ProgressiveDeathcore
  - Blackeneddeathcore
rating:
---

# The Tower: Part One
**Artist:** Disembodied Tyrant
**Year:** 2024

![[_covers/Disembodied Tyrant - The Tower- Part One.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/385181218
```
^button-a3dd
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Disembodied%20Tyrant%20The%20Tower%3A%20Part%20One
```
^button-08zq

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
| 1 | Icarian | 4:42 |  |
| 2 | Aberrant Waltz | 4:59 |  |
| 3 | Malphasian | 5:08 |  |
