#!/usr/bin/node
// Function returns the sum of two integers

exports.add = function add (a, b) {
  let sum = 0;
  sum = parseInt(a) + parseInt(b);
  return sum;
};
