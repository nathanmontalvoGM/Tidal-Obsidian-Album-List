---
title: "You're Not Alone"
artist: "Andrew W.K."
year: 2018
tidal_id: 82475046
tags:
  - Hardrock
  - Rock
  - 2010s
rating:
---

# You're Not Alone
**Artist:** Andrew W.K.
**Year:** 2018

![[_covers/Andrew W.K - You're Not Alone.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/82475046
```
^button-mbk0
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Andrew%20W.K.%20You%27re%20Not%20Alone
```
^button-ql9z

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
| 1 | The Power of Partying | 1:36 |  |
| 2 | Music Is Worth Living For | 4:22 |  |
| 3 | Ever Again | 3:18 |  |
| 4 | I Don’t Know Anything | 2:54 |  |
| 5 | The Feeling of Being Alive | 0:47 |  |
| 6 | Party Mindset | 4:11 |  |
| 7 | The Party Never Dies | 3:00 |  |
| 8 | Give Up on You | 3:16 |  |
| 9 | Keep on Going | 4:06 |  |
| 10 | In Your Darkest Moments | 1:05 |  |
| 11 | The Devil’s on Your Side | 5:22 |  |
| 12 | Break the Curse | 6:22 |  |
| 13 | Total Freedom | 3:56 |  |
| 14 | Beyond Oblivion | 4:06 |  |
| 15 | Confusion and Clarity | 1:01 |  |
| 16 | You’re Not Alone | 3:04 |  |
