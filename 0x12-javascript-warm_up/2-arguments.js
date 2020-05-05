#!/usr/bin/node
// If no arguments are passed, prints “No argument”
// If only one argument is passed, prints "Argument found”
// Otherwise, prints “Arguments found”

const myArgs = process.argv.slice(2);
const length = myArgs.length;

if (length === 0) {
  console.log('No argument');
} else if (length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
