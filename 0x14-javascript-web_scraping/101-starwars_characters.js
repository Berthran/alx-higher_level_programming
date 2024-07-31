#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
let characters = {};

// TRIAL 1
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

const requestPromise = (url) => {
  return new Promise((resolve, reject) => {
    request(url, function (err, response, body) {
      if (err) {
        reject(err);
      } else {
        resolve(body);
      }
    });
  });
};

(async () => {
  try {
    const body = await requestPromise(url);
    characters = JSON.parse(body).characters;
    for (let i = 0; i < characters.length; i++) {
      const character = await requestPromise(characters[i]);
      console.log(JSON.parse(character).name);
    }
  } catch (err) {
    console.error('code:', err.statusCode);
  }
})();
