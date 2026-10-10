---
title: "Altered State"
artist: "TesseracT"
year: 2013
tidal_id: 52105466
tags:
  - Djent
  - Progressivemetal
  - Mathmetal
  - Numetal
rating:
---

# Altered State
**Artist:** TesseracT
**Year:** 2013

![[_covers/TesseracT - Altered State.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/52105466
```
^button-md17
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=TesseracT%20Altered%20State
```
^button-0ukb

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
| 1 | Of Matter – Proxy | 5:05 |  |
| 2 | Of Matter – Retrospect | 5:32 |  |
| 3 | Of Matter – Resist | 3:40 |  |
| 4 | Of Mind – Nocturne | 5:50 |  |
| 5 | Of Mind – Exile | 8:50 |  |
| 6 | Of Reality – Eclipse | 5:03 |  |
| 7 | Of Reality – Palingenesis | 2:46 |  |
| 8 | Of Reality – Calabi‐Yau | 2:00 |  |
| 9 | Of Energy – Singularity | 8:21 |  |
| 10 | Of Energy – Embers | 3:36 |  |
