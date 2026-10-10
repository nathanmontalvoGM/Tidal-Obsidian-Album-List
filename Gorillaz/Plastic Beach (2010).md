---
title: "Plastic Beach"
artist: "Gorillaz"
year: 2010
tidal_id: 71109496
tags:
  - Electronicore
  - Alternativerock
  - Rock
  - Pop
rating:
---

# Plastic Beach
**Artist:** Gorillaz
**Year:** 2010

![[_covers/Gorillaz - Plastic Beach.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/71109496
```
^button-9o47
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Gorillaz%20Plastic%20Beach
```
^button-o6a7

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
| 1-1 | Orchestral Intro | 1:09 |  |
| 1-2 | Welcome to the World of the Plastic Beach | 3:35 |  |
| 1-3 | White Flag | 3:43 |  |
| 1-4 | Rhinestone Eyes | 3:20 |  |
| 1-5 | Stylo | 4:30 |  |
| 1-6 | Superfast Jellyfish | 2:54 |  |
| 1-7 | Empire Ants | 4:43 |  |
| 1-8 | Glitter Freeze | 4:03 |  |
| 1-9 | Some Kind of Nature | 2:59 |  |
| 1-10 | On Melancholy Hill | 3:53 |  |
| 1-11 | Broken | 3:17 |  |
| 1-12 | Sweepstakes | 5:20 |  |
| 1-13 | Plastic Beach | 3:47 |  |
| 1-14 | To Binge | 3:55 |  |
| 1-15 | Cloud of Unknowing | 3:06 |  |
| 1-16 | Pirate Jet | 2:32 |  |
| 2-1 | The Making of Plastic Beach Documentary | 45:00 |  |
