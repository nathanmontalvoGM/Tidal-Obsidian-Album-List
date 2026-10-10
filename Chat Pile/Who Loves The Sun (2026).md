---
title: "Who Loves The Sun"
artist: "Chat Pile"
year: 2026
tidal_id: 527100233
tags: []
rating:
---

# Who Loves The Sun
**Artist:** Chat Pile
**Year:** 2026

![[_covers/Chat Pile - Who Loves The Sun.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/527100233
```
^button-1vo5
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Chat%20Pile%20Who%20Loves%20The%20Sun
```
^button-mcrd

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
| 1 | Creature | 4:23 |  |
| 2 | Deep Blue | 4:05 |  |
| 3 | Same Rules | 3:47 |  |
| 4 | PEN I S MALL | 4:58 |  |
| 5 | Shrine | 4:37 |  |
| 6 | Intruder | 5:05 |  |
| 7 | Christabel ’26 | 3:56 |  |
| 8 | Influence | 4:29 |  |
| 9 | Family Funeral | 5:02 |  |
| 10 | October All the Time | 3:23 |  |
