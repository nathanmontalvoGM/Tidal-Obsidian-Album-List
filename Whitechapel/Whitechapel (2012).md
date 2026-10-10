---
title: "Whitechapel"
artist: "Whitechapel"
year: 2012
tidal_id: 23908493
tags:
  - Mathmetal
  - Deathcore
rating:
---

# Whitechapel
**Artist:** Whitechapel
**Year:** 2012

![[_covers/Whitechapel - Whitechapel.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/23908493
```
^button-104t
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Whitechapel%20Whitechapel
```
^button-froi

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
| 1-1 | Make It Bleed | 4:12 |  |
| 1-2 | Hate Creation | 3:28 |  |
| 1-3 | (Cult)uralist | 3:42 |  |
| 1-4 | I, Dementia | 4:43 |  |
| 1-5 | Section 8 | 4:25 |  |
| 1-6 | Faces | 3:12 |  |
| 1-7 | Dead Silence | 4:38 |  |
| 1-8 | The Night Remains | 2:58 |  |
| 1-9 | Devoid | 2:50 |  |
| 1-10 | Possibilities of an Impossible Existence | 4:00 |  |
| 2-1 | Section 8 | 4:26 |  |
| 2-2 | Strength Beyond Strength | 3:47 |  |
| 2-3 | Breeding Violence (Big Chocolate remix) | 2:52 |  |
| 2-4 | This Is Exile (Ben Weinman remix) | 3:15 |  |
| 2-5 | End of Flesh (acoustic) | 4:19 |  |
