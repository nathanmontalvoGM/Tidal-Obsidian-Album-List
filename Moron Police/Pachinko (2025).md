---
title: Pachinko
artist: Moron Police
year: 2025
tidal_id: 455086241
tags:
  - progressiverock
  - Poprock
rating:
---

# Pachinko
**Artist:** Moron Police
**Year:** 2025

![[_covers/Moron Police - Pachinko.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/455086241
```
^button-7ah0
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Moron%20Police%20Pachinko
```
^button-cqn6

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
| 1 | Nothing Breaks (A Port of Call) | 4:45 |  |
| 2 | Alfredo and the Afterlife | 2:31 |  |
| 3 | Waiting Around for You | 3:31 |  |
| 4 | Cormorant | 3:35 |  |
| 5 | Make Things Easier | 2:38 |  |
| 6 | Pachinko, Pt. 1 | 11:44 |  |
| 7 | Pachinko, Pt. 2 | 4:10 |  |
| 8 | King Among Kittens | 3:48 |  |
| 9 | Take Me to the City | 3:49 |  |
| 10 | The Apathy of Kings | 5:10 |  |
| 11 | Hanabi | 0:51 |  |
| 12 | Okinawa Sky | 4:15 |  |
| 13 | The Sentient Dreamer | 2:57 |  |
| 14 | Giving Up the Ghost | 6:00 |  |
