#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

// Making a GET request
request(url, function (err, response, body) {
  if (err) {
    console.error('code:', response.statusCode);
  } else {
    console.log(JSON.parse(body).title);
  }
});
