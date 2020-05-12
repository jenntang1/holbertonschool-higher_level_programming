#!/usr/bin/node
// Writes a string to a file

// Reads and saves command line args to a list
const myArgs = process.argv.slice(2);

// Imports fs module to write to a file
// If there's an error, then print the error object
// If not, print the content of the file
const fs = require('fs');
fs.writeFile(myArgs[0], myArgs[1], 'utf-8', (error) => {
  if (error) {
    console.error(error);
  }
});
