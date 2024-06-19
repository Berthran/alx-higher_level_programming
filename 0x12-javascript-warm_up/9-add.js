#!/usr/bin/node
function add (a, b) {
  return (a + b);
}

const firstArg = parseInt(process.argv.slice(2)[0]);
const secondArg = parseInt(process.argv.slice(2)[1]);
console.log(add(firstArg, secondArg));
