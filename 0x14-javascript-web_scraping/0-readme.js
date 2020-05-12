#!/usr/bin/node
// Read file
const fs = require('fs');
try {
  const data1 = fs.readFileSync(process.argv[2], 'utf8');
  console.log(data1);
} catch (err) {
  console.error(err);
}
