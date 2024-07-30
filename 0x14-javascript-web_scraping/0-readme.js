#!/usr/bin/node
const fs = require('fs');
const filepath = process.argv[2];

// Asynchronous read
fs.readFile(filepath, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data);
});
