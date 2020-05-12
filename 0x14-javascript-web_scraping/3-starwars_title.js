#!/usr/bin/node
// Show the body response
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const num = process.argv[2];

request(url + num, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }
  console.log(JSON.parse(body).title);
});
