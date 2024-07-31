#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films`;
const char_url = 'https://swapi-api.alx-tools.com/api/people/18/';
let no_films = 0;
var films = [];
let count = 0;

// Making a GET request
request(url, function (error, response, body) {
	if (error) console.log(error)
	// Printing status code
	// Printing body
	no_films = JSON.parse(body).count;
	console.log(no_films)
	films = JSON.parse(body).results;
	console.log(films.length)
	for (let i = 0; i < 1; i++) {
		console.log(films[i].characters.length)
		console.log(" ")
		for (let j = 0; j < films[i].characters.length; j++) {
			console.log(films[i].characters[j])
			if (films[i].characters[j] === char_url) {
				count++;
			}
		}
	}	
	console.log(count);
});
