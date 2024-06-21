#!/usr/bin/node
// Import the dictionary from the file 101-data.js
const { dict } = require('./101-data.js');

// Compute a dictionary of user ids by occurrence
const occurrencesById = Object.entries(dict).reduce((acc, [userId, occurrence]) => {
  // If the occurrence already exists in the accumulator, push the userId to the array
  if (acc[occurrence]) {
    acc[occurrence].push(parseInt(userId));
  } else {
    // Otherwise, create a new array with the userId
    acc[occurrence] = [parseInt(userId)];
  }
  return acc;
}, {});

// Print the new dictionary
console.log(occurrencesById);
