#!/usr/bin/node
// If no arguments are passed, prints “No argument”
// If an argument is passed, prints all  arguments

const myArgs = process.argv.slice(2);
const length = myArgs.length;
let i = 0;

if (length === 0) {
  console.log('No argument');
} else {
  for (; i < length; i++) {
    console.log(myArgs[i]);
  }
}
