---
title: "Virus"
artist: "Haken"
year: 2020
tidal_id: 135143049
tags:
  - Progressivemetal
  - Progressivepop
  - Prog
  - Conceptalbum
rating:
---

# Virus
**Artist:** Haken
**Year:** 2020

![[_covers/Haken - Virus.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/135143049
```
^button-n0w0
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Haken%20Virus
```
^button-r6ai

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
| 1 | Prosthetic | 5:58 |  |
| 2 | Invasion | 6:42 |  |
| 3 | Carousel | 10:29 |  |
| 4 | The Strain | 5:23 |  |
| 5 | Canary Yellow | 4:14 |  |
| 6 | Messiah Complex I: Ivory Tower | 3:57 |  |
| 7 | Messiah Complex II: A Glutton for Punishment | 3:38 |  |
| 8 | Messiah Complex III: Marigold | 2:24 |  |
| 9 | Messiah Complex IV: The Sect | 2:02 |  |
| 10 | Messiah Complex V: Ectobius Rex | 4:57 |  |
| 11 | Only Stars | 2:10 |  |
