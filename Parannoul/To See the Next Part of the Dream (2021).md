---
title: "To See the Next Part of the Dream"
artist: "Parannoul"
year: 2021
tidal_id: 180892435
tags:
  - Shoegaze
  - Emo
  - Postrock
  - Posthardcore
rating:
---

# To See the Next Part of the Dream
**Artist:** Parannoul
**Year:** 2021

![[_covers/Parannoul - To See the Next Part of the Dream.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/180892435
```
^button-0f53
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Parannoul%20To%20See%20the%20Next%20Part%20of%20the%20Dream
```
^button-msbz

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
| 1 | 아름다운 세상 (Beautiful World) | 5:20 |  |
| 2 | 변명 (Excuse) | 5:51 |  |
| 3 | 아날로그 센티멘탈리즘 (Analog Sentimentalism) | 4:24 |  |
| 4 | 흰천장 (White Ceiling) | 10:00 |  |
| 5 | To See the Next Part of the Dream | 5:07 |  |
| 6 | 격변의 시대 (Age of Fluctuation) | 9:20 |  |
| 7 | 청춘반란 (Youth Rebellion) | 7:00 |  |
| 8 | 엑스트라 일대기 (Extra Story) | 2:59 |  |
| 9 | Chicken | 6:00 |  |
| 10 | I Can Feel My Heart Touching You | 5:36 |  |
