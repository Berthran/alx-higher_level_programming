#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
let characters = {};

// Making a GET request
request(url, function (err, response, body) {
  if (err) {
    console.error('code:', response.statusCode);
  } else {
    characters = JSON.parse(body).characters;
    for (let i = 0; i < characters.length; i++) {
      request(characters[i], function (err, response, body) {
        if (err) {
          console.error('code:', response.statusCode);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
