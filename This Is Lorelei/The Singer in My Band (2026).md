---
title: "The Singer in My Band"
artist: "This Is Lorelei"
year: 2026
tidal_id: 554024739
tags: []
rating:
---

# The Singer in My Band
**Artist:** This Is Lorelei
**Year:** 2026

![[_covers/This Is Lorelei - The Singer in My Band.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/554024739
```
^button-16lu
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=This%20Is%20Lorelei%20The%20Singer%20in%20My%20Band
```
^button-w3ti

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
| 1 | I Will Eat My Heart in the Morning Light | 3:17 |  |
| 2 | Oh No Now My | 3:08 |  |
| 3 | Billy Came Back | 3:09 |  |
| 4 | Watching Heaven Fall | 3:12 |  |
| 5 | Sailing (Your Baby's Down) | 3:32 |  |
| 6 | The Singer in My Band | 2:25 |  |
| 7 | Nitro | 1:26 |  |
| 8 | Hey Sarah Is It Gonna Rain Forever | 3:27 |  |
| 9 | The Kid With the Crown | 4:14 |  |
| 10 | And I Haven't Seen My Love in Quite a While | 3:28 |  |
| 11 | Don't You Cry in Lonesomeness | 3:18 |  |
