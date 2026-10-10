---
title: "Graduation"
artist: "Kanye West"
year: 2007
tidal_id: 103805723
tags:
  - Hiphop
  - Rap
  - Kanyewest
  - Rnb
rating:
---

# Graduation
**Artist:** Kanye West
**Year:** 2007

![[_covers/Kanye West - Graduation.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/103805723
```
^button-daf6
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Kanye%20West%20Graduation
```
^button-r8qb

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
| 1 | Good Morning | 3:15 |  |
| 2 | Champion | 2:48 |  |
| 3 | Stronger | 5:12 |  |
| 4 | I Wonder | 4:03 |  |
| 5 | Good Life | 3:27 |  |
| 6 | Can’t Tell Me Nothing | 4:32 |  |
| 7 | Barry Bonds | 3:24 |  |
| 8 | Drunk & Hot Girls | 5:13 |  |
| 9 | Flashing Lights | 3:58 |  |
| 10 | Everything I Am | 3:48 |  |
| 11 | The Glory | 3:33 |  |
| 12 | Homecoming | 3:24 |  |
| 13 | Big Brother | 4:47 |  |
| 14 | Good Night | 3:06 |  |
| 15 | Bittersweet Poetry | 4:02 |  |
