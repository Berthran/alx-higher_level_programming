#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const charUrl = 'https://swapi-api.hbtn.io/api/people/18';
let count = 0;

// Making a GET request
request(url, function (err, response, body) {
  if (err) {
    console.error('code:', response.statusCode);
  } else {
    for (let i = 0; i < JSON.parse(body).count; i++) {
      if (JSON.parse(body).results[i].characters.includes(charUrl)) {
        count++;
      }
    }
    console.log(count);
  }
});
