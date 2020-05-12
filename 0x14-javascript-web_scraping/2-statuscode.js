#!/usr/bin/node
// Show the status code
const request = require('request');
const url = process.argv[2];
request.get(url).on('response', function (response) {
  console.log('code:', response.statusCode);
});
