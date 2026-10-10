---
title: "Fearless"
artist: "Crown Lands"
year: 2023
tidal_id: 284673445
tags:
  - Progressivepop
  - Rock
rating:
---

# Fearless
**Artist:** Crown Lands
**Year:** 2023

![[_covers/Crown Lands - Fearless.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/284673445
```
^button-ef0t
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Crown%20Lands%20Fearless
```
^button-yqql

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
| 1-1 | Starlifter - Fearless Pt. II: Overture / Begin Transmission / Fearless Awakens / Departure / The Journey / Interfacing the Machine / Requiem / The Battle of Starlifter / Event Horizon | 18:22 |  |
| 1-2 | Dreamer of the Dawn | 4:03 |  |
| 1-3 | The Shadow | 3:44 |  |
| 1-4 | Right Way Back | 3:51 |  |
| 1-5 | Context: Fearless Pt. I | 7:49 |  |
| 2-1 | Reflections | 5:43 |  |
| 2-2 | Penny | 3:42 |  |
| 2-3 | Lady of the Lake | 5:06 |  |
| 2-4 | Citadel | 5:52 |  |
