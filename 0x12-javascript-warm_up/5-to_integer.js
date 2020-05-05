#!/usr/bin/node
// If first argument can be converted to an integer, then print "My number: <integer>"
// If argument can't be converted, then print "Not a number"

const myArgs = process.argv.slice(2);

if (parseInt(myArgs[0])) {
  console.log('My number:', myArgs[0]);
} else {
  console.log('Not a number');
}
