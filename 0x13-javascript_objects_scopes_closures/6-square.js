#!/usr/bin/node
// Square class with a charPrint(c) instance method

const ParentSquare = require('./5-square.js');

module.exports = class Square extends ParentSquare {
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
};
