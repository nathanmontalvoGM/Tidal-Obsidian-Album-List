---
title: "Cacophony"
artist: "Gumshoes"
year: 2024
tidal_id: 336975269
tags:
  - Indiepop
  - Chamberpop
  - Pianorock
  - Bedroompop
rating:
---

# Cacophony
**Artist:** Gumshoes
**Year:** 2024

![[_covers/Gumshoes - Cacophony.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/336975269
```
^button-vn2e
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Gumshoes%20Cacophony
```
^button-0k3c

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
| 1 | Cacophony | 3:27 |  |
| 2 | The Real Thing | 4:07 |  |
| 3 | Clair De Lune 2 | 3:58 |  |
| 4 | One Fine Specimen | 3:58 |  |
| 5 | Nobodies | 5:40 |  |
| 6 | Low Fantasy | 3:09 |  |
| 7 | The Puppet Waltz | 4:52 |  |
| 8 | Last Living Kennedy | 7:29 |  |
