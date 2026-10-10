---
title: "The Land Is Inhospitable and So Are We"
artist: "Mitski"
year: 2023
tidal_id: 304555200
tags:
  - Indiefolk
  - Americana
  - Chamberpop
  - Singersongwriter
rating:
---

# The Land Is Inhospitable and So Are We
**Artist:** Mitski
**Year:** 2023

![[_covers/Mitski - The Land Is Inhospitable and So Are We.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/304555200
```
^button-5syl
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Mitski%20The%20Land%20Is%20Inhospitable%20and%20So%20Are%20We
```
^button-ac6f

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
| 1 | Bug Like an Angel | 3:32 |  |
| 2 | Buffalo Replaced | 2:40 |  |
| 3 | Heaven | 3:44 |  |
| 4 | I Don’t Like My Mind | 2:25 |  |
| 5 | The Deal | 3:52 |  |
| 6 | When Memories Snow | 1:44 |  |
| 7 | My Love Mine All Mine | 2:17 |  |
| 8 | The Frost | 2:48 |  |
| 9 | Star | 2:59 |  |
| 10 | I’m Your Man | 3:29 |  |
| 11 | I Love Me After You | 2:48 |  |
