#!/usr/bin/node
const value = process.argv.slice(2)[0];
const result = parseInt(value);
if (isNaN(result)) {
  console.log('Not a number');
} else {
  console.log('My number:', result);
}
