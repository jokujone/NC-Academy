function init() {
  window.requestAnimationFrame(draw);
}

button1.onclick = function() {
    canvas.style.visibility = "visible";
    setTimeout(showDiv2, 3000);
}

function showDiv2() {
    div2.style.visibility = "visible";

    setTimeout(showBeauty, 1000);
}
function showBeauty() {
    beauty.style.visibility = "visible";
    setTimeout(showRounddiv, 2000);
}

function showRounddiv() {
    rounddiv.style.visibility = "visible";
}


const canvas = document.getElementById("canvas");
const div2 = document.getElementById("div2");
const beauty = document.getElementById("beauty");
const rounddiv = document.getElementById("rounddiv");


const ctx = canvas.getContext("2d");

ctx.fillStyle = "#00a2ffff";
ctx.fillRect(0, 0, 150, 100);

const round = document.getElementById("round");
const ctx2 = round.getContext("2d");
ctx2.fillStyle = "#ff0000ff";
ctx2.beginPath();
ctx2.arc(50, 50, 50, 0, Math.PI * 2, true);
ctx2.fill();

var a = 0;
function draw() {
    if (a > Math.PI * 2) {
        a = 0;
    }
    a += 0.1;
    ctx2.globalCompositeOperation = "destination-over";
    ctx2.clearRect(0, 0, 300, 300);

    ctx2.save();

    ctx.restore();

    ctx2.fillStyle = "#ff0000ff";
    ctx2.beginPath();
    ctx2.arc(50, 50, 50, a, Math.PI * 2, true);
    ctx2.fill();

    window.requestAnimationFrame(draw);
}


init();