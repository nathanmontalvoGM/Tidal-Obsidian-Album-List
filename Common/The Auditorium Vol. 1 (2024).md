---
title: "The Auditorium Vol. 1"
artist: "Common"
year: 2024
tidal_id: 373515201
tags:
  - Hiphop
rating:
---

# The Auditorium Vol. 1
**Artist:** Common
**Year:** 2024

![[_covers/Common - The Auditorium Vol. 1.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/373515201
```
^button-5u66
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Common%20The%20Auditorium%20Vol.%201
```
^button-aa32

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
| 1 | Dreamin’ | 4:00 |  |
| 2 | Chi‐Town Do It | 4:26 |  |
| 3 | This Man | 4:02 |  |
| 4 | We’re on Our Way | 4:16 |  |
| 5 | Fortunate | 4:14 |  |
| 6 | So Many People | 5:14 |  |
| 7 | Wise Up | 3:47 |  |
| 8 | A GOD (There Is) | 3:47 |  |
| 9 | Stellar | 4:23 |  |
| 10 | Lonesome | 4:36 |  |
| 11 | All Kind of Ideas | 3:48 |  |
| 12 | When the Sun Shines Again | 4:45 |  |
| 13 | Everything’s So Grand | 6:04 |  |
| 14 | Now and Then | 4:30 |  |
| 15 | Outro | 0:55 |  |
