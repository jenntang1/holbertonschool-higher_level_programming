#!/usr/bin/node
// Square class that inherits from Rectangle

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
}

module.exports = Square;
