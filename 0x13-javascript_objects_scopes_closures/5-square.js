#!/usr/bin/node
// Square class that inherits from Rectangle

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    if (size <= 0) {
      return new Square();
    } else {
      super(size, size);
      this.size = size;
    }
  }
}

module.exports = Square;
