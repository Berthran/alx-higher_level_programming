#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

// Making a GET request
request(url, function (err, response, body) {
  if (err) {
    console.error('code:', response.statusCode);
  } else {
    console.log('code:', response.statusCode);
  }
});
