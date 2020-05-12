#!/usr/bin/node
// Count in the body response
const request = require('request');
const url = process.argv[2];
let counter = 0;

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }
  const rtaLst = JSON.parse(body).results;

  for (const ind in rtaLst) {
    const characterLst = rtaLst[ind].characters;
    for (const i in characterLst) {
      if (characterLst[i].includes('18')) {
        counter = counter + 1;
      }
    }
  }
  console.log(counter);
});
