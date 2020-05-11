#!/usr/bin/node
// Rectangle with a print, rotate and double instance methods

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

  rotate () {
    let swap;
    swap = this.width;
    this.width = this.height;
    this.height = swap;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
