#!/usr/bin/node
const fs = require('fs');
const path = process.argv[2];

// Asynchronous read
fs.readFile(path, 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading file:', err);
    return;
  }
  console.log('File content:', data);
});

