#!/usr/bin/node
// Square class with a charPrint(c) instance method

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    if (size <= 0) {
      return new Square();
    } else if (size >= 1) {
      this.size = size;
    }
  }

  charPrint (c) {
    let row = 0;
    let col = 0;
    let str = '';
    if (c === undefined) {
      c = 'X';
      for (; row < this.height; row++) {
        for (; col < this.width; col++) {
          str += c;
        }
        console.log(str);
      }
    } else {
      for (; row < this.height; row++) {
        for (; col < this.width; col++) {
          str += c;
        }
        console.log(str);
      }
    }
  }
}

module.exports = Square;
