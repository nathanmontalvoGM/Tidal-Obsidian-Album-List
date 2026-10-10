---
title: "Everything Goes Numb"
artist: "Streetlight Manifesto"
year: 2003
tidal_id: 73530248
tags:
  - Skapunk
  - Ska
  - Thirdwaveska
  - Punk
rating:
---

# Everything Goes Numb
**Artist:** Streetlight Manifesto
**Year:** 2003

![[_covers/Streetlight Manifesto - Everything Goes Numb.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/73530248
```
^button-4z09
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Streetlight%20Manifesto%20Everything%20Goes%20Numb
```
^button-8dng

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
| 1 | Everything Went Numb | 3:29 |  |
| 2 | That’ll Be the Day | 4:42 |  |
| 3 | Point / Counterpoint | 5:27 |  |
| 4 | If and When We Rise Again | 4:19 |  |
| 5 | A Better Place, a Better Time | 6:28 |  |
| 6 | We Are the Few | 4:56 |  |
| 7 | Failing, Flailing | 5:28 |  |
| 8 | Here’s to Life | 4:41 |  |
| 9 | A Moment of Silence | 5:13 |  |
| 10 | A Moment of Violence | 2:00 |  |
| 11 | The Saddest Song | 3:18 |  |
| 12 | The Big Sleep | 5:02 |  |
