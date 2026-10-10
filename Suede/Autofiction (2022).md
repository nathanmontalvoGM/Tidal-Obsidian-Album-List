---
title: "Autofiction"
artist: "Suede"
year: 2022
tidal_id: 489904997
tags:
  - Alternativerock
  - Postpunkrevival
  - Glamrock
  - Rock
rating:
---

# Autofiction
**Artist:** Suede
**Year:** 2022

![[_covers/Suede - Autofiction.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/489904997
```
^button-43xc
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Suede%20Autofiction
```
^button-funm

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
| 1 | She Still Leads Me On | 4:09 |  |
| 2 | Personality Disorder | 4:00 |  |
| 3 | 15 Again | 3:25 |  |
| 4 | The Only Way I Can Love You | 4:08 |  |
| 5 | That Boy on the Stage | 2:36 |  |
| 6 | Drive Myself Home | 4:30 |  |
| 7 | Black Ice | 2:45 |  |
| 8 | Shadow Self | 3:34 |  |
| 9 | It’s Always the Quiet Ones | 4:12 |  |
| 10 | What Am I Without You? | 6:18 |  |
| 11 | Turn Off Your Brain and Yell | 5:54 |  |
