#!/usr/bin/node
// Displays status code of a GET request

// Reads and saves command line args to a list
const myArgs = process.argv.slice(2);

// Imports request module to make http call
// Prints the response status code
// If there's an error, still print its status code
const request = require('request');
request.get(myArgs[0], function (error, response) {
  if (error || response) {
    console.log('code:', response.statusCode);
  }
});
