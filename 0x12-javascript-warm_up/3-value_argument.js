#!/usr/bin/node

const myVar0 = 'No argument';

if (process.argv[2] == null) {
  console.log(myVar0);
} else {
  console.log(process.argv[2]);
}
