#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const users = {};

// Making a GET request
request(url, function (err, response, body) {
  if (err) {
    console.error('code:', response.statusCode);
  } else {
    for (let i = 0; i < JSON.parse(body).length; i++) {
      if (JSON.parse(body)[i].completed === true) {
        if (users[JSON.parse(body)[i].userId] === undefined) {
          users[JSON.parse(body)[i].userId] = 1;
        } else {
          users[JSON.parse(body)[i].userId] += 1;
        }
      }
    }
    console.log(users);
  }
}
);
