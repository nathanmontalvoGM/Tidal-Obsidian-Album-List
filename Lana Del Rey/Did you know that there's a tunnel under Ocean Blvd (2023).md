---
title: "Did you know that there's a tunnel under Ocean Blvd"
artist: "Lana Del Rey"
year: 2023
tidal_id: 283735625
tags:
  - Singersongwriter
  - Neopsychedelia
  - Pop
  - ArtPop
rating:
---

# Did you know that there's a tunnel under Ocean Blvd
**Artist:** Lana Del Rey
**Year:** 2023

![[_covers/Lana Del Rey - Did you know that there's a tunnel under Ocean Blvd.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/283735625
```
^button-es4b
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Lana%20Del%20Rey%20Did%20you%20know%20that%20there%27s%20a%20tunnel%20under%20Ocean%20Blvd
```
^button-de9c

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
| 1 | The Grants | 4:55 |  |
| 2 | Did you know that there’s a tunnel under Ocean Blvd | 4:45 |  |
| 3 | Sweet | 3:35 |  |
| 4 | A&W | 7:14 |  |
| 5 | Judah Smith Interlude | 4:37 |  |
| 6 | Candy Necklace | 5:15 |  |
| 7 | Jon Batiste Interlude | 3:33 |  |
| 8 | Kintsugi | 6:19 |  |
| 9 | Fingertips | 5:48 |  |
| 10 | Paris, Texas | 3:27 |  |
| 11 | Grandfather please stand on the shoulders of my father while he’s deep‐sea fishing | 4:00 |  |
| 12 | Let the Light In | 4:38 |  |
| 13 | Margaret | 5:40 |  |
| 14 | Fishtail | 4:03 |  |
| 15 | Peppers | 4:09 |  |
| 16 | Taco Truck × VB | 5:53 |  |
