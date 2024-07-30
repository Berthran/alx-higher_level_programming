#!/usr/bin/node
const fs = require('fs');

try {
  // Synchronous read
  const data = fs.readFileSync('example.txt', 'utf8');
  console.log('File content:', data);
} catch (err) {
  console.error('Error reading file:', err);
}

