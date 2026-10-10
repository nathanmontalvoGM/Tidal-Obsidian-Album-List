---
title: "Day and Night"
artist: "Carly Rae Jepsen"
year: 2026
tidal_id: 560221929
tags:
  - Dancepop
  - Funk
  - NewJackSwing
  - Pop
rating:
---

# Day and Night
**Artist:** Carly Rae Jepsen
**Year:** 2026

![[_covers/Carly Rae Jepsen - Day and Night.jpg]]
```button
name ▶ Play on Tidal
type link
action tidal://album/560221929
```
^button-pqnw
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Carly%20Rae%20Jepsen%20Day%20and%20Night
```
^button-aqjo

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
| 1-1 | After All | 4:12 |  |
| 1-2 | Habits of Creatures | 2:57 |  |
| 1-3 | Versailles | 3:14 |  |
| 1-4 | On Wires | 3:22 |  |
| 1-5 | Blue Skies | 2:29 |  |
| 1-6 | Burning Heart | 3:30 |  |
| 1-7 | Wild Child | 3:49 |  |
| 1-8 | Good Fine Alright | 4:09 |  |
| 1-9 | Something Tragic | 2:57 |  |
| 1-10 | Soft | 3:03 |  |
| 1-11 | Lonely Side of the Bed | 3:30 |  |
| 1-12 | Just a Little Walk on the Moon | 3:48 |  |
| 2-1 | Never Let a Good Thing Die | 5:19 |  |
| 2-2 | Amalfi Coast | 2:59 |  |
| 2-3 | Patience Power Passion | 3:29 |  |
| 2-4 | Don’t Leave Me on the Dance Floor | 3:13 |  |
| 2-5 | Motivation | 3:53 |  |
| 2-6 | You Don’t Know How It Feels | 3:14 |  |
| 2-7 | Near or Far | 3:17 |  |
| 2-8 | Diver | 3:06 |  |
| 2-9 | Hold Me to the Light | 3:56 |  |
| 2-10 | That’s Just Me | 3:42 |  |
| 2-11 | No Labels, I Love You | 3:40 |  |
| 2-12 | Super Sage | 4:01 |  |
| 2-13 | Day and Night | 0:21 |  |
