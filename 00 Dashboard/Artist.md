```dataviewjs
// Shows every album by the artist you last tapped on an album page.
const artist = app.loadLocalStorage("music-artist");
if (artist) await dv.view("_scripts/playlist", { artist });
else dv.paragraph("Open an album and tap the artist's name to see all of their albums here.");
```
