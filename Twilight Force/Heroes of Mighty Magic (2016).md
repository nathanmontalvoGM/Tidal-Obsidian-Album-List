---
title: Heroes of Mighty Magic
artist: Twilight Force
year: 2016
tidal_id: 107100715
tags:
  - Symphonicmetal
  - Powermetal
  - Disneymetal
rating:
---

# Heroes of Mighty Magic
**Artist:** Twilight Force
**Year:** 2016

![[_covers/Twilight Force - Heroes of Mighty Magic.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/107100715
```
^button-opkj
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Twilight%20Force%20Heroes%20of%20Mighty%20Magic
```
^button-m9fe

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
| 1-1 | Battle of Arcane Might | 5:06 |  |
| 1-2 | Powerwind | 5:16 |  |
| 1-3 | Guardian of the Seas | 5:38 |  |
| 1-4 | Flight of the Sapphire Dragon | 5:40 |  |
| 1-5 | There and Back Again | 10:14 |  |
| 1-6 | Riders of the Dawn | 3:46 |  |
| 1-7 | Keepers of Fate | 5:38 |  |
| 1-8 | Rise of a Hero | 5:13 |  |
| 1-9 | To the Stars | 5:32 |  |
| 1-10 | Heroes of Mighty Magic | 9:57 |  |
| 1-11 | Epilogue | 6:39 |  |
| 1-12 | Knights of Twilight's Might | 1:45 |  |
| 2-1 | Rise of a Hero (orchestral version) | 5:13 |  |
| 2-2 | Flight of the Sapphire Dragon (orchestral version) | 5:40 |  |
| 2-3 | Heroes of Mighty Magic (orchestral version) | 9:54 |  |
| 2-4 | Battle of Arcane Might (karaoke version) | 5:06 |  |
| 2-5 | There and Back Again (short version) | 4:58 |  |
| 2-6 | Powerwind (chip version) | 4:37 |  |
