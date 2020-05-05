#!/usr/bin/node
// If no arguments are passed, prints “No argument”
// If an argument is passed, prints all  arguments

const myArgs = process.argv.slice(2);

if (myArgs[0] === undefined) {
  console.log('No argument');
} else {
  myArgs.forEach(element => console.log(element));
}
