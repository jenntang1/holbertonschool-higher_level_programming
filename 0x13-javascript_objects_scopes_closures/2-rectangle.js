#!/usr/bin/node
// Rectangle with conditions

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      return new Rectangle();
    } else if (w >= 1 && h >= 1) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
