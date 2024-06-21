#!/usr/bin/node
// Import the list from the file 100-data.js
const { list } = require('./100-data.js');

// Compute a new array where each value is the value of the initial list multiplied by the index
const newList = list.map((value, index) => value * index);

// Print the initial list
console.log(list);

// Print the new list
console.log(newList);
