#!/usr/bin/node
// Function the executes a function x number of times

exports.callMeMoby = function (x, theFunction) {
  let i = 0;
  for (; i < x; i++) {
    theFunction();
  }
};
