#!/usr/bin/node
// Count in the body response
const request = require('request');
const url = process.argv[2];
const taksT = {};
const lst = [];
request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }
  const todoLst = JSON.parse(body);
  for (const ind in todoLst) {
    const task = todoLst[ind];
    if (task.completed === true) {
      lst.push(task.userId);
    }
  }

  lst.forEach(function (i) { taksT[i] = (taksT[i] || 0) + 1; });
  console.log(taksT);
});
