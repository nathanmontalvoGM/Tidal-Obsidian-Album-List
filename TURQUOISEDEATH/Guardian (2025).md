---
title: "Guardian"
artist: "TURQUOISEDEATH"
year: 2025
tidal_id: 444820962
tags:
  - Progressivebreaks
  - Atmosphericdrumandbass
  - DrumAndBass
  - Breakbeat
rating:
---

# Guardian
**Artist:** TURQUOISEDEATH
**Year:** 2025

![[_covers/TURQUOISEDEATH - Guardian.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/444820962
```
^button-l4w6
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=TURQUOISEDEATH%20Guardian
```
^button-19p3

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
| 1 | Univa Transporter | 3:10 |  |
| 2 | Canyon of Secrets | 9:01 |  |
| 3 | Voyager | 6:23 |  |
| 4 | Guardian Surface | 7:28 |  |
| 5 | The Looking Glass | 9:27 |  |
| 6 | Close Your Eyes | 30:00 |  |
