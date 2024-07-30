#!/usr/bin/node
const request = require('request');
const url = 'http://jsonbin.io/b/591a64459208345676e6a1ed';
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).name);
  }
});
