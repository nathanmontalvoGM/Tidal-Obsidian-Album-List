---
title: "Ocean Machine"
artist: "Devin Townsend"
year: 2003
tidal_id: 51978105
tags:
  - Progressivemetal
  - Progressivepop
  - Ambient
  - Atmosphericmetal
rating:
---

# Ocean Machine
**Artist:** Devin Townsend
**Year:** 2003

![[_covers/Devin Townsend - Ocean Machine.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/51978105
```
^button-285e
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Devin%20Townsend%20Ocean%20Machine
```
^button-ls1x

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
| 1 | Seventh Wave | 6:50 |  |
| 2 | Life | 4:31 |  |
| 3 | Night | 4:45 |  |
| 4 | Hide Nowhere | 5:00 |  |
| 5 | Sister | 2:48 |  |
| 6 | 3 A.M. | 1:56 |  |
| 7 | Voices in the Fan | 4:39 |  |
| 8 | Greetings | 2:53 |  |
| 9 | Regulator | 5:06 |  |
| 10 | Funeral | 8:06 |  |
| 11 | Bastard | 10:17 |  |
| 12 | The Death of Music | 12:15 |  |
| 13 | Thing Beyond Things | 4:47 |  |
