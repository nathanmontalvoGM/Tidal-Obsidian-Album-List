---
title: "Melting Sun"
artist: "Lantlôs"
year: 2014
tidal_id: 175548943
tags:
  - Postrock
  - Postmetal
  - Shoegaze
  - Atmosphericmetal
rating:
---

# Melting Sun
**Artist:** Lantlôs
**Year:** 2014

![[_covers/Lantlôs - Melting Sun.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/175548943
```
^button-rrm2
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Lantl%C3%B4s%20Melting%20Sun
```
^button-ovu8

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
| 1-1 | Melting Sun I: Azure Chimes | 7:11 |  |
| 1-2 | Melting Sun II: Cherry Quartz | 9:39 |  |
| 1-3 | Melting Sun III: Aquamarine Towers | 8:06 |  |
| 1-4 | Melting Sun IV: Jade Fields | 6:29 |  |
| 1-5 | Melting Sun V: Oneironaut | 2:52 |  |
| 1-6 | Melting Sun VI: Golden Mind | 6:28 |  |
| 1-7 | Melting Sun VII | 6:43 |  |
| 2-1 | [studio documentary] |  |  |
