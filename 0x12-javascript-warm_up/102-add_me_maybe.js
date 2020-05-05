#!/usr/bin/node
// Function increments and executes a function

exports.addMeMaybe = function (number, theFunction) {
  return number + theFunction(number + 1);
};
