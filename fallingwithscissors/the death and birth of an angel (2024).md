---
title: "the death and birth of an angel"
artist: "fallingwithscissors"
year: 2024
tidal_id: 336232628
tags:
  - Metalcore
  - Breakcore
  - Cybergrind
  - Screamo
rating:
---

# the death and birth of an angel
**Artist:** fallingwithscissors
**Year:** 2024

![[_covers/fallingwithscissors - the death and birth of an angel.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/336232628
```
^button-i4le
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=fallingwithscissors%20the%20death%20and%20birth%20of%20an%20angel
```
^button-et5z

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
| 1 | 01100110011000010110110001101100 | 1:28 |  |
| 2 | gh0st.shell | 0:53 |  |
| 3 | Atrophy:Angel | 3:03 |  |
| 4 | blissful | 2:00 |  |
| 5 | (un)equivalent_exchange | 3:00 |  |
| 6 | tripping > wires | 3:38 |  |
| 7 | D.I.T.B. | 3:39 |  |
