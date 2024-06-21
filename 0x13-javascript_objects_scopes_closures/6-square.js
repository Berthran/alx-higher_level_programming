#!/usr/bin/node
const Square = require('./5-square');
class Square extends Square {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    let i;
    if (c === undefined) {
      c = 'X';
    }
    for (i = 0; i < this.size; i++) {
      console.log(c.repeat(this.size));
    }
  }
}
module.exports = Square;
