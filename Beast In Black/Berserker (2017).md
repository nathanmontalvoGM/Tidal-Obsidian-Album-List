---
title: "Berserker"
artist: "Beast In Black"
year: 2017
tidal_id: 107035370
tags:
  - Powermetal
  - Heavymetal
  - Numetal
  - Epicbutnotcheesy
rating:
---

# Berserker
**Artist:** Beast In Black
**Year:** 2017

![[_covers/Beast In Black - Berserker.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/107035370
```
^button-qgob
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Beast%20In%20Black%20Berserker
```
^button-xula

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
| 1 | Beast in Black | 4:29 |  |
| 2 | Blind and Frozen | 5:04 |  |
| 3 | Blood of a Lion | 5:03 |  |
| 4 | Born Again | 3:51 |  |
| 5 | Zodd the Immortal | 3:34 |  |
| 6 | The Fifth Angel | 3:30 |  |
| 7 | Crazy, Mad, Insane | 3:30 |  |
| 8 | Hell for All Eternity | 4:48 |  |
| 9 | Eternal Fire | 3:34 |  |
| 10 | Go to Hell | 3:01 |  |
| 11 | End of the World | 5:10 |  |
| 12 | Ghost in the Rain | 5:35 |  |
