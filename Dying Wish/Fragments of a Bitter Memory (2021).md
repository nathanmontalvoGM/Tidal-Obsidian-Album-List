---
title: "Fragments of a Bitter Memory"
artist: "Dying Wish"
year: 2021
tidal_id: 187698242
tags:
  - MelodicMetalcore
  - Metalcore
  - MelodicHardcore
  - Bestof2022
rating:
---

# Fragments of a Bitter Memory
**Artist:** Dying Wish
**Year:** 2021

![[_covers/Dying Wish - Fragments of a Bitter Memory.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/187698242
```
^button-t5sf
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Dying%20Wish%20Fragments%20of%20a%20Bitter%20Memory
```
^button-tzdz

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
| 1 | Cowards Fred, Cowards Bleed | 1:45 |  |
| 2 | Hollowed by Affliction | 3:22 |  |
| 3 | Innate Thirst | 3:15 |  |
| 4 | Severing the Senses | 2:54 |  |
| 5 | Fragments of a Bitter Memory | 3:58 |  |
| 6 | Cold Hearts in Bloom | 3:01 |  |
| 7 | Until Mourning Comes | 2:37 |  |
| 8 | Now You'll Rot | 2:45 |  |
| 9 | Blood Laced Misery | 3:40 |  |
| 10 | Enemies in Red | 4:09 |  |
| 11 | Drowning in the Silent Black | 3:41 |  |
