#!/usr/bin/node
// Rectangle with a print instance method

class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
    if (w <= 0 || h <= 0) {
      return {};
    }
  }

  print () {
    const syb = 'X';
    let row = 0;
    let col = 0;
    let str = '';
    for (; row < this.height; row++) {
      for (; col < this.width; col++) {
        str += syb;
      }
      console.log(str);
    }
  }
}

module.exports = Rectangle;
