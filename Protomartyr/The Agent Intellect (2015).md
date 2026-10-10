---
title: "The Agent Intellect"
artist: "Protomartyr"
year: 2015
tidal_id: 51799226
tags:
  - Postpunk
rating:
---

# The Agent Intellect
**Artist:** Protomartyr
**Year:** 2015

![[_covers/Protomartyr - The Agent Intellect.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/51799226
```
^button-9q52
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Protomartyr%20The%20Agent%20Intellect
```
^button-xu3f

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
| 1 | The Devil in His Youth | 2:37 |  |
| 2 | Cowards Starve | 3:36 |  |
| 3 | I Forgive You | 3:01 |  |
| 4 | Boyce or Boice | 3:37 |  |
| 5 | Pontiac 87 | 4:31 |  |
| 6 | Uncle Mother’s | 4:19 |  |
| 7 | Dope Cloud | 2:56 |  |
| 8 | The Hermit | 2:32 |  |
| 9 | Clandestine Time | 3:07 |  |
| 10 | Why Does It Shake? | 4:45 |  |
| 11 | Ellen | 6:22 |  |
| 12 | Feast of Stephen | 2:24 |  |
