#!/usr/bin/node
// Function returns the number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  let i = 0;
  for (; i < list.length; i++) {
    if (list[i] === searchElement) {
      count++;
    }
  }
  return count;
};
