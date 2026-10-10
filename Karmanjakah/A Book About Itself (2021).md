---
title: "A Book About Itself"
artist: "Karmanjakah"
year: 2021
tidal_id: 164870595
tags:
  - Numetal
  - Progressivemetal
  - Progressivepop
  - Thall
rating:
---

# A Book About Itself
**Artist:** Karmanjakah
**Year:** 2021

![[_covers/Karmanjakah - A Book About Itself.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/164870595
```
^button-2fo4
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Karmanjakah%20A%20Book%20About%20Itself
```
^button-nmkt

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
| 1 | Nautilus | 4:31 |  |
| 2 | Vårdkasar | 3:55 |  |
| 3 | Wild Horse | 5:01 |  |
| 4 | Unseen | 4:01 |  |
| 5 | Paper Boats | 4:55 |  |
| 6 | Starling | 3:33 |  |
| 7 | Julia | 6:58 |  |
| 8 | Samples | 4:53 |  |
| 9 | First Sun | 4:24 |  |
| 10 | Naustá | 7:35 |  |
