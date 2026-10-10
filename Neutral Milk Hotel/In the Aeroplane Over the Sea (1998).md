---
title: "In the Aeroplane Over the Sea"
artist: "Neutral Milk Hotel"
year: 1998
tidal_id: 37265686
tags:
  - Indie
  - Indierock
  - Folk
  - Mmmnmn
rating:
---

# In the Aeroplane Over the Sea
**Artist:** Neutral Milk Hotel
**Year:** 1998

![[_covers/Neutral Milk Hotel - In the Aeroplane Over the Sea.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/37265686
```
^button-ls6u
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Neutral%20Milk%20Hotel%20In%20the%20Aeroplane%20Over%20the%20Sea
```
^button-kw15

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
| 1 | The King of Carrot Flowers, Pt. One | 2:00 |  |
| 2 | The King of Carrot Flowers, Pts. Two & Three | 3:06 |  |
| 3 | In the Aeroplane Over the Sea | 3:22 |  |
| 4 | Two-Headed Boy | 4:26 |  |
| 5 | The Fool | 1:53 |  |
| 6 | Holland, 1945 | 3:12 |  |
| 7 | Communist Daughter | 1:57 |  |
| 8 | Oh Comely | 8:18 |  |
| 9 | Ghost | 4:08 |  |
| 10 | [untitled] | 2:16 |  |
| 11 | Two-Headed Boy, Pt. Two | 5:13 |  |
