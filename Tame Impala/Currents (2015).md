---
title: "Currents"
artist: "Tame Impala"
year: 2015
tidal_id: 47696788
tags:
  - Psychedelicpop
  - Psychedelicrock
  - Indie
  - Synthpop
rating:
---

# Currents
**Artist:** Tame Impala
**Year:** 2015

![[_covers/Tame Impala - Currents.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/47696788
```
^button-fxjy
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Tame%20Impala%20Currents
```
^button-xjt1

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
| 1-1 | Let It Happen | 7:46 |  |
| 1-2 | Nangs | 1:47 |  |
| 1-3 | The Moment | 4:15 |  |
| 1-4 | Yes I’m Changing | 4:30 |  |
| 1-5 | Eventually | 5:19 |  |
| 1-6 | Gossip | 0:55 |  |
| 1-7 | The Less I Know the Better | 3:38 |  |
| 1-8 | Past Life | 3:47 |  |
| 1-9 | Disciples | 1:48 |  |
| 1-10 | Cause I’m a Man | 4:01 |  |
| 1-11 | Reality in Motion | 4:12 |  |
| 1-12 | Love/Paranoia | 3:06 |  |
| 1-13 | New Person, Same Old Mistakes | 6:02 |  |
| 2-1 | Endors‐toi | 5:57 |  |
| 2-2 | Why Won’t You Make Up Your Mind? | 4:22 |  |
| 2-3 | Sestri Levante | 1:58 |  |
| 2-4 | Mind Mischief | 3:56 |  |
| 2-5 | Desire Be, Desire Go | 5:24 |  |
| 2-6 | Half Full Glass of Wine | 8:14 |  |
| 2-7 | Be Above It | 7:29 |  |
| 2-8 | Feels Like We Only Go Backwards | 2:56 |  |
| 2-9 | Apocalypse Dreams | 7:52 |  |
