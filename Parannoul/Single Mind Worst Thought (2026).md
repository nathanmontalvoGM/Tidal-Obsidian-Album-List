---
title: "Single Mind Worst Thought"
artist: "Parannoul"
year: 2026
tidal_id: 561624017
tags: []
rating:
---

# Single Mind Worst Thought
**Artist:** Parannoul
**Year:** 2026

![[_covers/Parannoul - Single Mind Worst Thought.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/561624017
```
^button-6jcx
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Parannoul%20Single%20Mind%20Worst%20Thought
```
^button-22f7

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
| 1 | Remaining | 5:17 |  |
| 2 | Firebreak | 4:30 |  |
| 3 | Sleepwalking Club | 4:45 |  |
| 4 | To Home | 4:16 |  |
