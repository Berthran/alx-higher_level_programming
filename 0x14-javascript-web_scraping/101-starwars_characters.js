#!/usr/bin/node
const request = require('request-promise');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
let characters = {};

// Making a GET request
request(url)
  .then(body => {
    characters = JSON.parse(body).characters;
    const requests = characters.map(character => request(character));
    return Promise.all(requests);
  })
  .then(characterResponses => {
    characterResponses.forEach(character => {
      console.log(JSON.parse(character).name);
    });
  })
  .catch(err => console.error('code:', err.statusCode));
// request(url, function (err, response, body) {
//   if (err) {
//     console.error('code:', response.statusCode);
//   } else {
//     characters = JSON.parse(body).characters;
//     for (let i = 0; i < characters.length; i++) {
//       request(characters[i], function (err, response, body) {
//         if (err) {
//           console.error('code:', response.statusCode);
//         } else {
//           console.log(JSON.parse(body).name);
//         }
//       });
//     }
//   }
// });
