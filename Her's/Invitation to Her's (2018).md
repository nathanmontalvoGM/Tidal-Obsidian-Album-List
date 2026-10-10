---
title: "Invitation to Her's"
artist: "Her's"
year: 2018
tidal_id: 89171500
tags:
  - Indie
  - Indiepop
  - Postpunk
  - Spinnyssillies
rating:
---

# Invitation to Her's
**Artist:** Her's
**Year:** 2018

![[_covers/Her's - Invitation to Her's.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/89171500
```
^button-effq
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Her%27s%20Invitation%20to%20Her%27s
```
^button-fkk3

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
| 1 | Harvey | 3:31 |  |
| 2 | Mannie’s Smile | 3:40 |  |
| 3 | If You Know What’s Right | 3:20 |  |
| 4 | Carry the Doubt | 4:41 |  |
| 5 | Low Beam | 4:28 |  |
| 6 | Breathing Easy | 4:49 |  |
| 7 | Blue Lips | 3:42 |  |
| 8 | She Needs Him | 5:14 |  |
| 9 | Love on the Line (Call Now) | 3:10 |  |
| 10 | Don’t Think It Over | 4:06 |  |
| 11 | Under Wraps | 5:03 |  |
