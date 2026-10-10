---
title: "Autofiction"
artist: "The London Suede"
year: 2022
tidal_id: 489904997
tags:
  - Alternativerock
  - Postpunkrevival
  - Glamrock
rating:
---

# Autofiction
**Artist:** The London Suede
**Year:** 2022

![[_covers/The London Suede - Autofiction.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/489904997
```
^button-ywwj
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=The%20London%20Suede%20Autofiction
```
^button-xdk2

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
| 1 | She Still Leads Me On | 4:08 |  |
| 2 | Personality Disorder | 4:00 |  |
| 3 | 15 Again | 3:24 |  |
| 4 | The Only Way I Can Love You | 4:07 |  |
| 5 | That Boy on the Stage | 2:35 |  |
| 6 | Drive Myself Home | 4:29 |  |
| 7 | Black Ice | 2:45 |  |
| 8 | Shadow Self | 3:33 |  |
| 9 | It’s Always the Quiet Ones | 4:12 |  |
| 10 | What Am I Without You? | 6:17 |  |
| 11 | Turn Off Your Brain and Yell | 5:54 |  |
| 12 | Still Waiting | 2:50 |  |
| 13 | The Sadness in You, the Sadness in Me | 4:28 |  |
| 14 | Days Like Dead Moths | 3:42 |  |
| 15 | The Prey | 3:34 |  |
