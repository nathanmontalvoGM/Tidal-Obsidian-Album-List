---
title: "You Will Never Be One of Us"
artist: "Nails"
year: 2016
tidal_id: 106187583
tags:
  - Grindcore
  - Powerviolence
  - CrustPunk
  - Mathmetal
rating:
---

# You Will Never Be One of Us
**Artist:** Nails
**Year:** 2016

![[_covers/Nails - You Will Never Be One of Us.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/106187583
```
^button-bto9
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Nails%20You%20Will%20Never%20Be%20One%20of%20Us
```
^button-co9x

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
| 1 | You Will Never Be One of Us | 1:29 |  |
| 2 | Friend to All | 0:45 |  |
| 3 | Made to Make You Fail | 0:55 |  |
| 4 | Life Is a Death Sentence | 1:39 |  |
| 5 | Violence Is Forever | 3:26 |  |
| 6 | Savage Intolerance | 1:46 |  |
| 7 | In Pain | 1:01 |  |
| 8 | Parasite | 0:55 |  |
| 9 | Into Quietus | 1:33 |  |
| 10 | They Come Crawling Back | 8:14 |  |
