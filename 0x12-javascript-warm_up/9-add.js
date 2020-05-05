#!/usr/bin/node
// Prints the sum of two integers

const myArgs = process.argv.slice(2);
const length = myArgs.length;

function add (a, b) {
  let sum = 0;
  if (length <= 1) {
    return NaN;
  } else {
    sum = parseInt(a) + parseInt(b);
    return sum;
  }
}

console.log(add(myArgs[0], myArgs[1]));
