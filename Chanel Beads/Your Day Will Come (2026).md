---
title: "Your Day Will Come"
artist: "Chanel Beads"
year: 2026
tidal_id: 513894999
tags: []
rating:
---

# Your Day Will Come
**Artist:** Chanel Beads
**Year:** 2026

![[_covers/Chanel Beads - Your Day Will Come.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/513894999
```
^button-xqlq
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Chanel%20Beads%20Your%20Day%20Will%20Come
```
^button-q956

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
| 1 | Dedicated to the World | 3:02 |  |
| 2 | Police Scanner | 2:22 |  |
| 3 | Idea June | 1:30 |  |
| 4 | Embarrassed Dog | 2:00 |  |
| 5 | Unifying Thought | 1:59 |  |
| 6 | Your Day Will Come | 3:04 |  |
| 7 | Urn | 4:33 |  |
| 8 | Coffee Culture | 5:46 |  |
| 9 | I Think I Saw | 3:11 |  |
