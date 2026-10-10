---
title: "Bunky Becky Birthday Boy"
artist: "Sleigh Bells"
year: 2025
tidal_id: 427884063
tags:
  - Indie
  - Electronicore
  - Experimentalrock
  - Loveatfirstlisten
rating:
---

# Bunky Becky Birthday Boy
**Artist:** Sleigh Bells
**Year:** 2025

![[_covers/Sleigh Bells - Bunky Becky Birthday Boy.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/427884063
```
^button-a129
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Sleigh%20Bells%20Bunky%20Becky%20Birthday%20Boy
```
^button-9ww0

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
| 1 | Bunky Pop | 3:01 |  |
| 2 | Wanna Start a Band? | 2:53 |  |
| 3 | Life Was Real | 2:38 |  |
| 4 | Roxette Ric | 2:48 |  |
| 5 | This Summer | 3:03 |  |
| 6 | Can I Scream | 2:33 |  |
| 7 | Badly | 2:35 |  |
| 8 | Blasted Shadow | 2:30 |  |
| 9 | Real Special Cool Thing | 2:43 |  |
| 10 | Hi Someday | 3:56 |  |
| 11 | Pulse Drips Quiet | 3:16 |  |
