---
title: "Écailles de lune"
artist: "Alcest"
year: 2010
tidal_id: 175547820
tags:
  - Shoegaze
  - Postrock
  - Atmosphericmetal
  - Blackmetal
rating:
---

# Écailles de lune
**Artist:** Alcest
**Year:** 2010

![[_covers/Alcest - Écailles de lune.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/175547820
```
^button-1vj6
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Alcest%20%C3%89cailles%20de%20lune
```
^button-gomx

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
| 1 | Écailles de lune, Part 1 | 9:52 |  |
| 2 | Écailles de lune, Part 2 | 9:48 |  |
| 3 | Percées de lumière | 6:38 |  |
| 4 | Abysses | 1:40 |  |
| 5 | Solar Song | 5:24 |  |
| 6 | Sur l’océan couleur de fer | 8:18 |  |
