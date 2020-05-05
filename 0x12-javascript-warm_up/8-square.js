#!/usr/bin/node
const num = process.argv[2];
let str = '';
if (parseInt(num)) {
  for (let i = 0; i < num; i++) {
    for (let j = 0; j < num; j++) {
      str = str.concat('X');
    }
    if (i === num - 1) {
    } else { str = str.concat('\n'); }
  }
  console.log(str);
} else {
  console.log('Missing size');
}
