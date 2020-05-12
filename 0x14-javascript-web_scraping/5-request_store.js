#!/usr/bin/node
// Gets and saves webpage content to a file

// Reads and saves command line args to a list
const myArgs = process.argv.slice(2);

// Imports request module to make http call
// Imports fs module to write to a file
const request = require('request');
const fs = require('fs');

// GET request and save to file
request.get(myArgs[0], function (error, response, body) {
  if (body) {
    fs.writeFile(myArgs[1], body, 'utf-8', (error) => {
      if (error) {
        console.error(error);
      }
    });
  } else {
    console.error(error);
  }
});
