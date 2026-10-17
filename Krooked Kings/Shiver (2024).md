```dataviewjs
  await dv.view("_scripts/album");
```

---
title: Shiver
artist: Krooked Kings
year: 2024
tidal_id: 314870321
tags:
  - Indierock
rating:
---

# Shiver
**Artist:** Krooked Kings
**Year:** 2024

![[_covers/Krooked Kings - Shiver.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/314870321
```
^button-pg4u
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Krooked%20Kings%20Shiver
```
^button-8e46

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
| 1 | Letter to a Past Self | 3:56 |  |
| 2 | On Again, Off Again | 3:46 |  |
| 3 | Catacombs | 2:56 |  |
| 4 | Snake Bite | 3:04 |  |
| 5 | Headhunters | 3:04 |  |
| 6 | Memory Loss | 3:31 |  |
| 7 | Holy Ghost | 3:30 |  |
| 8 | Roll Credits | 4:33 |  |
