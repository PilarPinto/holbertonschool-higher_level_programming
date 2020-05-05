#!/usr/bin/node

const lists = [];

if (process.argv[2] == null || process.argv[3] == null) {
  console.log(0);
} else {
  for (let ind = 2; ind < process.argv.length; ind++) {
    lists.push(process.argv[ind]);
  }
  lists.sort(function (x, y) {
    return x - y;
  });
  lists.pop();
  const may = lists.slice(-1);
  const num = parseInt(may);
  console.log(num);
}
