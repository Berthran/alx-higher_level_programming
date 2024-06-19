#!/usr/bin/node
const firstArg = process.argv.slice(2)[0];
const size = parseInt(firstArg);
let i, j;
let square = '';
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (i = 0; i < size; i++) {
    square = '';
    for (j = 0; j < size; j++) {
      square += 'X';
    }
    console.log(square);
  }
}
