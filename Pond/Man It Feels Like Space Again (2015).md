---
title: "Man It Feels Like Space Again"
artist: "Pond"
year: 2015
tidal_id: 475743082
tags:
  - Psychedelicrock
  - Poptron
  - Neopsychedelia
  - Psychedelicpop
rating:
---

# Man It Feels Like Space Again
**Artist:** Pond
**Year:** 2015

![[_covers/Pond - Man It Feels Like Space Again.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/475743082
```
^button-z00h
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Pond%20Man%20It%20Feels%20Like%20Space%20Again
```
^button-pr6p

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
| 1 | Waiting Around for Grace | 5:09 |  |
| 2 | Elvis' Flaming Star | 3:25 |  |
| 3 | Holding Out for You | 4:43 |  |
| 4 | Zond | 4:04 |  |
| 5 | Heroic Shart | 4:04 |  |
| 6 | Sitting Up on Our Crane | 6:00 |  |
| 7 | Outside Is the Right Side | 5:09 |  |
| 8 | Medicine Hat | 4:07 |  |
| 9 | Man It Feels Like Space Again | 8:21 |  |
