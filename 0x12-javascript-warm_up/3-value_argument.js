#!/usr/bin/node
// If no arguments are passed, prints “No argument”
// If an argument is passed, prints the first argument

const myArgs = process.argv.slice(2);
const length = myArgs.length;

if (length === 0) {
  console.log('No argument');
} else {
  console.log(myArgs[0]);
}
