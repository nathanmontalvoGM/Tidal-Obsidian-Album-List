---
title: Pain Remains
artist: Lorna Shore
year: 2022
tidal_id: 236075892
tags:
  - Favorite
  - Blackeneddeathcore
  - Deathcore
  - Bestof2022
  - Hardcore
rating:
---

# Pain Remains
**Artist:** Lorna Shore
**Year:** 2022

![[_covers/Lorna Shore - Pain Remains.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/236075892
```
^button-6ugp
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Lorna%20Shore%20Pain%20Remains
```
^button-fn3y

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
| 1 | Welcome Back, O’ Sleeping Dreamer | 7:21 |  |
| 2 | Into the Earth | 5:12 |  |
| 3 | Sun//Eater | 6:11 |  |
| 4 | Cursed to Die | 4:40 |  |
| 5 | Soulless Existence | 7:13 |  |
| 6 | Apotheosis | 4:55 |  |
| 7 | Wrath | 4:57 |  |
| 8 | Pain Remains I: Dancing Like Flames | 5:53 |  |
| 9 | Pain Remains II: After All I’ve Done, I’ll Disappear | 5:37 |  |
| 10 | Pain Remains III: In a Sea of Fire | 9:12 |  |
