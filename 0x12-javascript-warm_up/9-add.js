#!/usr/bin/node

const myVar0 = 'NaN';
const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);

if (process.argv[2] == null) {
  console.log(myVar0);
} else if (process.argv[3] == null) {
  console.log(myVar0);
} else {
  const suma = num1 + num2;
  console.log(suma);
}
