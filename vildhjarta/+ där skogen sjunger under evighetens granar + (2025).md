---
title: "+ där skogen sjunger under evighetens granar +"
artist: "vildhjarta"
year: 2025
tidal_id: 419257960
tags:
  - Progressivemetal
rating:
---

# + där skogen sjunger under evighetens granar +
**Artist:** vildhjarta
**Year:** 2025

![[_covers/vildhjarta - + där skogen sjunger under evighetens granar +.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/419257960
```
^button-spm4
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=vildhjarta%20%2B%20d%C3%A4r%20skogen%20sjunger%20under%20evighetens%20granar%20%2B
```
^button-vgex

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
| 1 | + byta ut alla stjärnor på himlen mot plustecken + | 3:45 |  |
| 2 | + två vackra svanar + | 5:13 |  |
| 3 | + sargasso + | 6:45 |  |
| 4 | + ylva + | 4:41 |  |
| 5 | + där mossan möter havet + | 3:48 |  |
| 6 | + röda läppar, söta äpplen + | 3:48 |  |
| 7 | + kristallfågel + | 4:03 |  |
| 8 | + ? regnet, the ? + | 3:30 |  |
| 9 | + hösten som togs ifrån mig + | 3:49 |  |
| 10 | + viktlös & evig + | 6:39 |  |
| 11 | + stjärnblödning + | 3:28 |  |
| 12 | + den spanska känslan + | 7:26 |  |
