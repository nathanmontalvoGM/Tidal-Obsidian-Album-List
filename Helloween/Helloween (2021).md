---
title: "Helloween"
artist: "Helloween"
year: 2021
tidal_id: 396320093
tags:
  - Powermetal
  - Speedmetal
  - Heavymetal
  - Numetal
rating:
---

# Helloween
**Artist:** Helloween
**Year:** 2021

![[_covers/Helloween - Helloween.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/396320093
```
^button-ipzw
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Helloween%20Helloween
```
^button-48wd

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
| 1 | Starlight | 5:18 |  |
| 2 | Murderer | 4:26 |  |
| 3 | Warrior | 4:01 |  |
| 4 | Victim of Fate | 6:38 |  |
| 5 | Cry for Freedom | 6:03 |  |
