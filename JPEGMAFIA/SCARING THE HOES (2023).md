---
title: "SCARING THE HOES"
artist: "JPEGMAFIA"
year: 2023
tidal_id: 280631979
tags:
  - ExperimentalHipHop
  - Hardcorehiphop
  - Glitchpop
  - Jazzrap
rating:
---

# SCARING THE HOES
**Artist:** JPEGMAFIA
**Year:** 2023

![[_covers/JPEGMAFIA - SCARING THE HOES.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/280631979
```
^button-cm1b
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=JPEGMAFIA%20SCARING%20THE%20HOES
```
^button-mjka

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
| 1 | GUESS WHAT BITCH, WE BACK HOE! | 2:58 |  |
| 2 | HERMANOS | 4:25 |  |
| 3 | TELL ME WHERE TO GO | 2:53 |  |
| 4 | NO! NO! NO! NO! NO! NO! NO! NO! NO! NO! NO! NO! NO! NO! NO! NO! NO! NO! NO! NO! NO! NO! NO! NO! NO! NO! | 5:05 |  |
