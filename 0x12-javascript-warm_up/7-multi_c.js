#!/usr/bin/node
// Prints “C is fun” depending on the integer argument passed

const myArgs = process.argv.slice(2);
const msg = 'C is fun';

let i = 0;

if (myArgs[0] === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (; i < myArgs[0]; i++) {
    console.log(msg);
  }
}
