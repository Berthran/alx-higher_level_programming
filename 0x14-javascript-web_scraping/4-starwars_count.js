#!/usr/bin/node
// Write a script that prints the number of movies where the character “Wedge Antilles” is present.
// The first argument is the API URL of the Star wars API: https://swapi-api.alx-tools.com/api/films/
// Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
// You must use the module request

const request = require('request');
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/';
const characterId = 18;

request(apiUrl, function (error, response, body) {
  if (error) {
    // Do nothing
  } else {
    const films = JSON.parse(body).results;
    const moviesWithWedgeAntilles = films.filter(film => film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`));
    console.log(moviesWithWedgeAntilles.length);
  }
});
