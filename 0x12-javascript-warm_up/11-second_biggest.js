#!/usr/bin/node
const args = process.argv.slice(2);
const lenArgs = args.length;
if (lenArgs > 1) {
  const argsDesc = args.sort((a, b) => b - a);
  console.log(argsDesc[1]);
} else {
  console.log(0);
}
