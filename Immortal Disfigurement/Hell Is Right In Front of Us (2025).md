---
title: "Hell Is Right In Front of Us"
artist: "Immortal Disfigurement"
year: 2025
tidal_id: 459807296
tags: []
rating:
---

# Hell Is Right In Front of Us
**Artist:** Immortal Disfigurement
**Year:** 2025

![[_covers/Immortal Disfigurement - Hell Is Right In Front of Us.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/459807296
```
^button-c2mh
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Immortal%20Disfigurement%20Hell%20Is%20Right%20In%20Front%20of%20Us
```
^button-igmp

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
| 1 | Gospel of Annihilation | 5:16 |  |
| 2 | Hellhole | 5:45 |  |
| 3 | Throne of Flies | 4:26 |  |
| 4 | Into a Dying Sun | 5:30 |  |
| 5 | Swap God(s) | 8:26 |  |
