---
title: "Frozen Charlotte"
artist: "Jack White"
year: 2026
tidal_id: 521508233
tags:
  - Plattentestsde
rating:
---

# Frozen Charlotte
**Artist:** Jack White
**Year:** 2026

![[_covers/Jack White - Frozen Charlotte.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/521508233
```
^button-4q6y
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Jack%20White%20Frozen%20Charlotte
```
^button-jxom

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
| 1 | G.O.D. and the Broken Ribs | 3:43 |  |
| 2 | Derecho Demonico | 3:53 |  |
| 3 | There's Nobody There | 3:56 |  |
| 4 | Raising the Grain | 3:06 |  |
| 5 | You'll Never Fix Me | 3:23 |  |
| 6 | Nobody Knows | 3:04 |  |
| 7 | Dollar Bill | 2:42 |  |
| 8 | I Can't Believe What I'm Hearing | 2:29 |  |
| 9 | Thick as Thieves | 3:01 |  |
| 10 | All Alone Again | 3:29 |  |
| 11 | She's in a Frenzy | 2:23 |  |
| 12 | Making Contact | 2:23 |  |
| 13 | Neighbors Blues | 5:04 |  |
