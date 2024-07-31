#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
let characters = {};

// Making a GET request
// request(url)
//   .then(body => {
//     characters = JSON.parse(body).characters;
//     const requests = characters.map(character => request(character));
//     return Promise.all(requests);
//   })
//   .then(characterResponses => {
//     characterResponses.forEach(character => {
//       console.log(JSON.parse(character).name);
//     });
//   })
//   .catch(err => console.error('code:', err.statusCode));
request(url, function (err, response, body) {
  console.log("Approaching if block...");
  if (err) {
    console.error('code:', response.statusCode);
  } else {
    console.log("In else block...");
    characters = JSON.parse(body).characters;
    console.log('characters:', characters);
    for (let i = 0; i < characters.length; i++) {
      console.log("within for loop");
      request(characters[i], function (err, response, body) {
        if (err) {
          console.error('code:', response.statusCode);
        } else {
          console.log("i current value:", i);
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
