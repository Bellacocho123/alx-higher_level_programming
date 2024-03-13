#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) return;
    if (w === undefined || h === undefined) return;
    this.width = w;
    this.height = h;
  }

  print () {
    let i;
    let j;
    let str = '';
    for (i = 0; i < this.width; i++) {
      str += 'X';
    }
    for (j = 0; j < this.height; j++) {
      console.log(str);
    }
  }
}

module.exports = Rectangle;
