#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];
let content = '';

// Making a GET request
request(url, function (err, response, body) {
  if (err) {
    // Do nothing
  } else {
    content = body;
  }

  fs.writeFile(file, content, 'utf-8', function (err) {
    if (err) {
      console.log(err);
    }
  });
}
);

// What is the problem with this code?
// A: The fs module is not imported
// B: The fs.writeFile function is not inside the request function
// C: The fs.writeFile function is not correctly written

// Why should the fs.writeFile function be inside the request function?
// A: To ensure that the file is written only after the request is completed
