#!/usr/bin/node
// Prints a square

const myArgs = process.argv.slice(2);
const msg = 'Missing size';
const symbol = 'X';

let i = 0;

if (myArgs[0] === undefined) {
  console.log(msg);
} else if (parseInt(myArgs[0])) {
  for (; i < myArgs[0]; i++) {
    console.log(symbol.repeat(myArgs[0]));
  }
} else {
  console.log(msg);
}
