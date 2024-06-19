#!/usr/bin/node
const firstArg = process.argv.slice(2)[0];
const iter = parseInt(firstArg);
let i;
if (isNaN(iter)) {
  console.log('Missing number of occurences');
}
for (i = 0; i < iter; i++) {
  console.log('C is fun');
}
