#!/usr/bin/node
// Finds the second largest integer in list
// Bubble sorts the list and returns the second to last element
// If no argument passed, print "0"
// If only one argument passed, print "0"

const myArgs = process.argv.slice(2);
const length = myArgs.length;
const newArr = myArgs.map(Number);

if (length <= 1) {
  console.log('0');
} else {
  let i, j, swap;
  for (i = 0; i < length - 1; i++) {
    for (j = 0; j < length - i - 1; j++) {
      if (newArr[j] > newArr[j + 1]) {
        swap = newArr[j];
        newArr[j] = newArr[j + 1];
        newArr[j + 1] = swap;
      }
    }
  }
  console.log(newArr[length - 2]);
}
