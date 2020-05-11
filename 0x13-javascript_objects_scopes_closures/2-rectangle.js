#!/usr/bin/node
// Rectangle with conditions

class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
    if (w <= 0 || h <= 0) {
      return {};
    }
  }
}

module.exports = Rectangle;
