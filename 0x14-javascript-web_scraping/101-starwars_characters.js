#!/usr/bin/node
// Show the body response of characters
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const num = process.argv[2];
const dicti = {};

request(url + num, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }
  const charLst = JSON.parse(body).characters;
  for (const ind in charLst) {
    request(charLst[ind], function (error, response, body) {
      if (error) {
        console.error('error:', error);
      }
      dicti[ind] = JSON.parse(body).name;
      const len1 = Object.keys(dicti).length;
      if (charLst.length === len1) {
        for (const k in dicti) {
          console.log(dicti[k]);
        }
      }
    });
  }
});
