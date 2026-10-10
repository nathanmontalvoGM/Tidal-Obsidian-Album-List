---
title: "Ego Death At A Bachelorette Party"
artist: "Hayley Williams"
year: 2025
tidal_id: 470829563
tags:
  - Indierock
  - Poprock
  - Bedroompop
  - Singersongwriter
rating:
---

# Ego Death At A Bachelorette Party
**Artist:** Hayley Williams
**Year:** 2025

![[_covers/Hayley Williams - Ego Death At A Bachelorette Party.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/470829563
```
^button-6t08
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Hayley%20Williams%20Ego%20Death%20At%20A%20Bachelorette%20Party
```
^button-4s3k

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
| 1 | Ego Death at a Bachelorette Party | 3:18 |  |
