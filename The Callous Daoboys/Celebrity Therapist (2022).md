---
title: "Celebrity Therapist"
artist: "The Callous Daoboys"
year: 2022
tidal_id: 333894014
tags:
  - Mathcore
  - Chaotichardcore
  - Bestof2022
  - Ohiamsoquirkyahahah
rating:
---

# Celebrity Therapist
**Artist:** The Callous Daoboys
**Year:** 2022

![[_covers/The Callous Daoboys - Celebrity Therapist.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/333894014
```
^button-7ikt
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=The%20Callous%20Daoboys%20Celebrity%20Therapist
```
^button-l43l

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
| 1 | Violent Astrology | 4:43 |  |
| 2 | A Brief Article Regarding Time Loops | 3:17 |  |
| 3 | Beautiful Dude Missile | 2:52 |  |
| 4 | Title Track | 6:36 |  |
| 5 | Field Sobriety Practice | 5:56 |  |
| 6 | The Elephant Man in the Room | 4:16 |  |
| 7 | What Is Delicious? Who Swarms? | 3:16 |  |
| 8 | Star Baby | 5:37 |  |
