```dataviewjs
const btn = dv.container.createEl("a");
btn.textContent = "Library";
btn.style.cssText = `
    display: inline-block;
    padding: 10px 20px;
    background: #7c3aed;
    color: #fff;
    border-radius: 10px;
    font-size: 15px;
    font-weight: bold;
    text-decoration: none;
    cursor: pointer;
    margin-bottom: 16px;
`;
btn.onclick = (e) => {
    e.preventDefault();
    app.workspace.openLinkText("Library", "", false);
};
```
```button
name ▶ Play on Tidal
type link
action tidal://album/256082707
```
^button-lqrn
```button
name Search on Album of the Year
type link
action https://www.albumoftheyear.org/search/?q=Anamanaguchi%20%5BUSA%5D
```
^button-vmeh