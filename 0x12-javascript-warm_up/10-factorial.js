#!/usr/bin/node
// Computes and prints a factorial
// Formula: n! = n × (n−1)!
// Example: 4! = 4 x 3 x 2 x 1 = 24
// Note: 1. ignore negative numbers
//       2. 0! = 1
//       3. 1! = 1

const myArgs = process.argv.slice(2);

function factorial (num) {
  if (parseInt(num) === 0 || parseInt(num) === 1 || isNaN(num)) {
    return 1;
  } else if (parseInt(num) < 0) {
    // pass
  } else {
    return parseInt(num) * factorial(parseInt(num) - 1);
  }
}

console.log(factorial(myArgs[0]));
