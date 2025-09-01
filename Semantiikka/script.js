//Tokmanni generator

const canvas = document.getElementById("logo");
const ctx = canvas.getContext("2d");

const pos = 75;
ctx.beginPath();
ctx.arc(pos * 2, pos, 65, 0, 2 * Math.PI);
ctx.fillStyle = "red";
ctx.fill();

ctx.beginPath();
ctx.arc(pos * 2, pos, 45, 0, 2 * Math.PI);
ctx.fillStyle = "white";
ctx.fill();

ctx.beginPath();
ctx.arc(pos * 2, pos, 20, 0, 2 * Math.PI);
ctx.fillStyle = "red";
ctx.fill();