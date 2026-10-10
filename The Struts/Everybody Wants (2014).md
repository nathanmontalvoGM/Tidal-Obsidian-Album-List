---
title: "Everybody Wants"
artist: "The Struts"
year: 2014
tidal_id: 77705468
tags:
  - Rock
  - British
  - Czhit
  - Hardrock
rating:
---

# Everybody Wants
**Artist:** The Struts
**Year:** 2014

![[_covers/The Struts - Everybody Wants.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/77705468
```
^button-ajqx
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=The%20Struts%20Everybody%20Wants
```
^button-nkfy

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
| 1 | Roll Up | 3:07 |  |
| 2 | Could Have Been Me | 3:07 |  |
| 3 | Kiss This | 2:57 |  |
| 4 | Put Your Money on Me | 3:33 |  |
| 5 | Mary Go Round | 3:19 |  |
| 6 | Dirty Sexy Money | 3:57 |  |
| 7 | The Ol’ Switcheroo | 3:42 |  |
| 8 | She Makes Me Feel Like | 2:38 |  |
| 9 | Young Stars | 3:23 |  |
| 10 | Black Swan | 3:24 |  |
| 11 | These Times Are Changing | 3:26 |  |
| 12 | Only Just a Call Away | 3:04 |  |
| 13 | Where Did She Go | 3:54 |  |
