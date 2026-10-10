---
title: "GLOW ON"
artist: "Turnstile"
year: 2021
tidal_id: 193913258
tags:
  - HardcorePunk
  - Alternativerock
  - Posthardcore
  - Hardcore
rating:
---

# GLOW ON
**Artist:** Turnstile
**Year:** 2021

![[_covers/Turnstile - GLOW ON.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/193913258
```
^button-uhq2
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Turnstile%20GLOW%20ON
```
^button-p6as

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
| 1 | MYSTERY | 2:35 |  |
| 2 | BLACKOUT | 2:53 |  |
| 3 | DON’T PLAY | 2:13 |  |
| 4 | UNDERWATER BOI | 3:04 |  |
| 5 | HOLIDAY | 2:52 |  |
| 6 | HUMANOID / SHAKE IT UP | 1:09 |  |
| 7 | ENDLESS | 1:58 |  |
| 8 | FLY AGAIN | 2:31 |  |
| 9 | ALIEN LOVE CALL | 2:55 |  |
| 10 | WILD WRLD | 2:54 |  |
| 11 | DANCE‐OFF | 2:09 |  |
| 12 | NEW HEART DESIGN | 2:27 |  |
| 13 | T.L.C. (TURNSTILE LOVE CONNECTION) | 1:42 |  |
| 14 | NO SURPRISE | 0:45 |  |
| 15 | LONELY DEZIRES | 2:43 |  |
