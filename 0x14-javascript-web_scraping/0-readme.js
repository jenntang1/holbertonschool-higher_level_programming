#!/usr/bin/node
// Reads and prints content of a file

// Reads and saves command line args to a list
const myArgs = process.argv.slice(2);

// Imports fs module to read file
// If there's an error, then print the error object
// If not, print the content of the file
const fs = require('fs');
const file = myArgs[0];

fs.open(file, 'r', (error, fd) => {
  if (error) {
    console.log(error);
  } else {
    fs.readFile(file, 'utf-8', (error, content) => {
      if (error) {
        console.log(error);
      } else {
        process.stdout.write(content);
      }
    });
  }
});
