#!/usr/bin/node
function add(a, b) {
	console.log(a + b);
}

const firstArg = parseInt(process.argv.slice(2)[0]);
const secondArg = parseInt(process.argv.slice(2)[1]);
add(firstArg, secondArg);
