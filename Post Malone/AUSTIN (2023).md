---
title: "AUSTIN"
artist: "Post Malone"
year: 2023
tidal_id: 307068779
tags:
  - Poprock
  - Pop
  - Singersongwriter
  - Cool
rating:
---

# AUSTIN
**Artist:** Post Malone
**Year:** 2023

![[_covers/Post Malone - AUSTIN.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/307068779
```
^button-a8be
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Post%20Malone%20AUSTIN
```
^button-d4de

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
| 1 | Don’t Understand | 3:03 |  |
| 2 | Something Real | 3:25 |  |
| 3 | Chemical | 3:03 |  |
| 4 | Novacandy | 3:17 |  |
| 5 | Mourning | 2:27 |  |
| 6 | Too Cool to Die | 3:24 |  |
| 7 | Sign Me Up | 3:18 |  |
| 8 | Socialite | 3:19 |  |
| 9 | Overdrive | 2:27 |  |
| 10 | Speedometer | 2:42 |  |
| 11 | Hold My Breath | 3:28 |  |
| 12 | Enough Is Enough | 2:45 |  |
| 13 | Texas Tea | 2:19 |  |
| 14 | Buyer Beware | 2:53 |  |
| 15 | Landmine | 3:04 |  |
| 16 | Green Thumb | 2:39 |  |
| 17 | Laugh It Off | 4:06 |  |
| 18 | Joy | 4:47 |  |
