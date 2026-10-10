---
title: "Giles Corey"
artist: "Giles Corey"
year: 2016
tidal_id: 65229453
tags:
  - Singersongwriter
  - Slowcore
  - Contemporaryfolk
  - Indiefolk
rating:
---

# Giles Corey
**Artist:** Giles Corey
**Year:** 2016

![[_covers/Giles Corey - Giles Corey.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/65229453
```
^button-emqg
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Giles%20Corey%20Giles%20Corey
```
^button-uxtj

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
| 1 | The Haunting Presence | 7:56 |  |
| 2 | Blackest Bile | 7:00 |  |
| 3 | Grave Filled With Books | 4:01 |  |
| 4 | Empty Churches | 5:41 |  |
| 5 | I’m Going to Do It | 6:15 |  |
| 6 | Spectral Bride | 7:10 |  |
| 7 | No One Is Ever Going to Want Me | 8:13 |  |
| 8 | Sleeping Heart | 3:28 |  |
| 9 | Buried Above Ground | 6:27 |  |
