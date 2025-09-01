//  a.

const add = (a, b) => {
    console.log(a + b)
    return a + b;
}

const myObject = {
    value: 10,
    multiply: function (n) {
        setTimeout(() => {
            console.log(this.value * n);
        }, 500)
    }
};

//  b.

const name = `Kimi`;
const greeting = `Hei, ${name}! Tervetuloa JavaScript-maailmaan.`;

const message = `Ensimmäinen tekstirivi
Toinen tekstirivi, jonka on kirjoittanut ${name}.`;

//c.

const fruits = ["omena", "banaani", "appelsiini"];
const vegetables = ["pinaatti", "porkkana", "peruna"];

const yhdistetty = [...fruits, ...vegetables]

console.log(yhdistetty);