#!/usr/bin/node
// Import the required modules
const fs = require('fs');
const process = require('process');

// Extract file paths from command line arguments
const [sourceFile1, sourceFile2, destinationFile] = process.argv.slice(2);

// Read the content of the first source file
fs.readFile(sourceFile1, 'utf8', (err, data1) => {
  if (err) throw err;

  // Read the content of the second source file
  fs.readFile(sourceFile2, 'utf8', (err, data2) => {
    if (err) throw err;

    // Concatenate the content of both source files
    const concatenatedData = data1 + data2;

    // Write the concatenated content to the destination file
    fs.writeFile(destinationFile, concatenatedData, (err) => {
      if (err) throw err;
    });
  });
});
