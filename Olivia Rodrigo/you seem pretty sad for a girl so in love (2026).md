---
title: "you seem pretty sad for a girl so in love"
artist: "Olivia Rodrigo"
year: 2026
tidal_id: 532396298
tags: []
rating:
---

# you seem pretty sad for a girl so in love
**Artist:** Olivia Rodrigo
**Year:** 2026

![[_covers/Olivia Rodrigo - you seem pretty sad for a girl so in love.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/532396298
```
^button-re3r
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Olivia%20Rodrigo%20you%20seem%20pretty%20sad%20for%20a%20girl%20so%20in%20love
```
^button-cbgs

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
| 1 | drop dead | 3:44 |  |
| 2 | stupid song | 3:30 |  |
| 3 | honeybee | 3:43 |  |
| 4 | maggots for brains | 4:00 |  |
| 5 | u + me = <3 | 4:08 |  |
| 6 | my way | 3:01 |  |
| 7 | purple | 4:00 |  |
| 8 | the cure | 4:57 |  |
| 9 | begged | 3:38 |  |
| 10 | what’s wrong with me | 3:45 |  |
| 11 | less | 3:14 |  |
| 12 | expectations | 3:42 |  |
| 13 | cigarette smoke | 5:41 |  |
