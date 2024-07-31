const request = require('request-promise');

request('https://swapi-api.alx-tools.com/films')
  .then(function (response) {
    // This runs when the website sends back an answer
    console.log('Here’s the information:', response);
  })
  .catch(function (err) {
    // This runs if there was a problem with the request
    console.log('Oops, something went wrong:', err);
  });

