---
title: "Get To Heaven"
artist: "Everything Everything"
year: 2015
tidal_id: 63101777
tags:
  - ArtPop
  - Progressivepop
  - Indietronica
  - Indiepop
rating:
---

# Get To Heaven
**Artist:** Everything Everything
**Year:** 2015

![[_covers/Everything Everything - Get To Heaven.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/63101777
```
^button-nrnv
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Everything%20Everything%20Get%20To%20Heaven
```
^button-zsec

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
| 1 | To the Blade | 4:13 |  |
| 2 | Distant Past | 3:41 |  |
| 3 | Get to Heaven | 3:43 |  |
| 4 | Regret | 3:22 |  |
| 5 | Spring / Sun / Winter / Dread | 3:18 |  |
| 6 | The Wheel (Is Turning Now) | 5:28 |  |
| 7 | Fortune 500 | 4:16 |  |
| 8 | Blast Doors | 3:30 |  |
| 9 | Zero Pharaoh | 3:39 |  |
| 10 | No Reptiles | 4:42 |  |
| 11 | Warm Healer | 6:10 |  |
| 12 | We Sleep in Pairs | 3:22 |  |
| 13 | Hapsburg Lippp | 3:39 |  |
| 14 | President Heartbeat | 3:21 |  |
| 15 | Brainchild | 3:51 |  |
| 16 | Yuppie Supper | 3:33 |  |
| 17 | Only as Good as My God | 3:35 |  |
