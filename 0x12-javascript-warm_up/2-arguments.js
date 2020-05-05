#!/usr/bin/node

const myVar0 = 'No argument';
const myVar1 = 'Argument found';
const myVar2 = 'Arguments found';

if (process.argv[2] == null) {
  console.log(myVar0);
} else if (process.argv[3] == null) {
  console.log(myVar1);
} else {
  console.log(myVar2);
}
