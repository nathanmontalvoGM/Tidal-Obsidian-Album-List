---
title: "From Mars to Sirius"
artist: "Gojira"
year: 2006
tidal_id: 13929179
tags:
  - Progressivemetal
  - Mathmetal
  - Numetal
  - Whalecore
rating:
---

# From Mars to Sirius
**Artist:** Gojira
**Year:** 2006

![[_covers/Gojira - From Mars to Sirius.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/13929179
```
^button-3ol9
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Gojira%20From%20Mars%20to%20Sirius
```
^button-zfo5

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
| 1 | Ocean Planet | 5:32 |  |
| 2 | Backbone | 4:18 |  |
| 3 | From the Sky | 5:48 |  |
| 4 | Unicorn | 2:09 |  |
| 5 | Where Dragons Dwell | 6:54 |  |
| 6 | The Heaviest Matter of the Universe | 3:57 |  |
| 7 | Flying Whales | 7:44 |  |
| 8 | In the Wilderness | 7:47 |  |
| 9 | World to Come | 6:52 |  |
| 10 | From Mars | 2:24 |  |
| 11 | To Sirius | 5:37 |  |
| 12 | Global Warming | 7:50 |  |
