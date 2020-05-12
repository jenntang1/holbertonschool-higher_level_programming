#!/usr/bin/node
// Reads and prints content of a file

// Reads and saves command line args to a list
const myArgs = process.argv.slice(2);

// Imports fs module to read file
// If there's an error, then print the error object
// If not, print the content of the file
const fs = require('fs');
fs.readFile(myArgs[0], 'utf-8', (error, content) => {
  if (error) {
    console.error(error);
  } else {
    console.log(content);
  }
});
