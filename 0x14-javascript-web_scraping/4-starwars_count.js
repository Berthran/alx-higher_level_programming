#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let characters = {};
let parts = [];
// const charUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
let count = 0;

// Making a GET request
request(url, function (err, response, body) {
  if (err) {
    // Do nothing
  } else {
    for (let i = 0; i < JSON.parse(body).count; i++) {
      characters = JSON.parse(body).results[i].characters;
      for (let j = 0; j < characters.length; j++) {
        parts = characters[j].split('/');
        if (parts[parts.length - 2] === "18") {
          count++;
        }
      }
      // if (parts[parts.length - 2] === '18') {
      //  count++;
      // }
      // if (JSON.parse(body).results[i].characters.includes(charUrl)) {
      //  count++;
    }
  }
  console.log(count);
}
);
