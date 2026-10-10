---
title: "So Much Country ‘Till We Get There"
artist: "Westside Cowboy"
year: 2026
tidal_id: 488297983
tags:
  - Rock
  - Indie
  - Alternativerock
  - Indierock
rating:
---

# So Much Country ‘Till We Get There
**Artist:** Westside Cowboy
**Year:** 2026

![[_covers/Westside Cowboy - So Much Country ‘Till We Get There.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/488297983
```
^button-oxaj
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Westside%20Cowboy%20So%20Much%20Country%20%E2%80%98Till%20We%20Get%20There
```
^button-tokr

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
| 1 | Strange Taxidermy | 4:52 |  |
| 2 | Can’t See | 2:26 |  |
| 3 | Don’t Throw Rocks | 3:01 |  |
| 4 | The Wahs | 2:24 |  |
| 5 | In the Morning | 1:52 |  |
