---
title: "Not for Want of Trying"
artist: "Maybeshewill"
year: 2008
tidal_id: 53868188
tags:
  - Electronicore
  - Experimentalrock
  - Postrock
  - Rock
rating:
---

# Not for Want of Trying
**Artist:** Maybeshewill
**Year:** 2008

![[_covers/Maybeshewill - Not for Want of Trying.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/53868188
```
^button-n2o9
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Maybeshewill%20Not%20for%20Want%20of%20Trying
```
^button-ha6v

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
| 1 | Ixnay on the Autoplay | 1:42 |  |
| 2 | Seraphim & Cherubim | 3:17 |  |
| 3 | The Paris Hilton Sex Tape | 3:34 |  |
| 4 | I’m in Awe, Amadeus! | 3:39 |  |
| 5 | We Called for an Ambulance but a Fire Engine Came | 3:23 |  |
| 6 | Heartflusters | 3:48 |  |
| 7 | C.N.T.R.C.K.T. | 2:27 |  |
| 8 | He Films the Clouds Pt. 2 | 6:43 |  |
| 9 | Not for Want of Trying | 5:34 |  |
| 10 | Takotsubo | 1:49 |  |
