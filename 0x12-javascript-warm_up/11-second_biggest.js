#!/usr/bin/node
// Finds the second largest integer in list
// Sorts the list and returns the second to last element
// If no argument passed, print "0"
// If only one argument passed, print "0"

const myArgs = process.argv.slice(2);
const length = myArgs.length;

if (length <= 1) {
  console.log('0');
} else {
  let i, j, swap;
  for (i = 0; i < length; i++) {
    for (j = i + 1; j < length; j++) {
      if (myArgs[i] > myArgs[j]) {
        swap = myArgs[i];
        myArgs[i] = myArgs[j];
        myArgs[j] = swap;
      }
    }
  }
  console.log(myArgs[length - 2]);
}
