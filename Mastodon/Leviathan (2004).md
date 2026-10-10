---
title: "Leviathan"
artist: "Mastodon"
year: 2004
tidal_id: 2826055
tags:
  - Progressivemetal
  - Whalecore
  - SludgeMetal
  - Numetal
rating:
---

# Leviathan
**Artist:** Mastodon
**Year:** 2004

![[_covers/Mastodon - Leviathan.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/2826055
```
^button-y8wf
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Mastodon%20Leviathan
```
^button-klyt

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
| 1 | Blood and Thunder | 3:48 |  |
| 2 | I Am Ahab | 2:45 |  |
| 3 | Seabeast | 4:15 |  |
| 4 | Ísland | 3:26 |  |
| 5 | Iron Tusk | 3:03 |  |
| 6 | Megalodon | 4:22 |  |
| 7 | Naked Burn | 3:42 |  |
| 8 | Aqua Dementia | 4:10 |  |
| 9 | Hearts Alive | 13:40 |  |
| 10 | Joseph Merrick | 3:33 |  |
