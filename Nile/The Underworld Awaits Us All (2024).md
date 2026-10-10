---
title: "The Underworld Awaits Us All"
artist: "Nile"
year: 2024
tidal_id: 360871049
tags:
  - Technicaldeathmetal
  - Mathmetal
  - Brutaldeathmetal
  - Numetal
rating:
---

# The Underworld Awaits Us All
**Artist:** Nile
**Year:** 2024

![[_covers/Nile - The Underworld Awaits Us All.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/360871049
```
^button-siat
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Nile%20The%20Underworld%20Awaits%20Us%20All
```
^button-indp

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
| 1 | Stelae of Vultures | 6:19 |  |
| 2 | Chapter for Not Being Hung Upside Down on a Stake in the Underworld and Made to Eat Feces by the Four Apes | 3:50 |  |
| 3 | To Strike With Secret Fang | 1:58 |  |
| 4 | Naqada II Enter the Golden Age | 5:27 |  |
| 5 | The Pentagrammathion of Nephren‐Ka | 1:18 |  |
| 6 | Overlords of the Black Earth | 4:44 |  |
| 7 | Under the Curse of the One God | 4:45 |  |
| 8 | Doctrine of Last Things | 4:39 |  |
| 9 | True Gods of the Desert | 7:08 |  |
| 10 | The Underworld Awaits Us All | 8:36 |  |
| 11 | Lament for the Destruction of Time | 4:50 |  |
