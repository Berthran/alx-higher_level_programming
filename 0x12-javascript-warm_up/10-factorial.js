#!/usr/bin/node
function factorial (a) {
  if (isNaN(a)) {
    return (1);
  }
  if (a === 1) {
    return (1);
  }
  return (a * factorial(a - 1));
}

const value = parseInt(process.argv.slice(2)[0]);
const result = factorial(value);
console.log(result);
