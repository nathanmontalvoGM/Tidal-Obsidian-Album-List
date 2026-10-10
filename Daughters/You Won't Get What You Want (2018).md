---
title: "You Won't Get What You Want"
artist: "Daughters"
year: 2018
tidal_id: 92428847
tags:
  - Noiserock
  - Industrialrock
  - Experimentalrock
  - Posthardcore
rating:
---

# You Won't Get What You Want
**Artist:** Daughters
**Year:** 2018

![[_covers/Daughters - You Won't Get What You Want.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/92428847
```
^button-78zy
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Daughters%20You%20Won%27t%20Get%20What%20You%20Want
```
^button-2fkl

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
| 1 | City Song | 5:55 |  |
| 2 | Long Road, No Turns | 5:04 |  |
| 3 | Satan in the Wait | 7:06 |  |
| 4 | The Flammable Man | 2:09 |  |
| 5 | The Lords Song | 2:45 |  |
| 6 | Less Sex | 4:47 |  |
| 7 | Daughter | 4:55 |  |
| 8 | The Reason They Hate Me | 3:55 |  |
| 9 | Ocean Song | 7:28 |  |
| 10 | Guest House | 4:29 |  |
