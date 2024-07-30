#!/usr/bin/node
const request = require('request');

const url = 'http://jsonbin.io/b/591a64459208345676e6a1ed';

request(url, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else {
    console.log('Status Code:', response.statusCode);
    console.log('Body:', body);
  }
});

