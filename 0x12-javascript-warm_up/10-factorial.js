#!/usr/bin/node

const num1 = parseInt(process.argv[2]);

function factorial (num) {
  if (num === 0) {
    return (1);
  } else if (process.argv[2] == null) {
    return (1);
  } else {
    return (num * factorial(num - 1));
  }
}
console.log(factorial(num1));
