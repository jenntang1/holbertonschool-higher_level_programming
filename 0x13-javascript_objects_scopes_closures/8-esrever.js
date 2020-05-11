#!/usr/bin/node
// Function returns the number of occurrences in a list

exports.esrever = function (list) {
  const newList = [];
  let i = list.length - 1;
  for (; i >= 0; i--) {
    newList.push(list[i]);
  }
  return newList;
};
