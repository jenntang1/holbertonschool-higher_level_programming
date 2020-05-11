#!/usr/bin/node
// Function that prints the number of arguments already printed and the new argument value

exports.logMe = function (item) {
  let counter = 0;
  function increment () {
    return counter++;
  }
  console.log(counter + ": " + item);
};
