---
title: "BITE ME"
artist: "Reneé Rapp"
year: 2025
tidal_id: 450174478
tags:
  - Poprock
  - Altpop
  - Juliamofada
  - Pop
rating:
---

# BITE ME
**Artist:** Reneé Rapp
**Year:** 2025

![[_covers/Reneé Rapp - BITE ME.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/450174478
```
^button-zmas
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Rene%C3%A9%20Rapp%20BITE%20ME
```
^button-svf2

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
| 1 | Leave Me Alone | 2:21 |  |
| 2 | Mad | 2:54 |  |
| 3 | Why Is She Still Here? | 2:30 |  |
| 4 | Sometimes | 3:03 |  |
| 5 | Kiss It Kiss It | 2:52 |  |
| 6 | Good Girl | 3:12 |  |
| 7 | I Can’t Have You Around Me Anymore | 2:44 |  |
| 8 | Shy | 3:12 |  |
| 9 | At Least I’m Hot | 2:34 |  |
| 10 | I Think I Like You Better When You’re Gone | 2:23 |  |
| 11 | That’s So Funny | 2:49 |  |
| 12 | You’d Like That Wouldn’t You | 2:48 |  |
