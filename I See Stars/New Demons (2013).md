---
title: "New Demons"
artist: "I See Stars"
year: 2013
tidal_id: 255152956
tags:
  - Posthardcore
  - Electronicore
  - Trancecore
  - Metalcore
rating:
---

# New Demons
**Artist:** I See Stars
**Year:** 2013

![[_covers/I See Stars - New Demons.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/255152956
```
^button-lm66
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=I%20See%20Stars%20New%20Demons
```
^button-9d0j

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
| 1 | Initialization Sequence | 0:53 |  |
| 2 | Ten Thousand Feet | 5:44 |  |
| 3 | Follow Your Leader | 4:46 |  |
| 4 | New Demons | 4:41 |  |
| 5 | Violent Bounce (People Like ¥øµ) | 4:39 |  |
| 6 | Murder Mitten | 5:02 |  |
| 7 | We're Not in Kansas Anymore | 4:46 |  |
| 8 | Judith Rules | 4:12 |  |
| 9 | Boris the Animal | 4:03 |  |
| 10 | Crystal Ball | 3:43 |  |
| 11 | When I Say Jump, You Say How High | 3:17 |  |
| 12 | Who Am I? | 4:28 |  |
