const MathLibrary = require("./mathlib");
const math = new MathLibrary();

const a = 4;
const b = 5;

let sum = (math.add(a,b));
let mult = (math.multiply(a,b));
let squ = (math.square(a));

console.log(a + " plus " + b + " = ", sum);
console.log(a + " x " + b + " = ", mult);
console.log(a + " squred = ", squ);
console.log("Random between " + a + " and " + b + ": ", math.random(a, b));
