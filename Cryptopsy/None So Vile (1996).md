---
title: "None So Vile"
artist: "Cryptopsy"
year: 1996
tidal_id: 18517462
tags:
  - Mathmetal
  - Technicaldeathmetal
  - Brutaldeathmetal
  - Numetal
rating:
---

# None So Vile
**Artist:** Cryptopsy
**Year:** 1996

![[_covers/Cryptopsy - None So Vile.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/18517462
```
^button-ymb3
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Cryptopsy%20None%20So%20Vile
```
^button-tuvg

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
| 1 | Crown of Horns | 3:57 |  |
| 2 | Slit Your Guts | 4:02 |  |
| 3 | Graves of the Fathers | 4:11 |  |
| 4 | Dead and Dripping | 3:53 |  |
| 5 | Benedictine Convulsions | 4:00 |  |
| 6 | Phobophile | 4:38 |  |
| 7 | Lichmistress | 2:31 |  |
| 8 | Orgiastic Disembowelment | 4:51 |  |
