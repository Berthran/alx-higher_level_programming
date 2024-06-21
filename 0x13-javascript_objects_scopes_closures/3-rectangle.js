#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i, j;
    let rect = '';
    for (i = 0; i < this.height; i++) {
      rect = '';
      for (j = 0; j < this.width; j++) {
        rect += 'X';
      }
      console.log(rect);
    }
  }
}
module.exports = Rectangle;
