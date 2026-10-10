---
title: "Who Will Look After The Dogs?"
artist: "PUP"
year: 2025
tidal_id: 414879455
tags:
  - Rock
  - Punk
  - Indie
  - Alternativerock
rating:
---

# Who Will Look After The Dogs?
**Artist:** PUP
**Year:** 2025

![[_covers/PUP - Who Will Look After The Dogs-.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/414879455
```
^button-07ld
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=PUP%20Who%20Will%20Look%20After%20The%20Dogs%3F
```
^button-jrso

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
| 1 | No Hope | 1:59 |  |
| 2 | Olive Garden | 1:52 |  |
| 3 | Concrete | 3:03 |  |
| 4 | Get Dumber | 2:36 |  |
| 5 | Hunger for Death | 3:10 |  |
| 6 | Needed to Hear It | 3:50 |  |
| 7 | Paranoid | 3:25 |  |
| 8 | Falling Outta Love | 2:17 |  |
| 9 | Hallways | 3:38 |  |
| 10 | Cruel | 2:38 |  |
| 11 | Best Revenge | 3:18 |  |
| 12 | Shut Up | 3:59 |  |
