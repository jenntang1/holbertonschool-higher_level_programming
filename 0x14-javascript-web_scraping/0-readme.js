#!/usr/bin/node
// Reads and prints content of a file

// Reads and saves command line args to a list
const myArgs = process.argv.slice(2);

// Imports fs module to read file
// If there's an error, then print the error object
// If not, print the content of the file
const fs = require('fs');

fs.open(myArgs[0], 'r', function (error, stat) {
  if (error === null) {
    fs.readFile(myArgs[0], 'utf-8', function (error, content) {
      if (error) {
        const errMsg = { Error: error.message };
        const obj = Object.assign({}, errMsg, error);
        console.log(obj);
      } else if (content) {
        process.stdout.write(content);
      }
    });
  } else if (error.code === 'ENOENT') {
    const errMsg = { Error: error.message };
    const obj = Object.assign({}, errMsg, error);
    console.log(obj);
  }
});
