var button = document.createElement("button");
var text = document.createTextNode("Klikkaa tästä!");
button.appendChild(text);
button.style.background = "#5babecff";
button.style.fontSize = "22px"
button.style.height = "100px"
button.style.width = "300px"
document.body.appendChild(button);
button.onclick = click

function click() {
    alert("Moi JavaScriptaus!");
}